from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('details/<int:cat_id>', views.details, name='details'),
    path('enquery_form_submit', views.enquery_form_submit, name='enquery_form_submit'), 
]