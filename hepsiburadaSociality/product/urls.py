from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from product import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
