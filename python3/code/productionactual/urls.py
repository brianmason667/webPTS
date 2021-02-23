from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlankProductionActualView, name='BlankProductionActual'),
    path('new/', views.NewProductionActualView, name='NewProductionActual'),
    path('open/', views.OpenProductionActualView.as_view(), name='OpenProductionActual'),
    path('<uuid:pk>/', views.ProductionActualView, name="ProductionActual"),
    path('newproduct/', views.NewProductView, name='NewProduct'),
]



# NewProductionActualForm

# localhost/pa/AS2001/2/10071992/

# urlpatterns += [
#     path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
# ]
