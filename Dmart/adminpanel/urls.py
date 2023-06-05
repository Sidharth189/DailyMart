from django.urls import path
from .import views

urlpatterns=[
    path('adminindex',views.adminindex,name='adminindex'),
    path('addcategorypage',views.addcategorypage,name='addcategorypage'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('deletecategory/<int:id>/',views.deletecategory,name='deletecategory'),
    path('editcategorypage/<int:id>/',views.editcategorypage,name='editcategorypage'),
    path('editcategory/<int:id>/',views.editcategory,name='editcategory'),
    path('addproductpage',views.addproductpage,name='addproductpage'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('editproductpage/<int:id>/',views.editproductpage,name='editproductpage'),
    path('editproduct/<int:id>/',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:id>/',views.deleteproduct,name='deleteproduct'),
    path('',views.loginpage,name='loginpage'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('adlogout',views.adlogout,name='adlogout'),
    path('feedback/',views.feedback,name='feedback'),
    path('deletefeedback/<int:id>/',views.deletefeedback,name='deletefeedback')
]