from django.contrib.auth.models import User
from django.test import TestCase, Client
from appointment.models import Appointment


class appointmentTestCases(TestCase):

    def test_schedule_testdrive(self):
        print(self._testMethodName)
        newUser = User.objects.create_user(username="robot", email="robot@gmail.com", password="pass")
        newUser.first_name = "machine"
        newUser.last_name = "language"
        newUser.save()

        self.client.login(username='robot', password='pass')
        data = {
            'username': "robot",
            'firstname': "machine",
            'lastname': "learning",
            'email': 'robot@gmail.com',
            'id': newUser.id,
            'appt_time': "12pm",
            'appt_date': "12/05/2022"
        }

        response = self.client.post('/schedule_appointment/', data=data)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(username="robot").last_name, "learning")
        self.assertEqual(Appointment.objects.filter(user_id=newUser.id).purpose, "appointment")

    def test_schedule_testdrive(self):
        print(self._testMethodName)
        newUser = User.objects.create_user(username="robot", email="robot@gmail.com", password="pass")
        newUser.first_name = "machine"
        newUser.last_name = "language"
        newUser.save()

        self.client.login(username='robot', password='pass')
        data = {
            'username': "robot",
            'firstname': "machine",
            'lastname': "learning",
            'email': 'robot@gmail.com',
            'id': newUser.id,
            'appt_time': "12pm",
            'appt_date': "12/05/2022"
        }

        response = self.client.post('/schedule_appointment/', data=data)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(username="robot").last_name, "learning")
        self.assertEqual(Appointment.objects.filter(user_id=newUser.id).purpose, "appointment")

    def test_schedule_testdrive_date(self):
        print(self._testMethodName)
        newUser = User.objects.create_user(username="robot", email="robot@gmail.com", password="pass")
        newUser.first_name = "machine"
        newUser.last_name = "language"
        newUser.save()

        self.client.login(username='robot', password='pass')
        data = {
            'username': "robot",
            'firstname': "machine",
            'lastname': "learning",
            'email': 'robot@gmail.com',
            'id': newUser.id,
            'appt_time': "12pm",
            'appt_date': "12/05/2022"
        }

        response = self.client.post('/schedule_testdrive/', data=data)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Appointment.objects.filter(user_id=newUser.id).appt_date, data["appt_date"])
