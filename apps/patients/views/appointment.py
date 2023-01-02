from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.selectors import get_appointments_by_patient_id
from patients.serializers import AppointmentSerializer


class AppointmentAPIView(GenericAPIView):
    serializer_class = AppointmentSerializer

    def post(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.save()
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user.doctor)


class AppointmentsByPatientAPIView(APIView):

    def get(self, request, pk=None):
        serializer = AppointmentSerializer(get_appointments_by_patient_id(pk), many=True)
        return Response(serializer.data)
