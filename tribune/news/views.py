from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article




def newsOfTheDay(request):
    date=dt.date.today()#get current date
    news=Article.today_news()
    return render(request, 'allnews/today-news.html', {"date": date,"news":news})




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


def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'allnews/article.html',{"article":article})
