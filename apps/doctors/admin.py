from django.contrib import admin

from doctors.models import Doctor, Specialization, DiseaseForm


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(DiseaseForm)
class DiseaseFormAdmin(admin.ModelAdmin):
    pass
