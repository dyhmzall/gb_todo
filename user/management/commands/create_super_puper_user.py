import json

from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = 'Генерация супер-пупер пользователя'

    def handle(self, *args, **options):
        with open(r"user/super_puper_user.json") as f:
            users = json.load(f)

            if not users:
                print("Ошибка загрузки супер-пупер-пользователей!")

            for user_number, user in enumerate(users):
                admin = User()
                admin.username = user.get("username", f"username{user_number}")
                admin.first_name = user.get("first_name", "first_name")
                admin.last_name = user.get("last_name", "last_name")
                admin.email = user.get("email", f"email@email{user_number}.com")
                admin.is_superuser = 1
                admin.is_staff = 1
                admin.is_active = 1
                admin.set_password(user.get("password", "test"))

                admin.save()
