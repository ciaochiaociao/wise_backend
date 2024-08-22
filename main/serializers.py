from rest_framework import serializers
from .models import Emotion, EmotionRecord


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ['name']

class EmotionRecordSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = EmotionRecord
        fields = ['emotion', 'confidence', 'created_at']