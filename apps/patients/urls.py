from rest_framework.urls import path

from patients.views import AppointmentAPIView, AppointmentsByPatientAPIView, PatientListAPIView
from patients.views import PatientDetailAPIView

urlpatterns = [
    path('appointments/', AppointmentAPIView.as_view()),
    path('<int:pk>/appointments/', AppointmentsByPatientAPIView.as_view()),
    path('<int:pk>/', PatientDetailAPIView.as_view()),
    path('', PatientListAPIView.as_view()),
]
