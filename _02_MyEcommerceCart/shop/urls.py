from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),    
    path("about/", views.about, name="AboutUs"),    
    path("contact/", views.contact, name="Contactus"),    
    path("tracker/", views.tracker, name="TrackingStatus"),    
    path("search/", views.search, name="Search"),    
    path("productview/", views.productView, name="ProductView"),    
    path("checkout/", views.checkout, name="Checkout"),    
]