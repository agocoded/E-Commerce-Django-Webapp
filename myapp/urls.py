from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path("products/", views.product, name='products'),
    path("products/<int:pk>", views.ProductDetailView.as_view(),
         name='product_detail'),
    path("products/add/", views.ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:pk>',
         views.ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>',
         views.ProductDeteleteView.as_view(), name='delete_product'),
    path('products/mylistings/', views.mylistings, name='mylistings'),
]
