from django.urls import path
from . import views

urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:pk>/',views.get_product),
    path('orders/', views.order_list),
    path('products/info/', views.product_info),
    path('user-orders/', views.UserOrdersListAPIView.as_view()),
]
