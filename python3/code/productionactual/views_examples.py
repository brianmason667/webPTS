import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NewProductionActualForm
from .models import ProductionActual

def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def NewProductionActual(request):
    ProductionActual_ID = ProductionActual.ProductionActual_id
    ProductionActual_Instance = get_object_or_404(ProductionActual, pk=ProductionActual_ID)

    if request.method == 'POST':
        form = NewProductionActualForm(request.POST)
        if form.is_valid():
            ProductionActual_Instance.pa_date = form.cleaned_data['pa_date']
            ProductionActual_Instance.save()

            return HttpResponseRedirect(reverse('index') )
    else:
        proposed_pa_date = datetime.date.today()
        form = NewProductionActualForm(initial={'pa_date': proposed_pa_date})

    context = {
        'form': form,
        'ProductionActual_Instance': ProductionActual_Instance,
    }

    return render(request, 'productionactual/newproductionactual.html', context)

