from django.urls import path
from app1 import views as app1_views

urlpatterns = [    
    path("welcome/", app1_views.welcome, name="welcome"),
    path("about/", app1_views.about, name="about"),
    path("welcome/<str:usname>", app1_views.welcome1, name="welcome1"),
    path("factorial/<int:n>", app1_views.factorial_view, name="factorial"),
    path("OddEven/<int:n>", app1_views.odd_even_view, name="odd_even"),
]
