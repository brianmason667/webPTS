from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlankProductionActualView, name='BlankProductionActual'),
    path('New/', views.NewProductionActualView, name='NewProductionActual'),
    path('Open/', views.OpenYearView, name='OpenYear'),
    path('Open/<int:year>/', views.OpenMonthView, name='OpenMonth'),
    path('Open/<int:year>/<int:month>', views.OpenDepartmentView, name='OpenDepartment'),
    path('Open/<int:year>/<int:month>/<str:department>', views.OpenLineView, name='OpenLine'),
    path('Open/<int:year>/<int:month>/<str:department>/<str:line>', views.OpenProductionActualView, name='OpenProductionActual'),
    path('OpenRecent/', views.OpenRecentProductionActualView.as_view(), name='OpenRecentProductionActual'),
    path('<uuid:pk>/', views.ProductionActualView, name="ProductionActual"),
    path('<uuid:pk>/LostTime', views.LostTimeView, name="LostTime"),
    path('NewProduct/', views.NewProductView, name='NewProduct'),
]



# NewProductionActualForm

# localhost/pa/AS2001/2/10071992/

# urlpatterns += [
#     path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
# ]
