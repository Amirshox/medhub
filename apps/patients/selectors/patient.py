from django.http import Http404
from rest_framework.status import HTTP_404_NOT_FOUND

from patients.models import Patient


def get_patients():
    return Patient.objects.filter(is_active=True)


def get_patient_by_id(patient_id):
    try:
        return Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        raise Http404(HTTP_404_NOT_FOUND)
