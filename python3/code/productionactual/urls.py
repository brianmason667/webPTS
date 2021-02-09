from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.NewProductionActual, name='NewProductionActual'),
]



# NewProductionActualForm

# localhost/pa/AS2001/2/10071992/

# urlpatterns += [
#     path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
# ]

urlpatterns += [
    path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]