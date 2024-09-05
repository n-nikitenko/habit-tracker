from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "tg_chat_id")
        optional_fields = ("email", "tg_chat_id")
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
        }
