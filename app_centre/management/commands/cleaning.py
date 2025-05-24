from django.core.management import BaseCommand

from root.utils import cleaning


class Command(BaseCommand):
    def handle(self, *args, **options):
        cleaning()