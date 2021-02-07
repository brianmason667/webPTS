from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('newpauid/', views.NewPauidView.as_view(), name='NewPauid'),
    # path('admin/', views.DetailView.as_view(), name='admin'),    
]
