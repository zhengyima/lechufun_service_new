from django.conf.urls import url
from django.urls import path

from . import view,login
 
urlpatterns = [
    url(r'^$', view.index),
    path('index/', view.index),
    path('login/', login.login),
    path('detail/', view.detail),

    
]