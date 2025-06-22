from rest_framework import serializers
from .models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        # fields = ('car_name','car_version','car_model')
        fields = '__all__'