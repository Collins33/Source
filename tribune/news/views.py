from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,Http404
import datetime as dt

#the welcome view
def welcome(request):
    return render(request,'welcome.html')

def newsOfTheDay(request):
    date=dt.date.today()#get current date
    day=convertDays(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convertDays(dates):
    dayNumber=dt.date.weekday(dates)#gets the number of the current day

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day=days[dayNumber]#get actual day

    return day

def pastDaysNews(request,pastDate):
    try:
        date=dt.datetime.strptime(pastDate,'%Y-%m-%d').date()#pass in the date and the format to convert to
    except ValueError:
        raise Http404()


    day=convertDays(date)#get the current day
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
