from rest_framework import serializers
from .models import Duties, Crops


class DutiesSerializer(serializers.ModelSerializer):
    '''Сериализатор пошлины на культуру'''
    class Meta:
        model = Duties
        fields = ('crop_id', 'duty')
