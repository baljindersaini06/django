from django.urls import path
from . import views
from .classviews import PicPageView, TeamPageView, InPageView, TestimonView, PortView, WhyView, UserCreateView, Disc, AddPortfolioView, PortfolioView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns=[
    path('',views.index, name='index'),
    path('form/', views.emailView, name='contactform'),
    path('show', views.contactView, name='show'),
    path('pic', PicPageView.as_view(), name='pic'),
    path('team', TeamPageView.as_view(), name = 'team'),
    path('index', InPageView.as_view(), name = 'index'),
    path('testo', TestimonView.as_view(), name = 'testo'),
    path('portfolio', PortView.as_view(), name = 'portfolio'),
    path('whyus', WhyView.as_view(), name = 'why'),
    path('accounts/login', views.loginView, name = 'accounts'),
    path('base', views.signupView, name = 'base'),
    path('register_user/', UserCreateView.as_view(), name="register"),
    path('accounts/password', views.change_password, name='change_password'),
    path('profile',login_required(Disc.as_view()), name='profile'),
    path('update', views.update_profile, name='update'),
    path('edit',views.edit_names, name='edit'),
    path('addportfolio',login_required(AddPortfolioView.as_view()), name='addportfolio'),
    path('showportfolio',login_required(PortfolioView.as_view()), name='showportfolio'),
    path('userlog', views.signView, name='user'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate')
]