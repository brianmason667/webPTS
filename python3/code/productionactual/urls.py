from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductionActual, name='ProductionActual'),
    path('new/', views.NewProductionActual, name='NewProductionActual'),
]



# NewProductionActualForm

# localhost/pa/AS2001/2/10071992/

# urlpatterns += [
#     path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
# ]
