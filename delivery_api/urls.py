from django.urls import path
from .views import *

urlpatterns = [
    path('couriers/', CourierActionAPIView.as_view(), name='couriers_actions'),
    path('delivery_departments/', DeliveryDepartmentActionAPIView.as_view(), name='delivery_departments_actions'),

]