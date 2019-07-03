from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView
from django.views import generic
from django.template import loader
from polls.models import Info,Client,Team,Index,Testo,Port,Why,Toggle,Service,Aboutinfo,Aboutdis,Newsletter,Portfolio
from .forms import ContactForm,UserCreateForm, PortfolioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, CreateView



class PicPageView(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'pic.html'

class TeamPageView(generic.ListView):
    model = Team
    template_name = 'polls/teaam.html'

class InPageView(generic.ListView):
    model = Index
    template_name = 'polls/inx.html'

class TestimonView(generic.ListView):
    model = Testo
    template_name = 'polls/testimon.html'

class PortView(generic.ListView):
    model = Port
    template_name = 'polls/porfolio.html'

class WhyView(generic.ListView):
    model = Why
    template_name = 'polls/why.html'

class TogView(generic.ListView):
    model = Toggle
    template_name = 'includes/why us.html'

class ServiceView(generic.ListView):
    model = Service
    template_name = 'includes/services.html'

class AboutView(ListView):
    model = Aboutinfo
    template_name = 'includes/about us.html'

class AboutDisView(ListView):
    model = Aboutdis
    template_name = 'includes/about us.html'

class NewsView(TemplateView):
    model = Newsletter
    template_name = 'includes/footer.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm

    def get_success_url(self):
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password1'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return reverse('show')
        return reverse('register')

class Disc(TemplateView):
    template_name='polls/profile.html'

class AddPortfolioView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    
    def get_success_url(self):
        return reverse('showportfolio')

class PortfolioView(ListView):
    model=Portfolio
    
