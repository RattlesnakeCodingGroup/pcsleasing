from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('Services/', views.Services.as_view(), name='services'),
    path('Agents/', views.Agents.as_view(), name="agents"),
    path('Quote/', views.Quote.as_view(), name='quote'),
    path('ContactUs/', views.Contact.as_view(), name='contact'),

]
