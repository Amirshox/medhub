from rest_framework.views import APIView
from rest_framework.response import Response

from doctors.services import get_disease_form_questions
from patients.selectors import get_patient_by_id


class AppointmentFormAPIView(APIView):

    def get(self, request, *args, **kwargs):
        patient_id = self.kwargs.get("patient_id")
        patient = get_patient_by_id(patient_id)
        questions = get_disease_form_questions(request.user.doctor, patient)
        if questions:
            return Response(questions)
        return Response({"message": "There is no form for your age."})
