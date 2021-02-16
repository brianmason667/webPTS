import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

## /ProductionActual/20a0904a-ba5f-4a67-a163-03110dae00ce/ ##
def ProductionActualView(request, pk):
    Production_Actual = get_object_or_404(ProductionActual, pk=pk)
    context = {
        'ProductionActual': ProductionActual,
    }
    return render(request, "productionactual.html", context)