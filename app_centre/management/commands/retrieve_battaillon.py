from django.core.management import BaseCommand

from app_base.models import Bataillon, Person

class Command(BaseCommand):
    def handle(self, *args, **options):
        personnes = Person.objects.all()
        
        battalions = []

        for p in personnes:
            if p.battalion not in battalions:
                battalions.append(p.battalion)
        
        for u in battalions:
            battalion = Bataillon()
            battalion.name = u
            battalion.save()