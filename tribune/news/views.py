from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Article,NewsLetterRecipient,Project
from .forms import NewsLetterForm,NewsArticleForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import JsonResponse



#handles the api
class ProjectList(APIView):
    permission_class=(IsAdminOrReadOnly)
    def get(self,request,format=None):#get data from the database
        all_projects=Project.objects.all()
        serializers=ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers=ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)










def welcome(request):
    form=NewsLetterForm()

    return render(request,"welcome.html",{"NewsLetterForm":form})

def newsLetter(request):
    name=request.POST.get('your_name')
    email=request.POST.get('email')
    text=request.POST.get('message')
    recipient=NewsLetterRecipient(name=name,email=email,text=text)
    # recipient.save()

    send_welcome_email(name,email,text)
    data={'success':'You have been added to the mailing list'}
    return JsonResponse(data)


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


def myProject(request):#get all the projects and display them
    allProjects=Project.allProjects()
    return render(request,"project.html",{"projects":allProjects})

#this view function displays a single project
def project(request,project_id):
    try:
        project=Project.objects.get(id=project_id)#grt project that matches project_id
    except DoesNotExist:
        raise Http404()# if it does not exist throw 404 error

    return render(request,'projectDetail.html',{"project":project})

#for searching for the projects based on the language
def searchProjects(request):
    #check if the project query is in the request.GET object and check if it has a Value
    if "project" in request.GET and request.GET["project"]:
        #get the searched term
        search_term=request.GET.get("project")
        #pass the searched term to the method to filter the projects
        searched_projects=Project.search_by_language(search_term)
        #create message to render
        message=f"{search_term}"

        return render(request,"searchProjects.html",{"message":message,"searched_projects":searched_projects})

    else:
        message="You havent searched for any item"
        return render(request,"searchProjects.html",{"message":mesage})
