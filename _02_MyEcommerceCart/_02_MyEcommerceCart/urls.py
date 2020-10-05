"""_02_MyEcommerceCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

# Improting for Media Directory
from django.conf import settings
from django.conf.urls.static import static

# This are working like this if the path is shop/ it will say that I don't know anything please contact the shop.urls. Then it will go to shop.urls and it will show a path("", views.index, name="ShopHome") it will say the path is {""} and run the function named as index in the views.. and show the content to the userr.And Afterwards it throw him in the shop folder{templates/shop/index.html} and run the content means show it to the user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("shop.urls")),
    path('blog/', include("blog.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
