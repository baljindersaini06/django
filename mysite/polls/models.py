from __future__ import unicode_literals
from django.db import models
from time import time
from django.contrib.auth.models import User

# Create your models here.



product_type = (
        ('app','APP'),
        ('card','CARD'),
        ('web','WEB'),
    )


icon_type = (
    ('ion-ios-analytics-outline','Analytics Outline Icon'),
    ('ion-ios-bookmarks-outline','Bookmarks Outline Icon'),
    ('ion-ios-paper-outline','Paper Outline Icon'),
    ('ion-ios-speedometer-outline','Speedometer Outline Icon'),
    ('ion-ios-world-outline','World Outline Icon'),
    ('ion-ios-clock-outline','Clock Outline Icon'),
)


icon_card = (
    ('fa fa-diamond','Diamond Icon'),
    ('fa fa-language','Language Icon'),
    ('fa fa-object-group','Object Group Icon'),
)


about_type = (
    ('col-lg-6 wow fadeInUp','left'),
    ('col-lg-6 wow fadeInUp order-1 order-lg-2','right')
)

div_type = (
    ('col-lg-6 wow fadeInUp pt-5 pt-lg-0','left'),
    ('col-lg-6 wow fadeInUp pt-4 pt-lg-0 order-2 order-lg-1','right')
)

class Info(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=500)

    def __str__(self):
        return str(self.name)


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return str(self.client_name)


class Team(models.Model):
    team_work = models.CharField(max_length=500 ,default="hello")
    team_name = models.CharField(max_length=100)
    designation_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    email_twitter = models.EmailField()
    email_facebook = models.EmailField()
    email_google = models.EmailField()
    email_linkd = models.EmailField()


    def __str__(self):
        return str(self.team_name)

class Index(models.Model):
    about_head = models.CharField(max_length=50)
    about_dis = models.CharField(max_length=500)
    services_head = models.CharField(max_length=50)
    services_dis = models.CharField(max_length=500)
    portfolio_head = models.CharField(max_length=50)
    team_head = models.CharField(max_length=50)
    team_dis = models.CharField(max_length=500)
    client_head = models.CharField(max_length=50)
    client_dis = models.CharField(max_length=500)
    contact_head = models.CharField(max_length=50)
    testimonials_head = models.CharField(max_length=50)
    why_head = models.CharField(max_length=50)
    why_dis = models.CharField(max_length=500)

    def __str__(self):
        return str(self.about_head)


class Testo(models.Model):
    image = models.ImageField(upload_to='testimonial/')
    tes_name = models.CharField(max_length=50)
    tes_designation = models.CharField(max_length=50)
    tes_des = models.TextField()

    def __str__(self):
        return str(self.tes_name)



class Product(models.Model):
    category = models.CharField(choices=product_type, max_length=50)
    
    def __str__(self):
        return str(self.category)
    


class Port(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    poduct_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.poduct_name)


class Why(models.Model):
    card_icon = models.CharField(choices=icon_card, max_length=50)
    card_title = models.CharField(max_length=50)
    card_dis = models.TextField()
    card_link = models.URLField()

    def __str__(self):
        return str(self.card_title)


class Toggle(models.Model):
    client_toggle = models.IntegerField()
    project_toggle = models.IntegerField()
    hours_toggle = models.IntegerField()
    workers_toggle = models.IntegerField()


class Service(models.Model):
    select_icon = models.CharField(choices=icon_type, max_length=50)
    service_name = models.CharField(max_length=100)
    service_discription = models.TextField()

    def __str__(self):
        return str(self.service_name)
    

class Aboutinfo(models.Model):
    About_discription = models.TextField()
    image = models.ImageField(upload_to='abouts/')
    About_title1 = models.CharField(max_length=50)
    About_discrip1 = models.TextField()
    About_title2 = models.CharField(max_length=50)
    About_discrip2 = models.TextField()
    About_title3 = models.CharField(max_length=50)
    About_discrip3 = models.TextField()

    def __str__(self):
        return str(self.About_title1)


class Aboutdis(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=100)
    clas = models.CharField(choices=about_type, max_length=50)
    div_clas = models.CharField(choices=div_type, max_length=60)
    discription = models.TextField()
    more_discription = models.TextField()

    def __str__(self):
        return str(self.title)


class Newsletter(models.Model):
    heading = models.CharField(max_length=100)
    foot_discription = models.TextField()
    link_head = models.CharField(max_length=50)
    link1 = models.CharField(max_length=50)
    link2 = models.CharField(max_length=50)
    link3 = models.CharField(max_length=50)
    link4 = models.CharField(max_length=50)
    link5 = models.CharField(max_length=50)
    contacthead = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    news_head = models.TextField()
    news_discription = models.CharField(max_length=1000)
    copy = models.CharField(max_length=100)
    strong_text = models.CharField(max_length=100)
    rights = models.CharField(max_length=50)
    designed = models.CharField(max_length=50)
    ulink = models.URLField()
    ulink_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.heading)


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    portfolio = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    url = models.URLField()

    def __str__(self):
        return str(self.portfolio)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='userprofile/')

    def __str__(self):
        return str(self.user)

