from django.shortcuts import render
from . models import *
# Create your views here.

def reportAccident(request):
    if request.method == 'POST':
        reportaccident = Report_Accident()
        reportaccident.user_id = request.user.id
        reportaccident.report_accident = request.POST['report_accident']
        reportaccident.save()
        success = 'The accident report has been sent successfully'
        return render(request, 'reportaccident.html',{'success':success})
    
    return render(request, 'reportaccident.html')

def viewAccidentReports(request):
    accident = Report_Accident.objects.all()
    return render(request, 'viewaccidentreports.html',{'accident':accident})
    
def roadSideAssistance(request):
    if request.method == 'POST':
        assistance = Road_Side_Assistance()
        assistance.user_id = request.user.id
        assistance.road_side_assistance = request.POST['road_side_assistance']
        assistance.save()
        success = 'The accident report has been sent successfully'
        return render(request, 'roadsideassistance.html',{'success':success})
    return render(request, 'roadsideassistance.html')

def viewRoadSideAssistance(request):
    assistance = Road_Side_Assistance.objects.all()
    return render(request, 'viewroadsideassistance.html',{'assistance':assistance})


def vehicleTheftReport(request):
    if request.method == 'POST':
        theft = Vehicle_Theft_Report()
        theft.user = request.user
        theft.vehicle_theft_report = request.POST['vehicle_theft_report']
        theft.save()
        success = 'The vehicle theft report has been sent successfully'
        return render(request, 'vehicletheftreport.html',{'success':success})
    return render(request, 'vehicletheftreport.html')

def viewVehicleTheftReport(request):
    theft = Vehicle_Theft_Report.objects.all()
    return render(request, 'viewvehicletheftreport.html',{'theft':theft})
