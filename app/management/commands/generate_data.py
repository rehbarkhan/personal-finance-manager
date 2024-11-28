from django.conf import settings
from django_seed import Seed
from app.models import Expense
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        if settings.DEBUG:
            users = User.objects.filter(is_superuser=False)
            start_date = date(2024,1,1)
            end_date = date(2024,12,31)
            for user in users:
                seeder.add_entity(
                    Expense, 100000,{
                        'date' : lambda x : seeder.faker.date_between(start_date = start_date, end_date = end_date),
                        'name': lambda x : seeder.faker.name(),
                        'User': user,
                        'sum': seeder.faker.random_int(min=1,max=120000),
                        'transaction_type': lambda x : seeder.faker.random_element(elements=['credit','debit'])
                    }
                )
                seeder.execute()
            print('date generated')
        