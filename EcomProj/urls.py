"""
URL configuration for EcomProj project.

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

from django.contrib import admin
from django.urls import path
from UserApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path("view_cart",views.view_cart,name="view_cart"),
    path('users/', views.get_users, name='get-users'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('products/', views.view_products, name='view_products'),
]
