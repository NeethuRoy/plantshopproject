from django.urls import path
from .import views
app_name = 'cart'

urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('update/<int:product_id>/',views.cart_update,name='cart_update'),
    path('minus/<int:product_id>/', views.cart_minus, name='cart_minus'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

]
