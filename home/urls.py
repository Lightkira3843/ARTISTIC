from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="home" ),
    path('login/', views.usrin,name="login" ),
    path('logout/', views.usrout,name="logout" ),
    path('signup/', views.usrup,name="signup" ),
    path('cart/', views.cart,name="cart" ),
    path('blog/', views.blog,name="blog" ),
    path('upfedit/', views.upfedit,name="upfedit" ),
    path('upload/', views.uprod,name="upload" ),
    path('artgal/', views.artgal,name="artgal" ),
    path('checkout/', views.checkout,name="checkout" ),
    path('contact/', views.contact,name="contact" )

] # +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

