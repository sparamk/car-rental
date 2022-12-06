from django.contrib import messages
from django.shortcuts import render
from customer.views import digitalCheckin, referFriend
from feedback.models import Feedback
from car.models import *
from customer.models import *
from booking.models import *
# Create your views here.
def assignCar(request):
    pass

def addDiscount(request):
    pass

def deleteDiscount(request):
    pass

def sfr(request):
    feedback = Feedback.objects.all()
    return render(request, 'sendfeedbackresponse.html', {'feedback':feedback})

def usfr(request):
    if request.method == 'POST':
        feedback = Feedback.objects.filter(id=request.POST['id']).update(feedback_text_response=request.POST['feedback_text_response'])
        success = 'Feedback response posted'
        feedback = Feedback.objects.all()
        return render(request, 'sendfeedbackresponse.html', {'feedback':feedback,'success':success})
    feedback = Feedback.objects.all()
    return render(request, 'sendfeedbackresponse.html', {'feedback':feedback})

def finalizeBooking(request):
    if request.method == 'POST':
        car_id = request.POST['id']
        booking_id = request.POST['booking_id']
        car = Cars.objects.filter(id=car_id).first()
        booking = Book_Car.objects.filter(id=booking_id).first()
        book = Book()
        book.from_date = booking.from_date
        book.to_date = booking.to_date
        book.book_car_id = booking.id
        book.car_id = car_id
        book.user_id = booking.user_id
        book.confirmation = True
        book.save()
        messages.success(request,"Your booking is success")
    return render(request, 'finalbooking.html')

def updateCarCondition(request):
    pass
