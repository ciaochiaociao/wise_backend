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

class EmotionRecordAggregateSerializer(serializers.Serializer):
    emotion__name = serializers.CharField()
    result = serializers.FloatField()

    class Meta:
        fields = ['emotion__name', 'result']