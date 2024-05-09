from django.contrib import admin
from django.urls import path
from centre import views

urlpatterns = [
    path("students/", views.alumnat, name="estudiant"),
    path("teachers/", views.professorat, name="professor"),   
    path("student/<int:id>",views.infoEstudiant, name='student'),
    path("teacher/<int:id>",views.infoProfessor, name='teacher'),
    path('user-form/',views.formulariUsuaris,name='formularis'),
    path('user-form/showUser/',views.index, name='showForm'),
    path('user-form/updateUser/<int:id>',views.formulariUpdate, name='actualitza'),
    path('user-form/deleteUser/<int:id>',views.eliminaRegistre,name='elimina')   
]
