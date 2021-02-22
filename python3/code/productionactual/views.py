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
        Return the last x created productionactuals (not including those set to be
        created in the future).
        """
        return ProductionActual.objects.filter(pa_date__lte=timezone.now()).order_by('-pa_date')[:50]

## /ProductionActual/20a0904a-ba5f-4a67-a163-03110dae00ce/ ## ex: an opened production actual
def ProductionActualView(request, pk):
    Production_Actual = get_object_or_404(ProductionActual, pk=pk)
    Hourly_Count = Hourly.objects.get(ProductionActual=pk)
    ## make hourly
    h1=int(Hourly_Count.hour1)
    h2=int(Hourly_Count.hour2)
    h3=int(Hourly_Count.hour3)
    h4=int(Hourly_Count.hour4)
    h5=int(Hourly_Count.hour5)
    h6=int(Hourly_Count.hour6)
    h7=int(Hourly_Count.hour7)
    h8=int(Hourly_Count.hour8)
    h9=int(Hourly_Count.hour9)
    h10=int(Hourly_Count.hour10)
    h11=int(Hourly_Count.hour11)
    h12=int(Hourly_Count.hour12)
    ## Cumulative Pcs. calculator
    h1c=h1
    h2c=h1+h2
    h3c=h1+h2+h3
    h4c=h1+h2+h3+h4
    h5c=h1+h2+h3+h4+h5
    h6c=h1+h2+h3+h4+h5+h6
    h7c=h1+h2+h3+h4+h5+h6+h7
    h8c=h1+h2+h3+h4+h5+h6+h7+h8
    h9c=h1+h2+h3+h4+h5+h6+h7+h8+h9
    h10c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10
    h11c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11
    h12c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12
    hourly_calc={
        'hour1calc': h1c,
        'hour2calc': h2c,
        'hour3calc': h3c,
        'hour4calc': h4c,
        'hour5calc': h5c,
        'hour6calc': h6c,
        'hour7calc': h7c,
        'hour8calc': h8c,
        'hour9calc': h9c,
        'hour10calc': h10c,
        'hour11calc': h11c,
        'hour12calc' : h12c
    }
    sethour={
        'hour1': h1,
        'hour2': h2,
        'hour3': h3,
        'hour4': h4,
        'hour5': h5,
        'hour6': h6,
        'hour7': h7,
        'hour8': h8,
        'hour9': h9,
        'hour10': h10,
        'hour11': h11,
        'hour12': h12,
        }
    
    # hourly_form = HourlyForm(initial=sethour)
    hourly_form = HourlyForm1(request.POST) # ,
    if hourly_form.is_valid():
        # not save until form.save()
        hourly_form = hourly_form.save(commit=False)
        # link the hourly object to the correct productionactual uuid
        hourly_form.ProductionActual_id = pk
        hourly_form.save()
        
    ## debug ouput
    debug_out = sethour
    context = {
        'ProductionActual': Production_Actual,
        'hourly': Hourly_Count,
        'hourlyform': hourly_form,
        'hourcalc': hourly_calc,
        'debug_out': debug_out
        
    }
    return render(request, "productionactual.html", context)