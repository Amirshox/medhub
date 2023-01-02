from django.utils import timezone
from rest_framework.serializers import ValidationError


def validate_required_symptoms(data):
    if data.get('temperature') is not None:
        validate_temperature(data['temperature'])
    if data.get('pressure') is not None:
        validate_pressure(data['pressure'])
    if data.get('pulse') is not None:
        validate_pulse(data['pulse'])
    if data.get('last_activity') is not None:
        validate_last_activity(data['last_activity'])


def validate_temperature(value):
    if isinstance(value, int) or isinstance(value, float):
        if value < 35 or value > 42:
            raise ValidationError('Temperature must be between 35 and 42 degrees.')
    else:
        raise ValidationError('Temperature must be a number.')


def validate_pressure(value):
    if isinstance(value, int) or isinstance(value, float):
        if value < 100 or value > 200:
            raise ValidationError('Pressure must be between 100 and 200 mmHg.')
    else:
        raise ValidationError('Pressure must be a number.')


def validate_pulse(value):
    if isinstance(value, int) or isinstance(value, float):
        if value < 40 or value > 180:
            raise ValidationError('Pulse must be between 40 and 180 bpm.')
    else:
        raise ValidationError('Pulse must be a number.')


def validate_last_activity(value):
    try:
        value = timezone.datetime.strptime(value, '%Y-%m-%d')
        if value.timestamp() > timezone.now().timestamp():
            raise ValidationError('Last activity must be in the past.')
    except ValueError:
        raise ValidationError('Last activity must be a date in the format YYYY-MM-DD.')
