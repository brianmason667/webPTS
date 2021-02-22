import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import *
from .models import *

## /ProductionActual ##
def BlankProductionActualView(request):
    return render(request, "productionactual.html", )

## /ProductionActual/new/ ##
def NewProductionActualView(request):
    if request.method == 'POST':
        form = NewProductionActualForm(request.POST)
        if form.is_valid():
            # not save until form.save()
            form = form.save(commit=False)
            # set user that is logged in, to the user in the created production actual
            form.user = request.user    
            form.save()
            # get the id of created, to go to that id as a url
            newuuid = form.id
            newuuidstr = str(newuuid)
            baseurl = "/ProductionActual/"
            # need to create hourly
            create_hourly =  Hourly.objects.create(pk=newuuid)
            return HttpResponseRedirect(baseurl+newuuidstr)
    else:
        context ={}
        form = NewProductionActualForm()
        if form.is_valid():
            # not save until form.save()
            form = form.save(commit=False)
            # set user that is logged in to the form user
            form.user = request.user    
            form.save()

        context['form']= form
        return render(request, "newproductionactual.html", context)

## /ProductionActual/open ##
# def OpenProductionActualView(request):
#     return render(request, "openproductionactual.html")
class OpenProductionActualView(generic.ListView):
    template_name = 'openproductionactual.html'
    context_object_name = 'latest_pa_list'

    def get_queryset(self):
        """
        Return the last five created productionactuals (not including those set to be
        created in the future).
        """
        return ProductionActual.objects.filter(pa_date__lte=timezone.now()).order_by('-pa_date')[:50]

## /ProductionActual/20a0904a-ba5f-4a67-a163-03110dae00ce/ ## ex: an opened production actual
def ProductionActualView(request, pk):
    Production_Actual = get_object_or_404(ProductionActual, pk=pk)
    Hourly_Count = Hourly.objects.get(ProductionActual=pk)
    ## attempt to make entering hourly
    hourly_form = HourlyForm(request.POST)
    if hourly_form.is_valid():
        # not save until form.save()
        hourly_form = form.save(commit=False)
        # set user that is logged in, to the user in the created production actual
        hourly_form.id = request.id    
        hourly_form.save()
        
    ##
    context = {
        'ProductionActual': Production_Actual,
        'hourly': Hourly_Count,
        'hourlyform': hourly_form
    }
    return render(request, "productionactual.html", context)