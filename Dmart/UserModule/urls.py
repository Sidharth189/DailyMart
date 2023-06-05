from django.urls import path
from .import views

urlpatterns=[
    path('',views.userindex,name='userindex'),
    path('shopgrid',views.shopgrid,name='shopgrid'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('contact',views.contact,name='contact'),
    path('userreg',views.userreg,name='userreg'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('productdetails/<int:id>',views.productdetails,name='productdetails'),
    path('shopcart',views.shopcart,name='shopcart'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    path('removecart/<int:id>/',views.removecart,name='removecart'),
    path('checkoutpage',views.checkoutpage,name='checkoutpage'),
    path('checkout',views.checkout,name='checkout'),
    path('cartupdate',views.cartupdate,name='cartupdate'),
    path('searchpage',views.searchpage,name='searchpage'),
    path('search/',views.search,name='search'),
]