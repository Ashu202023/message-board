from django.test import TestCase 
from .models import Post
from django.urls import reverse

class PostTests(TestCase):
    @classmethod 
    def setUpTestData(cls):
        cls.post=Post.objects.create(text="this is a test!")
    

    def test_model_content(self):
        self.assertEqual(self.post.text,"this is a test!")
    
    def test_url_exist(self):
        r=self.client.get("/")
        self.assertEqual(r.status_code,200)
        
    def test_homepage(self):
        r=self.client.get(reverse("home"))
        self.assertEqual(r.status_code,200)
        self.assertTemplateUsed(r,"posts_list.html")
        self.assertContains(r,"this is a test!")
    
    
    # def test_url_name_exist(self):
    #     r=self.client.get(reverse("home"))
    #     self.assertEqual(r.status_code,200)

    # def test_template_name(self):
    #     r=self.client.get(reverse("home"))
    #     self.assertTemplateUsed(r,"posts_list.html")
   
    
    

