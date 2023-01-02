def get_disease_form(doctor, patient):
    patient_age = patient.user.get_age
    form = doctor.specialization.forms.filter(
        is_active=True,
        from_age__lte=patient_age,
        to_age__gte=patient_age
    ).first()
    return form


def get_disease_form_questions(doctor, patient):
    form = get_disease_form(doctor, patient)
    if form:
        return form.questions
    return None


def get_disease_form_required_fields(doctor, patient):
    form = get_disease_form(doctor, patient)
    if form:
        return form.required_question_fields
    return None
