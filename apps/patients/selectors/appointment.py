from django.db.models import FloatField, Avg
from django.db.models.fields.json import KeyTransform
from django.db.models.functions import Cast

from patients.models import Appointment
from patients.models import Patient


def appointment_temperature_avg_by_patient(patient: Patient) -> float:
    return Appointment.objects.filter(patient=patient).annotate(
        temperature=Cast(KeyTransform('temperature', 'symptoms'), FloatField())
    ).values('temperature').aggregate(Avg('temperature'))['temperature__avg']


def appointment_pressure_avg_by_patient(patient: Patient) -> float:
    return Appointment.objects.filter(patient=patient).annotate(
        pressure=Cast(KeyTransform('pressure', 'symptoms'), FloatField())
    ).values('pressure').aggregate(Avg('pressure'))['pressure__avg']


def get_appointments_by_patient_id(patient_id: int):
    return Appointment.objects.filter(patient_id=patient_id)
