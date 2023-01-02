from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'passport_id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birth_date',
            'gender',
            'age',
        )

    def get_age(self, obj):
        return obj.get_age
