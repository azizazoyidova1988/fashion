from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('contact/', views.contact, name="contact"),
    path('regular/', views.regular, name="regular"),
    path('blog/<int:blog_id>/single_blog/', views.single_blog, name="single_blog"),
    path('shop/<int:product_id>/product_details/', views.product_details, name="product_details"),
    path('checkout/', views.checkouts, name="checkout"),
    path('blog/', views.blog, name="blog"),


]