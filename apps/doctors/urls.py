from rest_framework.urls import path

from doctors.views import AppointmentFormAPIView

urlpatterns = [
    path('<int:patient_id>/appointment-form/', AppointmentFormAPIView.as_view(), name='appointment-form'),
]
