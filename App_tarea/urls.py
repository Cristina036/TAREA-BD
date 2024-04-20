from django.urls import path
from App_tarea import views

urlpatterns = [
    path('', views.index),
    path('formpage/', views.form_user_view, name='form_user')
]
