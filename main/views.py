from django.shortcuts import render
from rest_framework import routers, viewsets
from django_filters import rest_framework as filters
from .models import EmotionRecord
from .serializers import EmotionRecordSerializer

class EmotionRecordFilter(filters.FilterSet):
    class Meta:
        model = EmotionRecord
        fields = {
            'emotion': ['exact'],
            'created_at': ['exact', 'range', 'year', 'time__range', 'time__gt', 'date__range', 'date__gt']
        }
class EmotionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmotionRecord.objects.all()
    serializer_class = EmotionRecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('emotion', 'created_at')
    filterset_class = EmotionRecordFilter
