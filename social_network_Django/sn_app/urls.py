"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from sn_app import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('post/<pk>/', views.PostPageView.as_view(), name='post_detail'),
    path('login', views.AuthenticatedView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register' ),
    path('logout', views.logout_user, name='logout'),
    path('post_new', views.PostNewView.as_view(), name='post_new'),
]

