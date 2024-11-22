from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Display the form
    path('check/', views.check_palindrome, name='check_palindrome'),  # Process the number
]
