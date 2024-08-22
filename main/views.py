from django.shortcuts import render
from rest_framework import routers, viewsets
from .models import EmotionRecord
from .serializers import EmotionRecordSerializer

class EmotionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmotionRecord.objects.all()
    serializer_class = EmotionRecordSerializer