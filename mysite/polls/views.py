from django.shortcuts import render, redirect, reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .classviews import PicPageView, TeamPageView, TestimonView, NewsView
from django.template import loader
from polls.models import Info,Client,Team,Index,Testo,Port,Why,Toggle,Service,Aboutinfo,Aboutdis,Newsletter
from .forms import ContactForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from .forms import PasswordChangedForm, UserChangedForm, UserForm, UserCreateForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.core.mail import send_mail


# Create your views here.

#def index (request):

    #template = loader.get_template('index.html')
    #return HttpResponse(html)

#def home(request):
    #return render(request,'index.html',{})


def index(request):
    image = Client.objects.all()
    photo = Team.objects.all()
    data = Index.objects.all()
    test = Testo.objects.all()
    folio = Port.objects.all()
    us = Why.objects.all()
    togg = Toggle.objects.all()
    servic = Service.objects.all()
    title = Aboutinfo.objects.all()
    detail = Aboutdis.objects.all()
    cric = Newsletter.objects.all()
    return render(request, 'polls/index.html',{"img": image, "pic": photo, "dat": data, "tst": test, "pt": folio, "uss": us, "tog": togg, "ser": servic, "titl": title, "deta": detail, "nu": cric})


def emailView(request):
    #print("djvjhdvsjvd")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                #data = {'name':name,'subject':subject,'email':email, 'message':message}
            	Info.objects.create(name=name,subject=subject,email=email, message=message)
                #send_mail(name, subject, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('show')
            return JsonResponse({'msg':'OK','tmsg':"Your message has been sent. Thank you!"})
        else:
            pass

@login_required
def successView(request):
    return HttpResponse('Success! Thank you for your message.')

@login_required
def contactView(request):
    return render(request, 'polls/show.html')
    
def loginView(request):
    return render(request, 'polls/login_base.html')

def signupView(request):
    return render(request, 'polls/register_user.html')


#def testimonview(request):
    #return render(request, 'polls/testimon.html')
#def get_data(request):
    #if request.method == 'POST':
        #form = ContactForm(request.POST)
        #if form.is_valid():
            #return HttpResponseRedirect('')
    #else:
        #form = ContactForm()
    #return render(request, '',{'form': ContactForm})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'base.html', {'form': form})


def change_password(request):
    #print("helloooooo")
    if request.method == 'POST':
        form = PasswordChangedForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangedForm(request.user)
    return render(request, 'polls/password.html', {'form': form})


@login_required
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UserChangedForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show'))
    else:
        form = UserChangedForm()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)


@login_required
def edit_names(request):
    args = {}
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserForm(instance=request.user)
        args['form'] = form
        return render(request, 'registration/edit_user_name.html', args)

    #return render_to_response('registration/edit_user_name.html', args)


def signView(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return reverse('show')
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreateForm()
    return render(request, 'auth/user_form.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponseRedirect(reverse('show'))
    else:
        return HttpResponse('Activation link is invalid!')
