from django.urls import path
from . import views

urlpatterns = [
    path('',views.testing,name='testing'),
	path('product-list/', views.product_list, name="product-list"),
	path('product-detail/<str:pk>/', views.product_details, name="product-detail"),

	path('product-create/', views.product_create, name="product-create"),
	path('product-update/<str:pk>/', views.product_update, name="product-update"),
	path('product-delete/<str:pk>/', views.product_delete, name="product-delete"),


	### customer urls

	path('customer-details/',views.customer_Details,name='customer-details')
]