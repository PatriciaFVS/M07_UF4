from django.contrib import admin
from django.urls import path
from centre import views

urlpatterns = [
    path("students/", views.alumnat, name="estudiant"),
    path("teachers/", views.professorat, name="professor"),    
    path("student/<int:id>",views.infoEstudiant, name='student'),
    path("teacher/<int:id>",views.infoProfessor, name='teacher'),
    path('user-form/',views.formulariUsuaris,name='formularis'),
    path('user-form/showUser/',views.index, name='showForm')
    
]
