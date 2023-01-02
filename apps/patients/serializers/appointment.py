from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from patients.models import Appointment
from patients.utils import validate_required_symptoms
from patients.selectors import get_patient_by_id
from doctors.services import get_disease_form_required_fields


class AppointmentSerializer(ModelSerializer):
    doctor = serializers.SlugField(source='doctor.user.get_full_name', read_only=True)

    class Meta:
        model = Appointment
        exclude = ('created_at', 'updated_at', 'is_active')
        extra_kwargs = {
            'doctor': {'read_only': True},
            'patient': {'write_only': True},
        }

    def validate_symptoms(self, value):
        patient_id = self.initial_data.get('patient')
        doctor = self.context['request'].user.doctor
        patient = get_patient_by_id(patient_id)
        fields = get_disease_form_required_fields(doctor, patient)
        if fields is None:
            raise ValidationError('Disease form is not found for your age')
        for field in fields:
            if field not in value:
                raise ValidationError(f'{field} is required.')
        validate_required_symptoms(value)
        return value

    def to_representation(self, instance):
        self.fields['parent'] = self.__class__(context=self.context)
        return super(AppointmentSerializer, self).to_representation(instance)
