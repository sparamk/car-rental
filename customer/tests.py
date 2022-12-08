import warnings
from django.test import TestCase
import unittest,datetime
from django.db import models
from customer.models import *
from django.contrib.auth.models import User, Group
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 

class Test_customer(TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ImportWarning)
        newUser=User.objects.create_user("robot", "robot@gmail.com", "pass")
        Refer_Friend.objects.create(user=newUser,refer_friend="Welcome",refer_date="2022-03-05")

    def test_customer(self):
        newUser=User.objects.create_user("robot1", "robot1@gmail.com", "pass")
        Refer_Friend.objects.create(user=newUser,refer_friend="Welcome",refer_date="2022-03-05")
        c=Refer_Friend.objects.get(refer_friend="Welcome")
        self.assertCountEqual(c.refer_friend,"Welcome")
        
    def setUp(self):
        warnings.simplefilter('ignore', category=ImportWarning)
        newUser=User.objects.create_user("robot", "robot@gmail.com", "pass")
        car=Cars.objects.create(car_name="INNOVA",color='red',capacity="5",rent_per_hour="10",cost_of_vehicle="100",is_available=False,description="good car",car_condition=False ,subscription="gold",date_added="2022-03-05")
        bk=Book_Car.objects.create(user=newUser,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=False,session_id="5")
        bok=Book.objects.create(user=newUser,car=car,book_car=bk,from_date="2022-03-05",to_date="2022-03-05",is_paid=False,confirmation=False,date_created="2022-03-05")
        # Digital_Check_In.objects.create(user=newUser,check_in_date="2022-05-05",book=bok,date_added="2022-05-05")
        
        
if __name__ == '__main__':
    unittest.main()
        