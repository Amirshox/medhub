from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("passport_id", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "birth_date", "email", "gender", "phone_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("passport_id", "birth_date", "password1", "password2"),
            },
        ),
    )
    list_display = ("passport_id", "first_name", "last_name", "is_staff")
    ordering = ("passport_id",)
