from django.core.management import BaseCommand

from app_base.utils import update_justification

class Command(BaseCommand):
    def handle(self, *args, **options):
        update_justification()