
import json
import unittest
from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from feedback.models import Feedback

class Feedback_TestCase(TestCase):
    
    
    def setUp(self):
        pass
     
    def test_modelstest_test(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        Feedback.objects.create(feedback_text="good work",feedback_text_response="", user=newUser)
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.feedback_text,"good work")
    
    def test_modelstest_valid(self):
        print(self._testMethodName)
        newUser=User.objects.create_user(username="gyro",email="gyro@gmail.com",password="pass")
        Feedback.objects.create(feedback_text="our service",feedback_text_response="",user=newUser)
        feedback = Feedback()
        feedback.user_id = 9
        self.assertFalse(feedback.feedback_text,"")
    
    
    def test_feedback(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        self.client.login(username='robot', password='pass')
        Feedback.objects.create(feedback_text="good work",feedback_text_response="", user=newUser)
        
        fb=Feedback.objects.get(feedback_text="good work")
        data={
            "user_id": newUser.id,  
            "feedback_text":"good service",
            "feedback": "done dusted"
            }
        response=self.client.post('/feedback/sendfeedback/',data=data)
        self.assertEqual(response.status_code,200)