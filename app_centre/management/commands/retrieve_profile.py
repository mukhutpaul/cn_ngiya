from django.core.management import BaseCommand

from app_centre.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        
        liste = ['Manager','Caissier','Administratif']
        
        for i in liste:
            p = Profile(
                name = i
            )
            p.save()