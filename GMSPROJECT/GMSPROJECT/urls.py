"""
URL configuration for GMSPROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("usage", views.usage, name='usage'),
    path("myprofile", views.myprofile, name='myprofile'),
    path("login", views.login, name='login'),
    path("sendOtp", views.sendOtp, name='sendOtp'),
    path("verifyOtp", views.verifyOtp, name='verifyOtp'),

    path('i18n/', set_language, name='set_lang'),

    path("addaacu/<int:id>", views.addaacu, name='addaacu'),
    path("", include("adminapp.urls")),
    path("", include("userapp.urls")),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

