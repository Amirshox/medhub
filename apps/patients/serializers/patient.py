from rest_framework import serializers

from patients.models import Patient
from patients.selectors import appointment_temperature_avg_by_patient, appointment_pressure_avg_by_patient
from users.serializers import UserSerializer


class PatientSerializer(serializers.ModelSerializer):
    temperature_avg = serializers.SerializerMethodField(read_only=True)
    pressure_avg = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        exclude = ('created_at', 'updated_at', 'is_active')

    def get_temperature_avg(self, obj):
        return appointment_temperature_avg_by_patient(obj)

    def get_pressure_avg(self, obj):
        return appointment_pressure_avg_by_patient(obj)
