from django.core.management import BaseCommand

from app_base.utils import updateProvince


class Command(BaseCommand):
    def handle(self, *args, **options):
        updateProvince()