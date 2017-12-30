from django.test import TestCase

# Create your tests here.
from .models import Editor,tags,Article

#test the editor module
class EditorTestClass(TestCase):
    #setup method
    def setUp(self):
        self.collins=Editor(firstName="colo",lastName="njau",email="collinsnjau39@gmail.com")


    def tearDown(self):
        Editor.objects.all().delete()



    #test that the instance is instantiated correctly
    def test_instance(self):
        self.assertTrue(isinstance(self.collins,Editor))

    #test for the save method
    def test_save_method(self):
        self.collins.saveEditor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def test_delete_method(self):
        self.collins.saveEditor()
        editors=Editor.objects.all()
        self.collins.deleteEditor()
        self.assertTrue(len(editors) == 0)



#test the Article module
class ArticleTestClass(TestCase):
    def setUp(self):
        #create editor and save it
        self.njau=Editor(firstName="muru",lastName="merita",email="murunjau@gmail.com")
        self.njau.saveEditor()

        #create new tag and save it
        self.new_tag=tags(name="testing")
        self.new_tag.save()

        #create new Article
        self.new_article=Article(title = 'Test Article',post = 'This is a random test Post',editor=self.njau)
        self.new_article.save()

        #add the created tag to the ManyToManyField of the Article
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        #delete all instances of the models from the database
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()


    def test_get_news_today(self):
        #test for getting today news
        today_news=Article.today_news()
        self.assertTrue(len(today_news)>0)    
