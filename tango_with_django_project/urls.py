
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^admin/',admin.site.urls),
    url(r'^rango/', include('rango.urls')),
    ]



