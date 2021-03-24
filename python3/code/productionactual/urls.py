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
    path('<uuid:pk>/EditDowntime/<int:number>', views.EditDowntimeView, name="EditDowntime"),
    path('<uuid:pk>/EditDefects/<int:number>', views.EditDefectView, name="EditDefects"),
    path('<uuid:pk>/Downtime', views.ViewDowntimeView, name="ViewDowntime"),
    path('<uuid:pk>/Defects', views.ViewDefectView, name="ViewDefects"),
    path('<uuid:pk>/RemoveRun', views.RemoveRunView, name="RemoveRun"),
    path('<uuid:pk>/EditRun/<int:number>', views.EditRunView, name="EditRun"),
    path('<uuid:pk>/AddRun', views.AddRunView, name="AddRun"),
    path('<uuid:pk>/LostTime', views.LostTimeView, name="LostTime"),
    path('NewProduct/', views.NewProductView, name='NewProduct'),
    path('<int:year>/<int:month>/<str:line>/QualityControlChart/', views.QualityControlChartView, name='QualityControlChart'),
    path('<int:year>/<int:month>/<str:line>/ProductionControlChart/', views.ProductionControlChartView , name='ProductionControlChart'),
]



# NewProductionActualForm

# localhost/pa/AS2001/2/10071992/

# urlpatterns += [
#     path('<uuid:pk>/', views.ProductionActual, name='ProductionActual'),
# ]
