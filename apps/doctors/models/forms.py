from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel


class DiseaseForm(BaseModel):
    number = models.CharField(max_length=100)
    questions = models.JSONField()
    required_question_fields = ArrayField(models.CharField(max_length=100), default=list)
    from_age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0)
    ])
    to_age = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(150)
    ])

    def __str__(self):
        return str(self.number)
