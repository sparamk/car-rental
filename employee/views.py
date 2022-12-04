from django.shortcuts import render
from customer.views import digitalCheckin, referFriend

# Create your views here.
def assignCar(request):
    pass
def addDiscount(request):
    pass
def deleteDiscount(request):
    pass
def sendFeedbackResponse(request):
    return render(request, 'sendfeedbackresponse.html')
def finalizeBooking(request):
    pass
def updateCarCondition(request):
    pass