from django.urls import path
from . import views

urlpatterns = [
path('devices/', views.get_all_devices, name='get_all_devices'),
path('devices/<int:id>/', views.get_device_by_id, name='get_device_by_id'),
path('devices/create/', views.create_device, name='create_device'), # New URL pattern for create_device
path('devices/predict/<int:id>/', views.pred_by_id, name='predict_price'), # New URL pattern for pred_by_id
]