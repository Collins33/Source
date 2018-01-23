from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Article,NewsLetterRecipient
from .forms import NewsLetterForm,NewsArticleForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required



def welcome(request):
    return render(request,"welcome.html")

def blog(request):
    news_article=Article.allPosts()
    return render(request,"blog.html",{"news_article":news_article})

def newsOfTheDay(request):
    #check if it is a post request
    if request.method == 'POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']
            recipient=NewsLetterRecipient(name=name,email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('newsOfTheDay')
    else:
        form=NewsLetterForm()


    date=dt.date.today()#get current date
    news=Article.today_news()
    return render(request, 'allnews/today-news.html', {"date": date,"news":news,"NewsLetterForm":form})




def pastDaysNews(request,pastDate):
    try:
        date=dt.datetime.strptime(pastDate,'%Y-%m-%d').date()#pass in the date and the format to convert to
    except ValueError:
        raise Http404()
        assert False


    if date == dt.date.today():
        return redirect(newsOfTheDay)

    return render(request, 'allnews/past-news.html', {"date": date})


def search_results(request):
    #check if the article query exists in the request.GET
    if 'article' in request.GET and request.GET['article']:
        #get what the user searched for
        search_term=request.GET.get('article')
        #get the searched articles
        search_articles=Article.search_by_title(search_term)
        message = f"{search_term}"
        #render the template
        return render(request,'allnews/search.html',{"message":message,"articles":search_articles})
    else:
        message="You havent searched for any news articles"
        return render(request,'allnews/search.html',{"message":message})


@login_required(login_url='/accounts/login/')#only authenticated users can have access
def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'allnews/article.html',{"article":article})

@login_required(login_url='/accounts/login/')
def new_article(request):
    #get current users
    current_user=request.user
    if request.method=='POST':
        form=NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.editor=current_user
            article.save()

    else:
        form=NewsArticleForm()
    return render(request, 'new_article.html', {"form": form})
