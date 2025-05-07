from rest_framework import serializers
from .models import LearningItem

class LearningItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningItem
        fields = '__all__'
