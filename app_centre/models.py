from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.core.exceptions import ValidationError


# Create your models here.
class Aprenant(models.Model):
    nom = models.CharField(max_length=100,null=False)
    postnom = models.CharField(max_length=100,null=False)
    prenom = models.CharField(max_length=100, null = False)
    lieunaissance = models.CharField(max_length=100)
    datenaissance = models.CharField(max_length=20)
    sexe = models.CharField(max_length=2,null=False)
    Etatcivil = models.CharField(max_length=30)
    niveauEtude = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    langue = models.CharField(max_length=50)
    adresse = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom+" "+self.postnom+" "+self.prenom
    
class Matiere(models.Model):
    designation = models.CharField(max_length=100)
    nombreHeure = models.IntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designation
    
class Formateur(models.Model):
    nom = models.CharField(max_length=100,null=False)
    postnom = models.CharField(max_length=100,null=False)
    prenom = models.CharField(max_length=100, null = False)
    sexe = models.CharField(max_length=2,null=False)
    Etatcivil = models.CharField(max_length=30)
    niveauEtude = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    langue = models.CharField(max_length=50)
    adresse = models.CharField(max_length=255)
    matieres = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom+" "+self.postnom+" "+self.prenom
    
class Formation(models.Model):
    designaion = models.CharField(max_length=255,null=False)
    duree = models.CharField(max_length=30)
    Formateurs = models.CharField(max_length=255,null=False)
    matieres = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designaion
    
class Local(models.Model):
    designation = models.CharField(max_length=100,null=False)
    capacité = models.IntegerField()
    createdat = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designation
    
class SessionFormation(models.Model):
    designation = models.CharField(max_length=100,null=False)
    dateDebut = models.CharField(max_length=20,null=False)
    dateFin = models.CharField(max_length=20,null=False)
    local = models.ForeignKey(Local, on_delete=models.DO_NOTHING)
    createdat = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designation,"-",self.dateDebut,"-",self.dateFin
    
class AffectationFormation(models.Model):
    sponsoriser = models.BooleanField(default=False)
    aprenant = models.ForeignKey(Aprenant,on_delete=models.DO_NOTHING)
    session = models.ForeignKey(SessionFormation,on_delete=models.DO_NOTHING)
    formation = models.ForeignKey(Formation, on_delete=models.DO_NOTHING)
    createdat = models.DateTimeField(auto_now=True)
    
    def __def__(self):
        return self.aprenant.nom

class Frais(models.Model):
    codeFrais = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    cout = models.IntegerField()
    createdat = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.codeFrais+" "+self.designation

class Paiement(models.Model):
    aprenant = models.ForeignKey(Aprenant,on_delete=models.DO_NOTHING)
    frais = models.ForeignKey(Frais,on_delete=models.DO_NOTHING)
    montant = models.IntegerField()
    createdat = models.DateTimeField(auto_now=True)
    
    def __int__(self):
        
        return self.id
    
class Presence(models.Model):
    aprenant = models.ForeignKey(Aprenant,on_delete=models.DO_NOTHING)
    present = models.BooleanField(default=False)
    matieres = models.CharField(models.CharField)
    createdat = models.DateTimeField(auto_now=True)
    
    def __init__(self):
        return self.aprenant,"-", self.matieres
    

#UTILISATEURS

class Profile(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True,null=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    noms = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True, null=True)
    #photo_url = models.ImageField(upload_to='photos/', blank=True, null=True)

    REQUIRED_FIELDS = []

class LogUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_synchronize = models.BooleanField(default=False)

    def __str__(self):
        name = self.user.username or ""
        return name
    
