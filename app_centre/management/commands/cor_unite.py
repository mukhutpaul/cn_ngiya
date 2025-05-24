from django.core.management import BaseCommand

from app_base.utils import cor_unite

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        cor_unite()