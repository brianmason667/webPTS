# Create your views here.

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import hourly
from .models import pauid
from django import forms
from .forms import NameForm


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = ''
    def get_queryset(self):
        """
        testing
        """
        return pauid.id
    
class NewPauidView(generic.CreateView):
    model = pauid
    form_class = NameForm
    template_name = 'main/newpauid.html'
    pa_date = forms.SelectDateWidget()
    shift = forms.NumberInput()
    assembly_line_number_id = forms.Select()
    your_name = forms.CharField(label='Your name', max_length=100)
    def NewPauidForm(request):
        # if is post requrest we process form data
        if request.method == 'POST':
        #create for instance and populate it with data from request
            form = NewPauidForm(request.POST)
            if form.is_valid():
            # proc the data in form.cleaned_data are required
                return HttpResponseRedirect('/main/')
        else:
            form = NewPauidForm()
        
        return render(request, 'newpauid.html', {'form': form})





# class AdminDisplayView(generic.DetailView):
#     # model = users
#     template_name = 'main/AdminDisplay.html'
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())

# class LoginView(generic.DetailView):
#     # model = user
#     template_name = 'main/login.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# class RegisterView(generic.DetailView):
#     # model = users
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
