from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
#method to send email
def send_welcome_email(name,sender,message):
    #get subject and sender
    subject="Hello friend"
    receiver="collinsnjau39@gmail.com"

    #pass in the template
    text_content=render_to_string('email/newsemail.txt',{"message":message})
    html_content=render_to_string('email/newsemail.html',{"message":message})

    msg=EmailMultiAlternatives(subject,html_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
