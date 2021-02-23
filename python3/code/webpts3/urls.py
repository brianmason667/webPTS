

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('ProductionActual/')),
    path('ProductionActual/', include('productionactual.urls')),
    path('Charts/', include('charts.urls')),
    path('admin/', admin.site.urls),
    path('acc/', include('django.contrib.auth.urls')),
    path('catalog/', include('catalog.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # path('main/', include('main.urls')),
    # path('polls/', include('polls.urls')),



