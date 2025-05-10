import json
from datetime import datetime
from django.http import HttpResponseRedirect
from time import time
from django.shortcuts import render, redirect
import qrcode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login, logout

from app_centre.models import Aprenant, Formateur, Formation, Frais, Local, Matiere, Paiement, User
from django.core.paginator import Paginator

from app_centre.utils import render_to_pdf
from qrcode import *

from cn_ngiya import settings

# Create your views here.
@login_required(login_url="sign_in")
def home(request):
    print(request.user)
    
    ctx ={
        'hm': 'active'
    }
    
    return render(request,'page/home.html',ctx)

@login_required(login_url="sign_in")
def aprenant(request):
    apreants = len(Aprenant.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Aprenant.objects.filter(nom__contains=rech) |
        Aprenant.objects.filter(postnom__contains=rech) |
        Aprenant.objects.filter(prenom__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Aprenant.objects.all())  
        
    else:
        p = Paginator(Aprenant.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Aprenant.objects.all())
    ctx = {
        'compte' : compte,
        'apr' : pages,
        'lapr': 'active',
        'pages':pages
    }
    return render(request,'page/aprenant.html',ctx)

@login_required(login_url="sign_in")
def matiere(request):
    apreants = len(Matiere.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Matiere.objects.filter(designation__contains=rech) |
        Matiere.objects.filter(nombreHeure__contains=rech) )
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Matiere.objects.all())  
        
    else:
        p = Paginator(Matiere.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Matiere.objects.all())
    ctx = {
        'compte' : compte,
        'mtr' : pages,
        'lmtr': 'active',
        'pages':pages
    }
    return render(request,'page/matiere.html',ctx)

@login_required(login_url="sign_in")
def formateur(request):
    apreants = len(Formateur.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Formateur.objects.filter(nom__contains=rech) |
        Formateur.objects.filter(postnom__contains=rech) |
        Formateur.objects.filter(prenom__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Formateur.objects.all())  
        
    else:
        p = Paginator(Formateur.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Formateur.objects.all())
    ctx = {
        'compte' : compte,
        'fmr' : pages,
        'lfmr': 'active',
        'pages':pages
    }
    return render(request,'page/formateur.html',ctx)

@login_required(login_url="sign_in")
def formation(request):
    formations = len(Formation.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Formation.objects.filter(designation__contains=rech) |
        Formateur.objects.filter(deree__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Formation.objects.all())  
        
    else:
        p = Paginator(Formation.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Formation.objects.all())
    ctx = {
        'compte' : compte,
        'fmt' : pages,
        'lfmt': 'active',
        'pages':pages
    }
    return render(request,'page/formation.html',ctx)

@login_required(login_url="sign_in")
def local(request):
    locaux = len(Local.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Local.objects.filter(designation__contains=rech) |
        Local.objects.filter(capacite__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Local.objects.all())  
        
    else:
        p = Paginator(Local.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Local.objects.all())
    ctx = {
        'compte' : compte,
        'local' : pages,
        'lloc': 'active',
        'pages':pages
    }
    return render(request,'page/local.html',ctx)

@login_required(login_url="sign_in")
def frais(request):
    locaux = len(Frais.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Frais.objects.filter(designation__contains=rech) |
        Frais.objects.filter(cout__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Frais.objects.all())  
        
    else:
        p = Paginator(Frais.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Frais.objects.all())
    ctx = {
        'compte' : compte,
        'frais' : pages,
        'lfrais': 'active',
        'pages':pages
    }
    return render(request,'page/frais.html',ctx)

@login_required(login_url="sign_in")
def paiement(request):
    solde = 0
    data =[]
    reste = 0
    locaux = len(Paiement.objects.all())
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Paiement.objects.filter(aprenant_nom__contains=rech) |
        Paiement.objects.filter(aprenant_postnom__contains=rech) | 
        Paiement.objects.filter(frais_designation__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Paiement.objects.all())  
        
    else:
        p = Paginator(Paiement.objects.all().order_by('-id'), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Paiement.objects.all())
    for d in pages:
        fr = Frais.objects.filter(id=d.frais.id)
        for f in fr:
           
            if d.montant == f.cout:
                solde = "oui"
            else :
                solde = "non"
            reste = f.cout - d.montant
        data.append(
            {
                'id':d.id,
                'frais':d.frais,
                'aprenant': d.aprenant,
                'createdAt': d.createdat,
                'montant': d.montant,
                'solde': solde,
                'reste': reste
            }
        )
        for d in data:
            print(d)
            
    ctx = {
        'compte' : len(data),
        'paie' : data,
        'lpaie': 'active',
        'pages':pages
    }
    return render(request,'page/paiement.html',ctx)

# RAPPORT OU LISTES

@login_required(login_url="sign_in")
def print_recu(request,id):
    id_user = request.user.id
    user = User.objects.get(pk=id_user)
    etat = None
    data=[]
    paie = Paiement.objects.get(pk=id)
    paies = Paiement.objects.filter(aprenant=paie.aprenant,frais=paie.frais)
    somme=0
    for p in paies:
        somme += p.montant
    print("MUKHUT",somme)
       
    fr = Frais.objects.get(pk=paie.frais.id)
    print(fr.cout)
    if somme == fr.cout:
        etat = "Solde"
    else :
        etat ="Acompte"
    
    data = {
        'N° paiement': paie.id,
        'N° Aprenant': paie.aprenant.id,
        'Aprenant': paie.aprenant,
        'Motif': etat +" "+str(paie.frais),
        'Montant payé': paie.montant,
        'Date Paie': paie.createdat,
        'Caissier': paie.createdat,
    }
    
    
    img = qrcode.make(data)
    img_name = 'Recu' + str(time())+'.png'
    img.save("mediafiles/recu/" + img_name)
    ctx = {
        'img': img_name,
        "paie": paie,
        "etat": etat,
        "noms": request.user.noms
    }   
    pdf = render_to_pdf("report/recu.html", ctx, 200)
    return pdf


# USER AUTHENTIFICATION


def login(request):
    
    
    return render(request,'user/login.html')

def sign_in(request):
    msg = None
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        user = User.objects.filter(username=username).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                auth_login(request, auth_user)
                return redirect("home")
            else:
                msg ="mot de pass incorrecte"
        else:
            msg ="User does not exist"
    
    ctx = {
        "msg":msg
    }

    return render(request,'user/login.html',ctx)

def log_out(request):
    logout(request)
    return redirect("sign_in")


#Formulaires
@login_required(login_url="sign_in")
def fpaiement(request):
    frs = Frais.objects.all()
    apr = Aprenant.objects.all()
    
    ctx = {
        'frs': frs,
        'apr': apr
    }
    
    return render(request,'formulaire/FPaiement.html',ctx)

#addPaie

def addpaiement(request):
    frs = Frais.objects.all()
    apr = Aprenant.objects.all()

    if request.method == 'POST':
        msg = None
        frais_id = request.POST.get("fraisid",None)
        aprenant_id = request.POST.get("aprenantid",None)
        montant = request.POST.get("montant",0)
        
        paies = Paiement.objects.filter(aprenant=aprenant_id,frais=frais_id)
        frss = Frais.objects.get(pk=frais_id)
        somme=0
        for p in paies:
            somme += p.montant
        sm = int(montant) + somme
        print("MUKHUT %%%%",sm)
        if frais_id:
            if  montant:
                if  aprenant_id:
                    if somme >= frss.cout:
                        msg = "Cet aprenant a déjà soldé ce frais"
                        
                    elif sm > frss.cout:
                         msg = "Le montant inscrit est supérieur au solde resté pour ce frais"
                    elif int(montant)>frss.cout:
                        msg = "Le montant inscrit est supérieur au coût de ce frais"
                         
                    else:
                        #frs = Frais.objects.get(pk=frais_id)
                        apr = Aprenant.objects.get(pk=aprenant_id)
                        paie = Paiement(
                                aprenant = apr,
                                frais = frss,
                                montant = montant
                            ) 
                        paie.save()
                        return HttpResponseRedirect('/paie/')
        else:
            msg ="Veuillez remplir les champs obliatoires"
        
            
    return render(request,'formulaire/FPaiement.html',{'msg':msg,'frs': frs,'apr': apr})

#Delete paie
def deletePaie(request,id):
    p = Paiement.objects.get(pk=id)
    p.delete()
    return HttpResponseRedirect('/paie/')

