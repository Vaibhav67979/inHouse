from django.urls import path,include
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('', views.properties, name="Properties"),
    path('Bangalore/', views.bng, name="Bangalore"),
    path('Chennai/', views.che, name="Chennai"),
    path('Hyderabad/', views.hyd, name="Hyderabad")

]