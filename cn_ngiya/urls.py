"""
URL configuration for cn_ngiya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from app_centre.views import addDetailAprenant, addDetailPresence, addFormation, addpaiement, aprenant, deletePaie, detaiPresence, detailAprenant, detailFormation, formateur, formation, fpaiement, frais, home, local, log_out, login, matiere, paiement, presence, print_recu, sign_in


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('aprenant/', aprenant, name="aprenant"),
    path('matiere/', matiere, name="matiere"),
    path('formateur/', formateur, name="formateur"),
    path('formation/', formation, name="formation"),
    path('local/', local, name="local"),
    path('frais/', frais, name="frais"),
    path('paie/', paiement, name="paie"),
    path('print_recu<int:id>/',  print_recu, name="print_recu"),
    
   #User root
   path('', login, name="login"),
   path('sign_in/', sign_in, name="sign_in"),
   path('log_out/',log_out, name="log_out"),
   
   #Formulaires paie
   path('fpaiement/', fpaiement, name="fpaiement"),
   path('addpaiement/', addpaiement, name="addpaiement"),
   
   #Delete paie
   path('deletePaie<int:id>/',deletePaie, name="deletePaie"),
   path('presence/',presence, name="presence"),
   path('addDetailPresence/',addDetailPresence, name="addDetailPresence"),
   
   path('detaiPresence<int:id>/',detaiPresence, name="detaiPresence"),
   path('detailAprenant<int:id>/',detailAprenant, name="detailAprenant"),
   
   path('addDetailAprenant/',addDetailAprenant, name="addDetailAprenant"),
   
   path('detailFormation<int:id>/',detailFormation, name="detailFormation"),
   
   path('addFormation/',addFormation, name="addFormation"),
   
   
   
   
   
   
   
   
   
   
]
