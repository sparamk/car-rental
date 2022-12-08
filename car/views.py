import json
from django.shortcuts import render
from appointment.views import *
from sales.views import *
from booking.views import *
from user.views import *
from .models import *
from booking.models import *
from django.http import HttpResponse
# Create your views here.
def checkCarAvlb(request):
    if request.method == 'POST':
        booking_id = request.POST['id']
        booking = Book_Car.objects.filter(id=booking_id).first()
        # return HttpResponse(vars(booking))
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        rent = request.POST['rent']
        capacity = request.POST['capacity']
        subscription = request.POST['subscription']
        cars = Cars.objects.filter(capacity=capacity, subscription=subscription)
        cars_list = []
        for car in cars:
            book_id = Book.objects.filter(car_id=car.id)
            car_dictionary = {'id': car.id, 'capacity': car.capacity, 'subscription': car.subscription, 'car_name': car.car_name, 'cost_of_vehicle': car.cost_of_vehicle, 'from_date':from_date, 'to_date':to_date, 'description':car.description, 'color':car.color, 'rent':rent, 'booking_id':booking_id}
            cars_list.append(car_dictionary)
            # elif book_id.from_date <= request.POST['from_date'] <= book_id.to_date:
            #     car_dictionary = {'id': car.id, 'capacity': car.capacity, 'subscription': car.subscription, 'car_name': car.car_name, 'cost_of_vehicle': car.cost_of_vehicle, 'from_date':from_date, 'to_date':to_date, 'description':car.description, 'color':car.color, 'rent':rent,'booking_id':booking_id}
            #     cars_list.append(car_dictionary)
            
            return render(request, 'checkcaravlb.html', {'cars':cars_list})
    error = "No cars available"
    return render(request, 'checkcaravlb.html',{'error':error})


