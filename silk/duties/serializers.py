from rest_framework import serializers

from .models import (
    Crops,
    Duties,
)


class CropsSerializer(serializers.ModelSerializer):
    """Сериализатор культур"""

    class Meta:
        model = Crops
        fields = ('id', 'name')


class DutiesSerializer(serializers.ModelSerializer):
    """Сериализатор пошлины на культуру"""
    crop = CropsSerializer()

    class Meta:
        model = Duties
        fields = ('crop', 'duty')
