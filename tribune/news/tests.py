from django.test import TestCase

# Create your tests here.
from .models import Editor,tags,Article

#test the editor module
class EditorTestClass(TestCase):
    #setup method
    def setUp(self):
        self.collins=Editor(firstName="colo",lastName="njau",email="collinsnjau39@gmail.com")

    #test that the instance is instantiated correctly
    def test_instance(self):
        self.assertTrue(isinstance(self.collins,Editor))
