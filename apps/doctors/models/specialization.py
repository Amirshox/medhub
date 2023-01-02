from django.db import models

from core.models import BaseModel


class Specialization(BaseModel):
    CARDIOLOGIST = "cardiologist"
    DENTIST = "dentist"
    DERMATOLOGIST = "dermatologist"
    THERAPIST = "therapist"
    SPECIALIZATION_CHOICES = (
        (CARDIOLOGIST, "Cardiologist"),
        (DENTIST, "Dentist"),
        (DERMATOLOGIST, "Dermatologist"),
        (THERAPIST, "Therapist"),
    )

    forms = models.ManyToManyField("doctors.DiseaseForm", blank=True)
    name = models.CharField(max_length=31, choices=SPECIALIZATION_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
