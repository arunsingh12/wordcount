
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name= 'home'),
    path('about/',views.about),
    path('count/', views.count, name='count'),

]
