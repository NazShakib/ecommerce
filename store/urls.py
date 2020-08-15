from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="store"),
    path('checkout/',views.check,name="checkout"),
    path('chart/',views.chart,name="chart"),

    path('update-data/',views.updateData,name='update-data'),
    path('payment-order/',views.orderProcess,name='payment-order'),

    #user info

    path('login/',views.login,name='login'),
    path('register/',views.register,name='signup'),
]
