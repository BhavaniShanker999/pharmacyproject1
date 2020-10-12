from django.urls import path
from . import views


urlpatterns = [
    path('registration', views.registration_page,name='registration_page'),
    path('login', views.login_page,name='login_page'),
    path('logout', views.logout_user,name='logout'),



    path('', views.home,name='home'),
    path('products', views.products,name='products'),
    path('info', views.info,name='info'),
    path('customer/<str:pk>', views.customer,name='customers'),


    #create update related urls
    path('create_customer',views.create_customer,name='create_customer'),
    path('create_product',views.create_product,name='create_product'),
    path('create_order/<str:pk>',views.create_order_customer,name='create_order'),
    path('update_order/<str:pk>',views.update_order_customer,name='update_order'),
    path('delete_order/<str:pk>',views.delete_order_customer,name='delete_order'),
]
