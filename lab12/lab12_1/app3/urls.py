from django.urls import path
from app3 import views as app3_views

urlpatterns = [
    path('showJob/',app3_views.show_jobs, name='show_Job'),
    path('showBook/',app3_views.show_books, name='show_Book'),
    path('showCustomer/',app3_views.show_customers, name='show_Customers'),
    path('insertJob/<int:n>',app3_views.insert_job, name='insert_Job'),
    path('insertBook/<int:n>',app3_views.insert_book, name='insert_Book'),
    path('insertCustomer/<int:n>',app3_views.insert_customer, name='insert_Customer'),
]