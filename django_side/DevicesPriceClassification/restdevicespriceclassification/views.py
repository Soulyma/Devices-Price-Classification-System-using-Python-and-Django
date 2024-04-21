from rest_framework.views import APIView
from .models import Device
from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np
import pandas as pd
from .apps import RestdevicespriceclassificationConfig as r 

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'  # Include all fields


@api_view(['GET'])
def get_all_devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_device_by_id(request, id):
    device = get_object_or_404(Device, pk=id)
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

@api_view(['GET'])
def pred_by_id(request, id):
    device = get_object_or_404(Device, pk=id)  # Fetch device data
    device_data = device.__dict__  # Convert to dictionary
    del device_data['id']
    del device_data['_state']
    data = pd.DataFrame([device_data])
    preprocessed_data = r.pre_proc.transform(data)
    
    return Response(r.svm.predict(preprocessed_data))
        
@api_view(['POST'])
def create_device(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the device data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


