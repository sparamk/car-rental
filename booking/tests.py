import warnings
from django.test import TestCase
import unittest,datetime
from django.db import models
from booking.models import Book_Car
from django.contrib.auth.models import User, Group
from .models import Cars,Coupons

class Test_Booking(TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ImportWarning)
        newUser=User.objects.create_user("robot", "robot@gmail.com", "pass")
        Book_Car.objects.create(user=newUser,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=False,session_id=5)

    def test_BookCar(self):
        print(self._testMethodName)
        booking=Book_Car.objects.get(capacity="5")
        self.assertEqual(booking.rent,100)
     
    def test_BookingCount(self):
        print(self._testMethodName)
        newUser=User.objects.create_user("robote", "robote@gmail.com", "passe")
        newUser1=User.objects.create_user("robots", "robots@gmail.com", "passs")
        Book_Car.objects.create(user=newUser,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=True,session_id=5)
        Book_Car.objects.create(user=newUser1,capacity="4",from_date="2022-03-05",to_date="2022-03-05",rent=150,subscription="platinum",is_paid=False,confirmation=False,session_id=5)
        self.assertEqual(Book_Car.objects.get(user=newUser).capacity,'5')
        self.assertEqual(Book_Car.objects.get(user=newUser1).capacity,'4')
            

    def test_BookingConfirmation(self):
        print(self._testMethodName)
        newUser=User.objects.create_user("robot1", "robot2@gmail.com", "passe")
        newUser1=User.objects.create_user("robot2", "robot3@gmail.com", "passs")
        Book_Car.objects.create(user=newUser,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=True,session_id=5)
        Book_Car.objects.create(user=newUser1,capacity="4",from_date="2022-03-05",to_date="2022-03-05",rent=150,subscription="platinum",is_paid=False,confirmation=False,session_id=5)
        self.assertEqual(Book_Car.objects.get(user=newUser).confirmation,'True')
        self.assertEqual(Book_Car.objects.get(user=newUser1).confirmation,'False')
        self.assertEqual(Book_Car.objects.get(user=newUser1).is_paid,False)
        self.assertEqual(Book_Car.objects.get(user=newUser1).subscription,"platinum")
        self.assertEqual(Book_Car.objects.get(user=newUser).subscription,'silver')    
        
class bookingTests(TestCase):
    def setUp(self):
        Cars.objects.create(car_name="audi", capacity="5",is_available="True",description="test_car",car_condition=True)
        Cars.objects.create(car_name="benz", capacity="3",is_available="True",description="test_car1",car_condition=True)
    
    def test_fareEstimator(self):
        print(self._testMethodName)
        vehicles=Cars.objects.all()
        response =self.client.post('/booking/fareestimator',{'vehciles':vehicles})
        self.assertEqual(response.status_code,200)


    def test_editBooking(self):
        newUser1=User.objects.create_user("rob2ot2", "rob2ot2@gmail.com", "passs")
        Book_Car.objects.create(user=newUser1,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=True,session_id=5)
        booking = Book_Car.objects.filter(id=newUser1.id).first()
        from_date = booking.from_date
        to_date = booking.to_date
        self.assertEqual(booking.capacity,'5')
        reponse = self.client.post('/booking/editbooking/',{'id':booking.id})
        self.assertEqual(reponse.status_code,200)

    def test_update_Booking(self):
        newUser9=User.objects.create_user("rob2ot22", "rob2ot2@gmail.com", "passs")
        Book_Car.objects.create(user=newUser9,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=True,session_id=5)
        booking = Book_Car.objects.filter(id=newUser9.id).first()
        from_date = booking.from_date
        to_date = booking.to_date
        self.assertEqual(booking.capacity,'5')
        reponse= self.client.post('/booking/updatebooking/',{"id":booking.id,"capacity":7,'from_date':from_date.strftime("%Y-%m-%d"),
            'to_date':to_date.strftime("%Y-%m-%d"),
            'from_time':from_date.strftime("%H:%M"),
            'to_time':to_date.strftime("%H:%M"),
            'subscription':booking.subscription,})
        self.assertEqual(reponse.status_code,200)

    def test_deleteBooking(self):
        newUser10=User.objects.create_user("new10", "new@gmail.com", "passs")
        booking=Book_Car.objects.create(user=newUser10,capacity="5",from_date="2022-03-05",to_date="2022-03-05",rent=100,subscription="silver",is_paid=False,confirmation=True,session_id=5)
        booking.id=newUser10.id
        reponse = self.client.post('/booking/deletebooking/',{"id":booking.id})
        self.assertEqual(reponse.status_code,302)

if __name__ == '__main__':
    unittest.main()