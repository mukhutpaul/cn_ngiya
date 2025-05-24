from django.core.management import BaseCommand

from app_base.utils import saveProvince

class Command(BaseCommand):
    def handle(self, *args, **options):
        saveProvince()