import json
import unittest

from django.test import TestCase, Client

from owner.models import Cars, Coupons

from django.contrib.auth.models import User, Group

class owner_Car_TestCase(TestCase):
    def setUp(self):
        Cars.objects.create(car_name="audi", capacity="5",is_available="True",description="test_car",car_condition=True)
        Cars.objects.create(car_name="benz", capacity="3",is_available="True",description="test_car1",car_condition=True)
    
    def test_ownerCarDescription(self):
        print(self._testMethodName)
        car=Cars.objects.get(car_name="audi")
        self.assertEqual(car.description,"test_car")
        
    def test_ownerCarCapacity(self):
        print(self._testMethodName)
        car=Cars.objects.get(car_name="audi")
        self.assertEqual(car.capacity,"5")
         
    def test_ownerCarConition(self):
        print(self._testMethodName)
        car=Cars.objects.get(car_name="audi")
        self.assertEqual(car.car_condition,True)  
        
    def test_compare_car_names(self):
        print(self._testMethodName)
        car1=Cars.objects.get(car_name="audi")
        car2=Cars.objects.get(car_name="benz")
        self.assertNotEqual(car1.car_name,car2.car_name)        

class owner_Coupon_TestCase(TestCase):
    def setUp(self):
        Coupons.objects.create(coupon_code="NEW15",discount="15")
        Coupons.objects.create(coupon_code="OLD20",discount="20")

    def test_coupon_creation(self):
        print(self._testMethodName)
        coupon=Coupons.objects.get(coupon_code="NEW15")
        self.assertEqual(coupon.discount,"15")
    
    def test_coupon_discount_valid(self):
        print(self._testMethodName)
        coupon=Coupons.objects.get(coupon_code="NEW15")
        self.assertTrue(coupon.discount!='')
    
    def test_coupon_empty(self):
        print(self._testMethodName)
        coupon=Coupons.objects.get(coupon_code="OLD20")
        self.assertTrue(coupon.coupon_code!='')
        
class Car_methods(unittest.TestCase):
    def setUp(self):
        self.client = Client()


    def test_AddCar(self):
        print(self._testMethodName)
        newUser=User.objects.create_user("robot", "robot@gmail.com", "pass")
        self.client.login(username="robot",password="pass")
        data = {
            "car_name": "Marutii",
            "color": "White",
            "capacity": 5,
            "cost_of_vehicle":50,
            "rent_per_hour":20,
            "description": "Thevintage indian car",
            "car_condition":1,
            "subscription":3
        }
        response = self.client.post('/owner/addcar/', data=data)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        
        
    def test_updateCar(self):
        print(self._testMethodName)
        Cars.objects.create(car_name="benz_old", capacity="3",is_available="True",description="test_car3",car_condition=True)
        car_edit_id = Cars.objects.get(car_name="benz_old").id
        data = {
            "car_id": car_edit_id,
            "car_name": "benz_old",
            "color": "White",
            "capacity": 3,
            "description": "edit_car_change",
            "car_condition":1,
            "subscription":1

        }
        response = self.client.post('/owner/updatecar/',data=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(Cars.objects.get(id=car_edit_id).description,"edit_car_change")
        
    def test_listCars(self):
        print(self._testMethodName)
        Cars.objects.create(car_name="alto", capacity="5",is_available="True",description="test_car",car_condition=True)
        Cars.objects.create(car_name="i10", capacity="3",is_available="True",description="test_car1",car_condition=True)
        cars=Cars.objects.all
        self.assertGreater(Cars.objects.count(),1)
        
    def test_deleteCars(self):
        print(self._testMethodName)
        Cars.objects.create(car_name="nano", capacity="4",is_available="True",description="test_car",car_condition=True)
        count=Cars.objects.count()
        car_delete_id = Cars.objects.get(car_name="nano").id
        data = {
            "id":car_delete_id,
            "car_name" : "nano",
            "capacity":"4",
            "is_available":"True",
            "description=":"test_car",
            "car_condition":True
            
        }
        response = self.client.post('/owner/deletecar/', data=data)
        self.assertEqual(count,Cars.objects.count()+1)
                    
    def test_addCoupon(self):
        print(self._testMethodName)
        Coupons.objects.create(coupon_code="TEST30",discount="30")
        data = {
            "coupon_code":"TEST300",
            "discount":"30"
        }
        response=self.client.post('/owner/addcoupon/',data=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(Coupons.objects.get(coupon_code="TEST300").discount,"30")
      
        
    def test_updateCoupon(self):
        print(self._testMethodName)
        Coupons.objects.create(coupon_code="COLA",discount="23")
        coupon_edit_id = Coupons.objects.get(coupon_code="COLA").id
        data = {
            "coupon_id":coupon_edit_id,
            "coupon_code":"COLA",
            "discount":"25"
        }
        response = self.client.post('/owner/updatecoupon/',data=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(Coupons.objects.get(id=coupon_edit_id).discount,"25")
            
    def test_deleteCoupon(self):
        print(self._testMethodName)
        Coupons.objects.create(coupon_code="PEPSI",discount="78")
        count=Coupons.objects.count()
        coupon_delete_id = Coupons.objects.get(coupon_code="PEPSI").id
        data = {
            "id":coupon_delete_id,
            "coupon_code":"PEPSI",
            "discount":"78"
        }
        response = self.client.post('/owner/deletecoupon/', data=data)
        self.assertEqual(count,Coupons.objects.count()+1)            
            
if __name__ == '__main__':
    unittest.main()