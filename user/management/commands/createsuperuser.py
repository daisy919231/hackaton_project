# app1/management/commands/createsuperuser.py

from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.db import transaction
from django.contrib.auth.models import User

class Command(createsuperuser.Command):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--noinput',
            action='store_true',
            dest='noinput',
            default=False,
            help='Do not prompt for input.'
        )

    @transaction.atomic
    def handle(self, *args, **options):
        # Override to use default fields like username, email, etc.
        user_data = {
            'username':None,
            'email': None,
            'password': None,
        }

        if not options.get('noinput'):
            # Prompt for fields like username, email, etc. (default Django behavior)
            user_data['username']=input('Username:')
            user_data['email'] = input("Email: ")
            user_data['password'] = input("Password: ")
    
        
        user = User.objects.create_superuser(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            
        )
        
        self.stdout.write(self.style.SUCCESS(f"Superuser {user.username} created successfully."))
