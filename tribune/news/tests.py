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
