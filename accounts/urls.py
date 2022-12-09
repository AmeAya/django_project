from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('profile/', TemplateView.as_view(template_name="profile.html"), name='profile'),
]
