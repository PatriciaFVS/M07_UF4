from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UsuariForm
from . import models
 


professor=[
        {"id":1,"nom":"Oriol","cognom1":"Roca","cognom2":"Gómez","correu":"oriol@gmail.com","curs":"DAW2A","tutor":"si","moduls":"MO7"},
        {"id":2,"nom":"Roger","cognom1":"Sobrino","cognom2":"Pérez","correu":"roger@gmail.com","curs":"DAW2B","tutor":"si","moduls":"MO8"},
        {"id":3,"nom":"Carlota","cognom1":"Jimenez","cognom2":"Valencia","correu":"carlota@gmail.com","curs":"DAM2A","tutor":"no","moduls":"MO9"}
    ]

student=[
        {"id":1,"nom":"David","cognom1":"Argüelles","cognom2":"López","correu":"david@gmail.com","curs":"DAW2A","moduls":"MO7"},
        {"id":2,"nom":"Joan","cognom1":"Martinez","cognom2":"Ros","correu":"joan@gmail.com","curs":"DAW2B","moduls":"MO8"},
        {"id":3,"nom":"Maria","cognom1":"Bas","cognom2":"Silva","correu":"maria@gmail.com","curs":"DAM2A","moduls":"MO9"}
    ]


def professorat(request):  
    return render(request,'teachers.html',{"professors":professor})

def alumnat(request):   
    return render(request,'students.html',{"alumnes":student})


def infoProfessor(request,id):
    professorSelected = professor[id-1]

    return render(request,'teachersinfo.html',{"professor":professorSelected})

def infoEstudiant(request,id):
    estudiantSelected = student[id-1]

    return render(request,'studentsinfo.html',{"alumne":estudiantSelected})

def formulariUsuaris(request):
    form=UsuariForm()
    if request.method=='POST':
        form=UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showForm')
    
    context={'form':form}
    return render(request,'form.html',context)

def index(request):
    usuari= list(models.Usuari.objects.all())
    
    return render(request,'formInfo.html',{'usuaris': usuari})



