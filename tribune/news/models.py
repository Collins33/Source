from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField




# # Create your models here.
# class Editor(models.Model):
#     firstName=models.CharField(max_length=30)
#     lastName=models.CharField(max_length=30)
#     email=models.EmailField()
#     #make model readable from the shell
#
#
#     def __str__(self):
#         return self.firstName
#     #save method
#     def saveEditor(self):
#         self.save()
#
#     #delete method
#     def deleteEditor(self):
#         self.delete()
#
#     class Meta:
#         ordering=['firstName']

class tags(models.Model):
    name=models.CharField(max_length=30)

    #make model readable from the shell
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/',blank =True)


    @classmethod
    def today_news(cls):
        today=dt.date.today()
        news=cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news_article=cls.objects.filter(title__icontains=search_term)
        return news_article

    @classmethod
    def allPosts(cls):
        allArticles=cls.objects.all()
        return allArticles

    def __str__(self):
        return self.title


class NewsLetterRecipient(models.Model):
    name=models.CharField(max_length=30)
    text=models.CharField(max_length=200,default="Hello my friend")
    email=models.EmailField()


class Project(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    github=models.CharField(max_length=100)
    live_url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='articles/',blank=True)
