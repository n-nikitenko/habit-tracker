from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "last_login",
        "date_joined",
        "tg_chat_id",
    )
