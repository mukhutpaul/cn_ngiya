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

from app_centre.views import addAprenant, addDetailAprenant, addDetailFormateur, addDetailFormation, addDetailPresence, addFormateur, addFormation, addFrais, addLocal, addMatiere, addUser, addpaiement, addpresence, aprenant, deleteAprenant, deleteFormateur, deleteLocal, deleteMatiere, deletePaie, deletePresence, deleteUser, deletedetailAprenant, deletedetailFormateur, deletedetailFormation, deletedetailPresence, detaiPresence, detailAprenant, detailFormateur, detailFormation, fAprenant, fFormateur, fFormation, fFrais, fUser, flocal, fmatiere, formateur, formation, fpaiement, fpresence, frais, home, local, log_out, login, matiere, paiement, presence, print_recu, sign_in, statistiquePresence, users


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
   

   path('presence/',presence, name="presence"),
   path('addDetailPresence/',addDetailPresence, name="addDetailPresence"),
   
   path('detaiPresence<int:id>/',detaiPresence, name="detaiPresence"),
   path('detailAprenant<int:id>/',detailAprenant, name="detailAprenant"),
   
   path('addDetailAprenant/',addDetailAprenant, name="addDetailAprenant"),
   
   path('detailFormation<int:id>/',detailFormation, name="detailFormation"),
   
   path('addFormation/',addFormation, name="addFormation"),
   
   ##Formulaires Matières
   path('fmatiere/',fmatiere, name="fmatiere"),
   path('addMatiere/',addMatiere, name="addMatiere"),
   
   ##Formulaires Aprenant
   path('fAprenant/',fAprenant, name="fAprenant"),
   path('addAprenant/',addAprenant, name="addAprenant"),
   
   
   ##Formulaires Présence
   path('fpresence/',fpresence, name="fpresence"),
   path('addpresence/',addpresence, name="addpresence"),
   
   ##FLOCAL
   path('flocal/',flocal, name="flocal"),
   path('addLocal/',addLocal, name="addLocal"),
   
   ##FFORMATION
   path('fFormation/',fFormation, name="fFormation"),
   path('addFormation/',addFormation, name="addFormation"),
   
   ##FFRAIS
   path('fFrais/',fFrais, name="fFrais"),
   path('addFrais/',addFrais, name="addFrais"),
   
   ##FFormateur
   path('fFormateur/',fFormateur, name="fFormateur"),
   path('addFormateur/',addFormateur, name="addFormateur"),
   
   ##DETAIL FORMATEUR
   path('detailFormateur<int:id>/',detailFormateur, name="detailFormateur"),
   path('addDetailFormateur/',addDetailFormateur, name="addDetailFormateur"),
   path('addDetailFormation/',addDetailFormation, name="addDetailFormation"),
   
   
   
   ##USERS
   path('users/',users, name="users"),
   path('fUser/',fUser, name="fUser"),
   path('addUser/',addUser, name="addUser"),
   
   ##STATISTIQUES PRESENCES
   path('statistiquePresence<int:id>/',statistiquePresence, name="statistiquePresence"),
   
   ##SUPPRESSION
   #Delete paie
   path('deletePaie<int:id>/',deletePaie, name="deletePaie"),
   #Delete Aprenant
   path('deleteAprenant<int:id>/',deleteAprenant, name="deleteAprenant"),
   
   #Delete Matière
   path('deleteMatiere<int:id>/',deleteMatiere, name="deleteMatiere"),
   #Delete Formateur
   path('deleteFormateur<int:id>/',deleteFormateur, name="deleteFormateur"),
   
   #Delete Présence
   path('deletePresence<int:id>/',deletePresence, name="deletePresence"),
   #Delete Local
   path('deleteLocal<int:id>/',deleteLocal, name="deleteLocal"),
   
   #Delete users
   path('deleteUser<int:id>/',deleteUser, name="deleteUser"),
   
   path('deletedetailFormation<int:id>/',deletedetailFormation, name="deletedetailFormation"),
   path('deletedetailPresence<int:id>/',deletedetailPresence, name="deletedetailPresence"),
   path('deletedetailFormateur<int:id>/',deletedetailFormateur, name="deletedetailFormateur"),
   
   path('deletedetailAprenant<int:id>/',deletedetailAprenant, name="deletedetailAprenant"),
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
]
