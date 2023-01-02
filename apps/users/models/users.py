from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from users.managers import UserManager
from users.utils import phone_regex, password_regex, birth_date_validator


class User(AbstractUser):
    MALE = "m"
    FEMALE = "f"

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    username = None

    passport_id = models.CharField(max_length=9, unique=True, validators=[password_regex])
    phone_number = models.CharField(max_length=12, validators=[phone_regex])
    birth_date = models.DateField(validators=[birth_date_validator])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    objects = UserManager()

    USERNAME_FIELD = "passport_id"
    REQUIRED_FIELDS = ['phone_number', 'birth_date']

    @property
    def is_adult(self):
        return timezone.now().year - self.birth_date.year >= 18

    @property
    def is_older(self):
        return timezone.now().year - self.birth_date.year >= 30

    @property
    def get_age(self):
        return timezone.now().year - self.birth_date.year
