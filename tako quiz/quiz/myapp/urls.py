from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employees, name='employees'),
    path('stacks/', views.stacks, name='stacks'),
    path('team-leads/', views.team_leads, name='team_leads'),
]
