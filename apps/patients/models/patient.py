from django.db import models

from core.models import BaseModel


class Patient(BaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()
