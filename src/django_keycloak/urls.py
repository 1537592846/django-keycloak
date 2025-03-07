"""resource_provider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import url, include
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path

from django_keycloak import views

urlpatterns = [
    re_path(r'^login$', views.Login.as_view(), name='keycloak_login'),
    re_path(r'^login-complete$', views.LoginComplete.as_view(),
        name='keycloak_login_complete'),
    re_path(r'^logout$', views.Logout.as_view(), name='keycloak_logout'),
    re_path(r'^session-iframe', views.SessionIframe.as_view(),
        name='keycloak_session_iframe')
]
