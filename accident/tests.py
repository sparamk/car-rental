import json
import unittest
import datetime
from django.test import TestCase, Client
from accident.models import * 
from django.contrib.auth.models import User

class accident_test(TestCase):
    def test_modelsTest(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        ac=Report_Accident.objects.create(report_accident="Accident done",user=newUser)
        self.assertNotEqual(ac.report_accident,"")
    
    def test_report_accident_validation(self):
        print(self._testMethodName)
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        Report_Accident.objects.create(report_accident="Accident done",user=newUser)
        accident=Report_Accident.objects.get(report_accident="Accident done")
        self.assertEqual(accident.report_accident,"Accident done")
        
    def  test_accident(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        self.client.login(username='robot', password='pass')
        Report_Accident.objects.create(report_accident="Accident done",user=newUser)
        acc=Report_Accident.objects.get(report_accident="Accident done")
        data={
            "user_id": newUser.id,
            "report_accident":"Accident done"
            }
        response=self.client.post('/accident/reportaccident/',data=data)
        self.assertEqual(response.status_code,200)
    
    def  test_Road_side_assistance(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        self.client.login(username='robot', password='pass')
        Road_Side_Assistance.objects.create(road_side_assistance="Help Need",user=newUser)
        Rs=Road_Side_Assistance.objects.get(road_side_assistance="Help Need")
        data={
            "user_id": newUser.id,
            "road_side_assistance":"Help Need"
            }
        response=self.client.post('/accident/roadsideassistance/',data=data)
        self.assertEqual(response.status_code,200)
        
    def test_Road_side_assistance_empty(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        R=Road_Side_Assistance.objects.create(road_side_assistance="Help Need",user=newUser)
        self.assertNotEqual(R.road_side_assistance,"")
    
    
    def test_Road_side_assistance_validation(self):
        print(self._testMethodName)
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        Road_Side_Assistance.objects.create(road_side_assistance="Help Need",user=newUser)
        road_assistance=Road_Side_Assistance.objects.get(road_side_assistance="Help Need")
        self.assertEqual(road_assistance.road_side_assistance,"Help Need")
    
    def  test_Vehicle_Theft_Report(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        self.client.login(username='robot', password='pass')
        Vehicle_Theft_Report.objects.create(vehicle_theft_report="Vehicle lost",user=newUser)
        VTR=Vehicle_Theft_Report.objects.get(vehicle_theft_report="Vehicle lost")
        data={
            "user_id": newUser.id,
            "vehicle_theft_report":"Vehicle lost"
            }
        response=self.client.post('/accident/vehicletheftreport/',data=data)
        self.assertEqual(response.status_code,200)
    
    def test_Vehicle_theft_report_empty(self):
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        veh=Vehicle_Theft_Report.objects.create(vehicle_theft_report="Vehicle lost",user=newUser)
        self.assertNotEqual(veh.vehicle_theft_report,"")
        
    def test_Vehicle_theft_report_validation(self):
        print(self._testMethodName)
        newUser=User.objects.create_user(username="robot",email="robot@gmail.com",password="pass")
        veh=Vehicle_Theft_Report.objects.create(vehicle_theft_report=" ",user=newUser,theft_date= "2022-08-05")
        veh.user = newUser
        veh.vehicle_theft_report="need help"
        veh.save()
        self.assertEqual(veh.vehicle_theft_report,"need help")


class Accident_methods_test(TestCase):
    
    def test_reportaccident(self):
        print(self._testMethodName)
        newUser=User.objects.create_user(username="robots",email="robots@gmail.com",password="passs") 
        self.client.login(username="robots",password="passs")       
        data={
            "user_id":newUser.id,
            "report_accident":"accident happeneds",
            "accident_date":"2022-08-05"
        }
        response=self.client.post("/accident/reportaccident/",data=data)
        self.assertEqual(response.status_code,200)

    
    
    
