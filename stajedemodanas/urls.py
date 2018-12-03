"""stajedemodanas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from stajedemodanas.views import HomePageView, SignupView, validate_username

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^deliverers/', include(('deliverers.urls', 'deliverers'), namespace='deliverers')),
    url(r'^receivers/', include(('receivers.urls', 'receivers'), namespace='receivers')),
    url(r'^workplaces/', include(('workplaces.urls', 'workplaces'), namespace='workplaces')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home-page'),
    path('ajax/validate_username/', validate_username, name='validate_username'),
]

urlpatterns += staticfiles_urlpatterns()
