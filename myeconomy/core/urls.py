from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('filter/', views.filter, name='filter'),
    path('ajax/filter-transaction/', views.filter_transaction, name='filter_transaction'),
    path('visualize/', views.visualize, name='visualize'),
]