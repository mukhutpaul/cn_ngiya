import json
from datetime import datetime
from django.http import HttpResponseRedirect
from time import time
from django.shortcuts import render, redirect
import qrcode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login, logout

from app_centre.models import AffectationFormation, AffecteMatiereFormateur, Aprenant, DetailFormation, DetailPresence, Formateur, Formation, Frais, Local, Matiere, Paiement, Presence, Profile, SessionFormation, User
from django.core.paginator import Paginator
from django.db.models import Count
from app_centre.utils import render_to_pdf
from qrcode import *
from django.db.models import Avg

from cn_ngiya import settings

# Create your views here.
@login_required(login_url="sign_in")
def home(request):
    nbrAprenant = Aprenant.objects.all().count()
    nbrFormateur = Formateur.objects.all().count()
    nbrFormation = Formateur.objects.all().count()
    nbrhomme = Aprenant.objects.filter(sexe="M").count()
    nbrFemme = Aprenant.objects.filter(sexe="F").count()
    formations = Formation.objects.all()
    utilisateurs = User.objects.all().count()
    
    phomme = round((nbrhomme * 100 / nbrAprenant),1)
    pfemme = round((nbrFemme * 100 / nbrAprenant),1)
   
    data = []
    
    for d in formations:
        nbr =AffectationFormation.objects.filter(formation=d).count()
        data.append({
            'formation':d.designaion,
            'id':d.id,
            'compte': nbr
        })
    
    ctx ={
        'hm': 'active',
        'nbrAprenant':nbrAprenant,
        'nbrFormateur':nbrFormateur,
        'nbrFormation': nbrFormation,
        'nbrlocal': Local.objects.all().count(),
        'nbrhomme':nbrhomme,
        'nbrFemme':nbrFemme,
        "noms": request.user.noms,
        "profile": request.user.profile,
        'formations': data,
        "p_homme" : json.dumps(phomme),
        "p_femme" : json.dumps(pfemme),
        'utilisateurs': utilisateurs 
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
        p = Paginator(Formateur.objects.all().order_by('-id'), 20)
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
        p = Paginator(Formation.objects.all().order_by('-id'), 20)
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
        p = Paginator(Local.objects.all().order_by('-id'), 20)
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
        p = Paginator(Frais.objects.all().order_by('-id'), 20)
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
        msk = None
        frais_id = request.POST.get("fraisid",None)
        aprenant_id = request.POST.get("aprenantid",None)
        montant = request.POST.get("montant",0)
        somme=0
        sm =0
        
        if frais_id == '':
            msg ="Veuillez remplir le frais"
        elif  montant=='':
            msg ="Veuillez remplir le montant"
        
        elif  aprenant_id == '':
            paies = Paiement.objects.filter(aprenant=aprenant_id,frais=frais_id)
            frss = Frais.objects.get(pk=frais_id)
            for p in paies:
                somme += p.montant
            sm = int(montant) + somme
            print("MUKHUT %%%%",sm)
            msg ="Veuillez choisir l aprenant"
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
                msk = "Traitement ok"
                print("aaaaaaaaa",msk)
                #return HttpResponseRedirect('/paie/')
        
            
    return render(request,'formulaire/FPaiement.html',{'msg':msg,'frs': frs,'apr': apr,'msk':msk})

#Delete paie
def deletePaie(request,id):
    p = Paiement.objects.get(pk=id)
    p.delete()
    return HttpResponseRedirect('/paie/')


##Formulaire Matière
@login_required(login_url="sign_in")
def fmatiere(request):
    
    
    return render(request,'formulaire/FMatiere.html')

##ADD MATIERES
def addMatiere(request):
    if request.method == 'POST':
        msg = None
        msok = None
        designat = request.POST.get("matiere",None)
        hr = request.POST.get("heure",None)
        
        if designat == '':
            msg ="Veuillez remplir la désignation"
        elif hr == '':
            msg ="Veuillez remplir le volume horaire"
        else:
            mt = Matiere(
                designation = designat.upper(),
                nombreHeure = hr
            )
            mt.save()
            msok = "Traitement ok"
            #return HttpResponseRedirect('/matiere/')
    ctx ={
        'msg':msg,
        'msok': msok
    }
    return render(request,'formulaire/FMatiere.html',ctx)


###APPRENANT FORMULAIRES

@login_required(login_url="sign_in")
def fAprenant(request):
    
    
    return render(request,'formulaire/FAprenant.html')

##ADD APPRENANT
def addAprenant(request):
   
    if request.method == 'POST':
        msg = None
        mesok =None
        nom = request.POST.get("nom",None)
        postnom = request.POST.get("postnom",None)
        prenom = request.POST.get("prenom",None)
        lieu = request.POST.get("lieu",None)
        datenais = request.POST.get("datenais",None)
        langue = request.POST.get("langue",None)
        etatciv = request.POST.get("etatciv",None)
        niveau = request.POST.get("niveau",None)
        adresse = request.POST.get("adresse",None)
        email = request.POST.get("email",None)
        telephone  = request.POST.get("telephone",None)
        sexe  = request.POST.get("sexe",None)
        
        if nom == '':
            msg ="Veuillez remplir le nom"
        elif postnom == '':
            msg ="Veuillez remplir le postnom"
        elif prenom == '':
            msg ="Veuillez remplir le prenom"
        elif lieu == '':
            msg ="Veuillez remplir le lieu de naissance"
        elif datenais == '':
            msg ="Veuillez remplir la date de naissance"
        elif langue == '':
            msg ="Veuillez choisir la langue"
        elif etatciv == '':
            msg ="Veuillez remplir l'état civil"
        elif niveau == '':
            msg ="Veuillez remplir l'état civil"
        elif telephone == '':
            msg ="Veuillez remplir le téléphone"
        elif adresse == '':
            msg ="Veuillez remplir l'adresse"
        elif email == '':
            msg ="Veuillez remplir le mail"
        elif sexe == '':
            msg ="Veuillez remplir le sexe"
        else:
            
            apr = Aprenant(
                nom = nom.upper(),
                postnom = postnom.upper(),
                prenom = prenom.upper(),
                lieunaissance = lieu.upper(),
                datenaissance = datenais,
                sexe = sexe.upper(),
                Etatcivil = etatciv.upper(),
                niveauEtude = niveau.upper(),
                telephone = telephone.upper(),
                email = email,
                langue = langue.upper(),
                adresse = adresse.upper()
            )
            apr.save()
            mesok = nom + " "+postnom+" est inscrit avec succès"
            #return HttpResponseRedirect('/aprenant/')
    ctx ={
        'msg':msg,
        'mesok': mesok 
    }
    return render(request,'formulaire/FAprenant.html',ctx)
     
        

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
        p = Paginator(Presence.objects.all().order_by(('-id')), 20)
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
        compte = len(AffectationFormation.objects.filter(aprenant__id=sel_aprenant.id))
    
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


#Formulaires Présence
@login_required(login_url="sign_in")
def fpresence(request):
    matiere = Matiere.objects.all()
    session = SessionFormation.objects.all()
    formation = Formation.objects.all()
    
    ctx = {
        'matiere': matiere,
        'session': session,
        'formation': formation
    }
    
    return render(request,'formulaire/FPresence.html',ctx)

#addPrésence

def addpresence(request):
   
    if request.method == 'POST':
        msg = None
        msok = None
        dateP = request.POST.get("dateP",None)
        session = request.POST.get("session",None)
        formation = request.POST.get("formation",None)
        matiere = request.POST.get("matiere",None)
        
        if dateP == '':
            msg ="Veuillez remplir la date"
            matiere = Matiere.objects.all()
            session = SessionFormation.objects.all()
            formation = Formation.objects.all()
        elif  session=='':
            matiere = Matiere.objects.all()
            session = SessionFormation.objects.all()
            formation = Formation.objects.all()
            msg ="Veuillez remplir la session"
        
        elif  formation == '':
            matiere = Matiere.objects.all()
            session = SessionFormation.objects.all()
            formation = Formation.objects.all()
            msg ="Veuillez remplir la formation"
        elif  matiere == '':
            matiere = Matiere.objects.all()
            session = SessionFormation.objects.all()
            formation = Formation.objects.all()
            msg ="Veuillez remplir la matiere"
        else:
            mat = Matiere.objects.get(pk=matiere)
            ses = SessionFormation.objects.get(pk=session)
            form = Formation.objects.get(pk=formation)
            pr = Presence(
                formation = form,
                matiere = mat,
                sesion = ses,
                datePr = dateP
            )
            pr.save()
            msok = "Traitement ok!"
    ctx ={
        'msg':msg,
        'msok':msok,
        'matiere': matiere,
        'formation': formation,
        'session': session
    }
    return render(request,'formulaire/FPresence.html',ctx)

##Formulaire Local
@login_required(login_url="sign_in")
def flocal(request):
    
    
    return render(request,'formulaire/FLocal.html')

##ADD MATIERES
def addLocal(request):
   
    if request.method == 'POST':
        msg = None
        msok = None
        designat = request.POST.get("designation",None)
        cap = request.POST.get("cap",None)
        
        if designat == '':
            msg ="Veuillez remplir la désignation"
        elif cap == '':
            msg ="Veuillez remplir la capacité d'accueil"
        else:
            loc = Local(
                designation = designat.upper(),
                capacite = cap
            )
            loc.save()
            msok ="Traitement ok"
            #return HttpResponseRedirect('/matiere/')
    ctx ={
        'msg':msg,
        'msok': msok 
    }
    return render(request,'formulaire/FLocal.html',ctx)

##Formulaire Formation
@login_required(login_url="sign_in")
def fFormation(request):
    
    
    return render(request,'formulaire/FFormation.html')

##ADD Formation
def addFormation(request):
    if request.method == 'POST':
        msg = None
        msok = None
        designat = request.POST.get("designation",None)
        duree = request.POST.get("duree",None)
        
        if designat == '':
            msg ="Veuillez remplir la désignation"
        elif duree == '':
            msg ="Veuillez remplir la durée de la formation"
        else:
            form = Formation(
                designaion = designat.upper(),
                duree = duree.upper()
            )
            form.save()
            msok ="Traitement ok"
            #return HttpResponseRedirect('/matiere/')
    ctx ={
        'msg':msg,
        'msok': msok 
    }
    return render(request,'formulaire/FFormation.html',ctx)


##Formulaire Frais
@login_required(login_url="sign_in")
def fFrais(request):
    
    
    return render(request,'formulaire/FFrais.html')

##ADD FRAIS
def addFrais(request):
    if request.method == 'POST':
        msg = None
        msok = None
        designat = request.POST.get("designation",None)
        cout = request.POST.get("cout",None)
        
        if designat == '':
            msg ="Veuillez remplir la désignation"
        elif cout == '':
            msg ="Veuillez remplir le coût"
        elif len(cout)>3:
            msg ="le coût ne peut pas être supérieur à 3 caractères"
        else:
            fr = Frais(
                designation = designat.upper(),
                cout = cout
            )
            fr.save()
            msok ="Traitement ok"
            #return HttpResponseRedirect('/matiere/')
    ctx ={
        'msg':msg,
        'msok': msok 
    }
    return render(request,'formulaire/FFrais.html',ctx)


###FORMATEUR FORMULAIRES

@login_required(login_url="sign_in")
def fFormateur(request):
    
    return render(request,'formulaire/FFormateur.html')

##ADD APPRENANT
def addFormateur(request):
   
    if request.method == 'POST':
        msg = None
        mesok =None
        nom = request.POST.get("nom",None)
        postnom = request.POST.get("postnom",None)
        prenom = request.POST.get("prenom",None)
        etatciv = request.POST.get("etatciv",None)
        niveau = request.POST.get("niveauEtud",None)
        adresse = request.POST.get("adresse",None)
        email = request.POST.get("email",None)
        telephone  = request.POST.get("telephone",None)
        sexe  = request.POST.get("sexe",None)
        
        if nom == '':
            msg ="Veuillez remplir le nom"
        elif postnom == '':
            msg ="Veuillez remplir le postnom"
        elif prenom == '':
            msg ="Veuillez remplir le prenom"
        elif etatciv == '':
            msg ="Veuillez remplir l'état civil"
        elif niveau == '':
            msg ="Veuillez remplir l'état civil"
        elif telephone == '':
            msg ="Veuillez remplir le téléphone"
        elif adresse == '':
            msg ="Veuillez remplir l'adresse"
        elif email == '':
            msg ="Veuillez remplir le mail"
        elif sexe == '':
            msg ="Veuillez remplir le sexe"
        else:
            
            apr = Formateur(
                nom = nom.upper(),
                postnom = postnom.upper(),
                prenom = prenom.upper(),
                sexe = sexe.upper(),
                Etatcivil = etatciv.upper(),
                niveauEtude = niveau.upper(),
                telephone = telephone.upper(),
                email = email,
                adresse = adresse.upper()
            )
            apr.save()
            mesok = nom + " "+postnom+" est inscrit avec succès"
            #return HttpResponseRedirect('/aprenant/')
    ctx ={
        'msg':msg,
        'mesok': mesok 
    }
    return render(request,'formulaire/FFormateur.html',ctx)

##DETAILS FORMATEURS
def detailFormateur(request,id):
    sel_formateur = Formateur.objects.get(id = id)
    #liste_formationD = AffectationFormation.objects.all()
    matiere = Matiere.objects.all()
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(AffecteMatiereFormateur.objects.filter(formateur__nom__contains=rech,formateur__id=sel_formateur.id) |
        AffecteMatiereFormateur.objects.filter(formateur__postnom__contains=rech,formateur__id=sel_formateur.id) |
        AffecteMatiereFormateur.objects.filter(matiere__designation__contains=rech,formateur__id=sel_formateur.id),20)
        page = request.GET.get('page')
        list_detailF =p.get_page(page)
        compte = len(list_detailF)
        if rech == '':
             compte = len(AffecteMatiereFormateur.objects.filter(formateur__id=sel_formateur.id))  
        
    else:
        p = Paginator(AffecteMatiereFormateur.objects.filter(formateur__id=sel_formateur.id).order_by('-id'), 20)
        page = request.GET.get('page')
        list_detailF =p.get_page(page)
        compte = len(AffecteMatiereFormateur.objects.filter(formateur__id=sel_formateur.id))
    
    ctx = {
        'sel_formateur': sel_formateur,
        'list_detailF': list_detailF,
        'matiere': matiere,
        'lf': 'active',
        'compte':compte
    }
    return render(request,'page/detailFormateur.html',ctx)

##ADD DETALS FORMATEUR
def addDetailFormateur(request):
    if request.method == 'POST':
        msg = None
        formateur = request.POST.get("formateur",None)
        matiere = request.POST.get("matiere",None)

        if formateur =='':
            msg = "Veuillez choisir la matière"
        elif  matiere=='':
            msg="Veuillez choisir la matière"
       
        else:
            format = Formateur.objects.get(pk=formateur)
            mat = Matiere.objects.get(pk=matiere)
            
            matiere = AffecteMatiereFormateur(
                formateur = format,
                matiere = mat,
            ) 
            matiere.save()
            return HttpResponseRedirect('/detailFormateur'+formateur)
    return HttpResponseRedirect('/detailFormateur'+formateur)

@login_required(login_url="sign_in")
def users(request):
    if request.method == "POST":
        rech = request.POST['rech']
        p = Paginator(User.objects.filter(username__contains=rech) |
        User.objects.filter(noms__contains=rech) )
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(User.objects.all())  
        
    else:
        p = Paginator(User.objects.all().order_by('-id'), 20)
        page = request.GET.get('page')
        pages =p.get_page(page)
        compte = len(User.objects.all())
    ctx = {
        'compte' : compte,
        'users' : pages,
        'luser': 'active',
        'pages':pages
    }
    return render(request,'user/user.html',ctx)

##Formulaire Frais
@login_required(login_url="sign_in")
def fUser(request):
    profiles = Profile.objects.all()
    
    ctx = {
        'pro': profiles
    }
    
    
    return render(request,'formulaire/FUser.html',ctx)

##ADD USERS
def addUser(request):
    if request.method == 'POST':
        profiles = Profile.objects.all()
        msg = None
        msok =None
        profile = request.POST.get("profile",None)
        noms = request.POST.get("noms",None)
        username = request.POST.get("username",None)
        email = request.POST.get("email",None)
        password = request.POST.get("password",None)

        if email =='':
            msg = "Veuillez remplir le mail"
            profiles = Profile.objects.all()
        elif profile=='':
            msg="Veuillez choisir le profile"
            profiles = Profile.objects.all()
        
        elif len(User.objects.filter(username=username))>0:
            msg="Ce nom utilisateur existe déjà"
            profiles = Profile.objects.all()
            
        elif len(User.objects.filter(email=email))>0:
            msg="Cette adresse mail existe déjà"
            profiles = Profile.objects.all() 
        elif noms=='':
            msg="Veuillez remplir les noms"
            profiles = Profile.objects.all()
        elif username =='':
            msg="Veuillez remplir le nom utilisateur"
            profiles = Profile.objects.all()
        elif password =='':
            msg="Veuillez remplir le mot de passe"
            profiles = Profile.objects.all()
        else:
            pro = Profile.objects.get(pk=profile)
            
            u = User(
                noms = noms.upper(),
                profile = pro,
                username = username.upper(),
                email = email,
                is_active = True
            ) 
            u.set_password(password)
            u.save()
            msok = username+ " est enregistré comme utiisateur"
            
            #return HttpResponseRedirect('/detailFormateur'+formateur)
        
    return render(request,'formulaire/FUser.html',{'msg':msg,'msok':msok,'pro':profiles})


##STATISTIQUES PRESENCES

def statistiquePresence(request,id):
    compte = 0
    data = [] 
    nbrfois = 0
    sel_formation = Formation.objects.get(id = id)
    liste_presence = Presence.objects.filter(formation__id =sel_formation.id).count()
    nbrApe =AffectationFormation.objects.filter(formation__id=sel_formation.id).count()
    
    nbrH =AffectationFormation.objects.filter(formation__id=sel_formation.id,aprenant__sexe="M").count()
    nbrF =AffectationFormation.objects.filter(formation__id=sel_formation.id,aprenant__sexe="F").count()
   
    
    v =DetailPresence.objects.values('aprenant__nom','aprenant__postnom',
    'aprenant__prenom').filter(Presence__formation=sel_formation).annotate(total=Count('id'),taux=Count('id')*100/liste_presence).order_by('aprenant__nom')
    
    myn = DetailPresence.objects.aggregate(Avg("id", default=0))
    print("Mukhut",myn)
    
   

    ctx = {
        'sel_formation':  sel_formation,
        'compte':len(v),
        'nbrseance': liste_presence,
        'nbrApe': nbrApe,
        'apr': v,
        'nbrH': nbrH,
        'nbrF': nbrF
    }
   
    
    return render(request,'page/statistiques.html',ctx)




