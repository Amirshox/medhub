from django.db import models

from core.models import BaseModel


class Appointment(BaseModel):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE)
    symptoms = models.JSONField()
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient} - {self.doctor}"
