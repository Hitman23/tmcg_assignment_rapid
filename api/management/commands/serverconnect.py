from django.core.management.base import BaseCommand, CommandError
from api.models import GetData, Groups

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass

    help = 'Gets the updated list of groups'

    # def get_list(self):