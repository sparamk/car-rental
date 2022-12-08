import warnings
from django.test import TestCase
import unittest,datetime
from django.db import models
from car.models import *
from django.contrib.auth.models import User, Group

class test_car(TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ImportWarning)
        newUser=User.objects.create_user("robot", "robot@gmail.com", "pass")
        car=Cars.objects.create(car_name="INNOVA",color='red',capacity="5",rent_per_hour="10",cost_of_vehicle="100",is_available=False,description="good car",car_condition=False ,subscription="gold",date_added="2022-03-05")
        bk=Book_Car.objects.create(user=newUser,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=False,session_id="5")
        Book.objects.create(user=newUser,car=car,book_car=bk,from_date="2022-03-05",to_date="2022-03-05",is_paid=False,confirmation=False,date_created="2022-03-05")
    
    def test_book(self):
        print(self._testMethodName)
        b=Book.objects.get(to_date="2022-03-05")
        self.assertEqual(b.is_paid,False)
        self.assertEqual(b.confirmation,False)
        
        
        
if __name__ == '__main__':
    unittest.main()
    