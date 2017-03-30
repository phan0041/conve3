__author__ = 'hungfly'

from django.core.management.base import BaseCommand, CommandError
from LandingPage import gSheet_services


class Command(BaseCommand):
    help = 'update data'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        gSheet_services.update_data()
        self.stdout.write('Data updated')
