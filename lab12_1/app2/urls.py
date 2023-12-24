from django.urls import path
from app2 import views as app2_views

urlpatterns = [
    path('showEmployees/',app2_views.show_employees, name='show_employees'),
]
