from django.contrib import admin

# Register your models here.
from django.db import models

from app_centre.models import AffectationFormation, Aprenant, DetailPresence, Formation, Matiere,Formateur,Local, Presence, Profile,SessionFormation,Frais,Paiement, User

# Create your models here.

admin.site.register(Aprenant)
admin.site.register(Matiere)
admin.site.register(Formateur)
admin.site.register(Formation)
admin.site.register(Local)
admin.site.register(SessionFormation)
admin.site.register(AffectationFormation)
admin.site.register(Frais)
admin.site.register(Paiement)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Presence)
admin.site.register(DetailPresence)



  
    

    
    
        