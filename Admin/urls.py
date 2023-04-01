from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
from . import views
from RMSapp.views import index

urlpatterns = [
    
    path('', views.admin_car_list, name='adminIndex'),
    path('<int:id>/editOrder/', views.order_update, name = "order_edit"),
    path('<int:id>/deleteOrder/', views.order_delete, name = "order_delete"),
    path('create/', views.car_created, name = "car_create"),
    path('<int:id>/deletemsg/', views.msg_delete, name = "msg_delete"),
    path('carlist/', views.car_list, name = "car_list"),
    path('createOrder/', views.order_created, name = "order_create"),
    path('car/', index, name = 'home'),
    path('<int:id>/edit/', views.car_update, name = "car_edit"),
    path('<int:id>/', views.car_detail, name = "car_detail"),
    path('detail/<int:id>/', views.order_detail, name = "order_detail"),
    path('<int:id>/delete/', views.car_delete, name = "car_delete"),
    path('<int:id>/deleteOrder/', views.order_delete, name = "order_delete"),
    path('contact/', views.contact, name = "contact"),
    path('newcar/', views.newcar, name = "newcar"),
    path('<int:id>/like/', views.like_update, name = "like"),
    path('popularcar/', views.popular_car, name = "popularcar"),
]