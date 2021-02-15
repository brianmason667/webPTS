import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

def ProductionActual(request):
    return render(request, "productionactual.html")

def NewProductionActual(request):
    context ={}
    form = NewProductionActualForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "newproductionactual.html", context)


    # ProductionActual_ID = ProductionActual.ProductionActual_id
    # ProductionActual_Instance = get_object_or_404(ProductionActual, pk=ProductionActual_ID)

    # if request.method == 'POST':
    #     form = NewProductionActualForm(request.POST)
    #     if form.is_valid():
    #         ProductionActual_Instance.pa_date = form.cleaned_data['pa_date']
    #         ProductionActual_Instance.save()

    #         return HttpResponseRedirect(reverse('index') )
    # else:
    #     proposed_pa_date = datetime.date.today()
    #     form = NewProductionActualForm(initial={'pa_date': proposed_pa_date})

    # context = {
    #     'form': form,
    #     'ProductionActual_Instance': ProductionActual_Instance,
    # }

    # return render(request, 'productionactual/newproductionactual.html', context)