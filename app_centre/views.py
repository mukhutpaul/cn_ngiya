import json
from datetime import datetime
from django.http import HttpResponseRedirect
from time import time
from django.shortcuts import render, redirect
import qrcode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login, logout

from app_centre.models import AffectationFormation, Aprenant, DetailFormation, DetailPresence, Formateur, Formation, Frais, Local, Matiere, Paiement, Presence, SessionFormation, User
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
        p = Paginator(Aprenant.objects.all().order_by('-id'), 20)
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
                         msg = "Le montant inscrit est supérieur au solde restant pour ce frais"
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

#Gestion Présences

@login_required(login_url="sign_in")
def presence(request):
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(Presence.objects.filter(formation__designaion__contains=rech) |
        Presence.objects.filter(matiere__designation__contains=rech) |
        Presence.objects.filter(createdat__contains=rech),20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Presence.objects.all())  
        
    else:
        p = Paginator(Presence.objects.all(), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(Presence.objects.all())
    ctx = {
        'compte' : compte,
        'pres' : pages,
        'lpres': 'active',
        'pages':pages
    }
    return render(request,'page/presence.html',ctx)

#Details présence

def detaiPresence(request,id):
    sel_presence = Presence.objects.get(id = id)
    liste_aprenant = Aprenant.objects.all()
    
    
    data =[]
    #for prs in pres:
    #apreAff = AffectationFormation.objects.filter(formation=prs.formation,session=prs.sesion)
    dpres = AffectationFormation.objects.filter()
    
    for d in dpres:
        pres = Presence.objects.filter(formation=d.formation,sesion=d.session,id=sel_presence.id)
        #for p in pres:
        if pres :
            list_sans_prs = DetailPresence.objects.filter(aprenant_id=d.aprenant.id,Presence_id=sel_presence.id) 
            
            if list_sans_prs:
                pass
            else:
                data.append(
                    {
                        'id': d.aprenant.id,
                        'noms': d.aprenant
                    }
                )
            print("#####",d.aprenant)
        else :
            pass
            #print("#####",d.aprenant)
            

    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(DetailPresence.objects.filter(aprenant__nom__contains=rech,Presence_id=sel_presence.id) |
        DetailPresence.objects.filter(aprenant__postnom__contains=rech,Presence_id=sel_presence.id) |
        DetailPresence.objects.filter(Presence__createdat__contains=rech,Presence_id=sel_presence.id),20)
        page = request.GET.get('page')
        list_detailp =p.get_page(page)
        compte = len(list_detailp)
        if rech == '':
             compte = len(DetailPresence.objects.filter(Presence_id=sel_presence.id))  
        
    else:
        p = Paginator(DetailPresence.objects.filter(Presence_id=sel_presence.id), 20)
        page = request.GET.get('page')
        list_detailp =p.get_page(page)
        compte = len(DetailPresence.objects.filter(Presence_id=sel_presence.id))
    
    ctx = {
        'sel_presence': sel_presence,
        'liste_aprenant': data,
        'list_detailp': list_detailp,
        'lpresence': 'active',
        'compte':compte
    }
    return render(request,'page/detailPresence.html',ctx)

def addDetailPresence(request):
    if request.method == 'POST':
        msg = None
        harrive = request.POST.get("harrive",None)
        hdepart = request.POST.get("hdepart",None)
        aprenant = request.POST.get("aprenant",None)
        presence = request.POST.get("presence",None)
        print("#############",presence)
        if harrive =='':
            msg = "Veuillez saisir l'heure d'arrivée"
        elif  hdepart=='':
            msg="Veuillez saisir l'heure départ"
        elif aprenant == '':
            msg="Veuillez choisir l'aprenant"

        else:
            apr = Aprenant.objects.get(pk=aprenant)
            prs = Presence.objects.get(pk=presence)
            ap = DetailPresence(
                    aprenant = apr,
                    Presence =prs ,
                    heurArrive = harrive,
                    heurDepart = hdepart
                            ) 
            ap.save()
            return HttpResponseRedirect('/detaiPresence'+presence)
    return HttpResponseRedirect('/detaiPresence'+presence)

#Detail Aprenant
def detailAprenant(request,id):
    sel_aprenant = Aprenant.objects.get(id = id)
    #liste_formationD = AffectationFormation.objects.all()
    formations = Formation.objects.all()
    sessions = SessionFormation.objects.all()
    


    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(AffectationFormation.objects.filter(aprenant__nom__contains=rech,aprenant__id=sel_aprenant.id) |
        AffectationFormation.objects.filter(aprenant__postnom__contains=rech,aprenant__id=sel_aprenant.id) |
        AffectationFormation.objects.filter(session__designation__contains=rech,aprenant__id=sel_aprenant.id),20)
        page = request.GET.get('page')
        list_detailA =p.get_page(page)
        compte = len(list_detailA)
        if rech == '':
             compte = len(AffectationFormation.objects.filter(aprenant__id=sel_aprenant.id))  
        
    else:
        p = Paginator(AffectationFormation.objects.filter(aprenant__id=sel_aprenant.id), 20)
        page = request.GET.get('page')
        list_detailA =p.get_page(page)
        compte = len(AffectationFormation.objects.all())
    
    ctx = {
        'sel_aprenant': sel_aprenant,
        'list_detailA': list_detailA,
        'laff': 'active',
        'formations':formations,
        'sessions': sessions,
        'compte':compte
    }
    return render(request,'page/detailAprenant.html',ctx)

##ADD DETALS APRENANT
def addDetailAprenant(request):
    if request.method == 'POST':
        msg = None
        session = request.POST.get("session",None)
        formation = request.POST.get("formation",None)
        sponsor = request.POST.get("sponsor",None)
        aprenant = request.POST.get("aprenant",None)
        print("#############",aprenant )
        if session =='':
            msg = "Veuillez choisir la session"
        elif  formation=='':
            msg="Veuillez choisir formation"
       
        else:
            apr = Aprenant.objects.get(pk=aprenant)
            ses = SessionFormation.objects.get(pk=session)
            form = Formation.objects.get(pk=formation)
            ap = AffectationFormation(
                sponsoriser = sponsor,
                aprenant = apr,
                session = ses,
                formation = form
                            ) 
            ap.save()
            return HttpResponseRedirect('/detailAprenant'+aprenant)
    return HttpResponseRedirect('/detailAprenant'+aprenant)


##DETAIL FORMATIONS

def detailFormation(request,id):
    sel_formation = Formation.objects.get(id = id)
    #liste_formationD = AffectationFormation.objects.all()
    matieres = Matiere.objects.all()
    formateurs = Formateur.objects.all()
    
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(DetailFormation.objects.filter(matiere__designaion__contains=rech,formation__id=sel_formation.id) |
        DetailFormation.objects.filter(formateur__nom__contains=rech,formation__id=sel_formation.id) |
        DetailFormation.objects.filter(createdat__contains=rech,formation__id=sel_formation.id),20)
        page = request.GET.get('page')
        list_detailFa =p.get_page(page)
        compte = len(list_detailFa)
        if rech == '':
             compte = len(DetailFormation.objects.filter(formation__id=sel_formation.id))  
        
    else:
        p = Paginator(DetailFormation.objects.filter(formation__id=sel_formation.id), 20)
        page = request.GET.get('page')
        list_detailFa =p.get_page(page)
        compte = len(DetailFormation.objects.filter(formation__id=sel_formation.id))
    
    ctx = {
        'sel_formation': sel_formation,
        'list_detailFa': list_detailFa,
        'ldf': 'active',
        'matieres':matieres,
        'formateurs': formateurs,
        'compte':compte
    }
    return render(request,'page/detailFormation.html',ctx)


## ADD DETAIL FORMATEURS

def addFormation(request):
    if request.method == 'POST':
        msg = None
        formation = request.POST.get("formation",None)
        matiere = request.POST.get("matiere",None)
        formateur = request.POST.get("formateur",None)
    
        print("#############",aprenant )
        if formation =='':
            msg = "Veuillez choisir la formation"
        elif  matiere=='':
            msg="Veuillez choisir formation"
        elif  formation=='':
            msg="Veuillez choisir formation"
       
        else:
            form = Formation.objects.get(pk=formation)
            matr = Matiere.objects.get(pk=matiere)
            format = Formateur.objects.get(pk=formateur)
           
            df = DetailFormation(
                matiere = matr,
                formation = form,
                formateur = format
            ) 
            df.save()
            return HttpResponseRedirect('/detailFormation'+formation)
    return HttpResponseRedirect('/detailAprenant'+formation)


