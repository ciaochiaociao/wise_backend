from django.shortcuts import render
from rest_framework import routers, viewsets
from django_filters import rest_framework as filters
from .models import EmotionRecord
from .serializers import EmotionRecordSerializer

class EmotionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmotionRecord.objects.all()
    serializer_class = EmotionRecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('emotion', 'created_at')
