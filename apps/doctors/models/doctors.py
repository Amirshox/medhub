from django.db import models

from core.models import BaseModel


class Doctor(BaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    specialization = models.ForeignKey("doctors.Specialization", on_delete=models.SET_NULL, null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()
