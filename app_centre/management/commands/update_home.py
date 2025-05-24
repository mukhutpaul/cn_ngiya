from django.core.management import BaseCommand

from root.utils import cleaning, update_home


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_home(None)
        cleaning()