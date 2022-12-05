import unittest

from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib import auth

from django.test import TestCase, Client

class userTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create()
            
    def test_signUp(self):
        print(self._testMethodName)
        newUser=User.objects.create_user("robot", "robot@gmail.com", "pass")
        data= {
        "username":"robot",
        "firstname":"machine",
        "lastname":"language",
        "email":"shashiteja441@gmail.com",
        "password" : "pass",
        "confirm-password" : "pass",
        "is_active": True
        }   
        response = self.client.post('/signup/', data=data)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(username="robot"))

    def test_Login(self):
        print(self._testMethodName)
        data ={
            "username":"robot",
            "password":"passs"
        }
        
        user = authenticate(username="robot",password="pass")
        response = self.client.post('/login/', data=data)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    
    def test_modifyProfile(self):
        print(self._testMethodName)
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        newUser.first_name="machine"
        newUser.last_name="language"
        newUser.save()
        
        self.client.login(username='robot', password='pass')
        data= {
            'username':"robot",
            'firstname':"machine",
            'lastname':"learning",
            'email':'robot@gmail.com'
        }
        
        response = self.client.post('/modifyprofile/', data=data)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code,200)
        self.assertEqual(User.objects.get(username="robot").last_name,"learning")    
        
    def test_changeProfilePassword(self):
        print(self._testMethodName)
        User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        user = User.objects.get(username = "robot")
        user.set_password("newPass")
        user.save()
        data= {
            "username" : "robot",
            "password" : "newPass",
            "success" : "success"
        }
        self.assertTrue(self.client.login(username='robot', password='newPass'))
        response = self.client.post('/changeprofilepassword/',data=data)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code,200)
        
    def test_logout(self):
        print(self._testMethodName)
        User.objects.create_user(username="black",email="black@gmail.com",password="white")
        user = User.objects.get(username = "black")
        user.save()
        self.client.login(username='black', password='white')
        data= {
            "success" : "successfully logged out"
        }
        response = self.client.post('/logout/',data=data)
        reponse1=self.client.logout()
        self.assertTrue(response)