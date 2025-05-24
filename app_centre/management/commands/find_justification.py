from django.core.management import BaseCommand

from app_controle.models import Justification

from root.utils import justifications

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        for j in justifications:
            if Justification.objects.filter(name=j).exists():
                pass
            else:
                justification = Justification()
                justification.name = j
                justification.save()
        print("Les justifications")
        for j in Justification.objects.all():
            print(j.name)
