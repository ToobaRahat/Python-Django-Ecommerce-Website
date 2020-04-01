from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("customization/", views.Customization, name="Customization"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("allproducts/", views.allproducts, name="allproducts"),
    path("productupload/", views.productupload, name="productupload"),     
]
