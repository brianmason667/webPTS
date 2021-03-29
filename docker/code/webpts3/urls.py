

from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.conf.urls import include
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = [
    path('', lambda r: HttpResponseRedirect('Records/')),
    path('Records/', include('productionactual.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('acc/', include('acc.urls')),
    ]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # path('main/', include('main.urls')),
    # path('polls/', include('polls.urls')),


