"""ilnurgi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin

from application.views import HomePage
from metrics import urls as metric_urls
from arduino import urls as arduino_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^metrics/', include(metric_urls)),
    url(r'^arduino/', include(arduino_urls)),
    url(r'', HomePage.as_view(), name='home_page'),
]
