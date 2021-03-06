"""findtorun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from find2run.views import (signup, welcome, login, get_locations,
                            update_location, get_users_in_location)


urlpatterns = [
    url(r'^$', welcome),
    url(r'^admin/', admin.site.urls),
    url(r'^get_users_in_location/', get_users_in_location),
    url(r'^get_locations', get_locations),
    url(r'^login', login),
    url(r'^signup', signup),
    url(r'^update_location', update_location),
]
