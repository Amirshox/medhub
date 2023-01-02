from rest_framework.views import APIView
from rest_framework.response import Response
from patients.selectors import get_patients, get_patient_by_id
from patients.serializers import PatientSerializer


class PatientListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = PatientSerializer(get_patients(), many=True)
        return Response(serializer.data)


class PatientDetailAPIView(APIView):
    def get(self, request, pk=None):
        serializer = PatientSerializer(get_patient_by_id(pk))
        return Response(serializer.data)
