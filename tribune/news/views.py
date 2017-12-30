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
