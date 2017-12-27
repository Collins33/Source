from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import datetime as dt

#the welcome view
def welcome(request):
    return HttpResponse("COLLINS NJAU")

def newsOfTheDay(request):
    date=dt.date.today()#get current date
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)        
