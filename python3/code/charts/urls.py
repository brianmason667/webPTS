from django.contrib import admin 
from django.urls import path 
from charts import views 

from django.conf import settings
urlpatterns = [
    path('', views.HomeView.as_view()), 
    # path('test-api', views.get_data), 
    path('api', views.ChartData.as_view()), 
]
