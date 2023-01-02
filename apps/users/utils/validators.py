from django.core.validators import ValidationError, RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)

# AA1234567
password_regex = RegexValidator(
    regex=r'^[A-Z]{2}[0-9]{7}$',
    message="Password must be entered in the format: 'AA1234567'. Up to 9 digits allowed."
)


def birth_date_validator(value):
    if value > timezone.now().date():
        raise ValidationError(
            _('%(value)s is not a valid birth date'),
            params={'value': value},
        )
