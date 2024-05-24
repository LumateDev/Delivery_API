from rest_framework import serializers
from .models import DeliveryDepartment, Courier


class DeliveryDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDepartment
        fields = "__all__"


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = "__all__"
