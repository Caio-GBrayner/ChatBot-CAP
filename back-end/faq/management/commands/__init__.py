# createsimpleuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser without email'

    def handle(self, *args, **options):
        username = input('Username: ')
        password = input('Password: ')

        User.objects.create_superuser(
            username=username,
            password=password,
            user_type='AD'
        )
        self.stdout.write(self.style.SUCCESS('Superuser criado com sucesso!'))