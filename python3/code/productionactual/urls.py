from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlankProductionActualView, name='BlankProductionActual'),
    path('New/', views.NewProductionActualView, name='NewProductionActual'),
    path('Open/', views.OpenProductionActualView.as_view(), name='OpenProductionActual'),
    path('<uuid:pk>/', views.ProductionActualView, name="ProductionActual"),
    path('<uuid:pk>/LostTime', views.LostTimeView, name="LostTime"),
    path('NewProduct/', views.NewProductView, name='NewProduct'),
]



# NewProductionActualForm

# localhost/pa/AS2001/2/10071992/

# urlpatterns += [
#     path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
# ]
