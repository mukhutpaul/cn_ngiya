from django.core.management import BaseCommand

from app_base.models import GrandeUnite, Unite
from root.utils import findparent

class Command(BaseCommand):
    def handle(self, *args, **options):
        unites = Unite.objects.all()
        grande_unites = GrandeUnite.objects.all()
        for gu in grande_unites:
            gu.delete()
        for unite in unites:
            findparent(unite)