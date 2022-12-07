from django.urls import path, include
from . import views

urlpatterns = [
    path("reportaccident/", views.reportAccident, name='reportaccident'),
    path("viewaccidentreports/", views.viewAccidentReports, name='viewaccidentreports'),
    path("roadsideassistance/", views.roadSideAssistance, name='roadsideassistance'),
    path("viewroadsideassistance/", views.viewRoadSideAssistance, name='viewroadsideassistance'),
    path("vehicletheftreport/", views.vehicleTheftReport, name='vehicletheftreport'),
    path("viewvehicletheftreport/", views.viewVehicleTheftReport, name='viewvehicletheftreport'),
]