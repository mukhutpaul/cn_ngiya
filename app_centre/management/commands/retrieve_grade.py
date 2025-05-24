from django.core.management import BaseCommand

from app_base.models import Grade, Person
from app_controle.models import Controle, Justification

from root.utils import justifications

class Command(BaseCommand):
    def handle(self, *args, **options):
        personnes = Person.objects.all()
        controles = Controle.objects.all()
        
        grades = []

        for p in personnes:
            if p.grade not in grades:
                grades.append(p.grade)
        
        for p in controles:
            if p.grade not in grades:
                grades.append(p.grade)
        
        
        for u in grades:
            if u != None:
                if Grade.objects.filter(name=u).exists():
                    pass
                else:
                    grade = Grade()
                    grade.name = u
                    grade.save()
        
        for j in justifications:
            if Justification.objects.filter(name=j).exists():
                pass
            else:
                justification = Justification()
                justification.name = j
                justification.save()