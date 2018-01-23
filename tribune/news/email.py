from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
#method to send email
def send_welcome_email(name,receiver):
    #get subject and sender
    subject="Welcome to the THE SOURCE"
    sender="collinsnjau39@gmail.com"
    #pass in the template
    text_content=render_to_string('email/newsemail.txt',{'name':name})
    html_content=render_to_string('email/newsemail.html',{'name':name})

    msg=EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
