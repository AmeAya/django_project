from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    # path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('', ProductListView.as_view(), name='home'),
]
# path(<url:str>, <view:<class:view>>, name=<name:str>)
