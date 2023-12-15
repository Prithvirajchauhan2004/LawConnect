from django.urls import path
from . import views

urlpatterns = [
   path('personal/', views.PersonalDetials, name='personal-detials')
]
