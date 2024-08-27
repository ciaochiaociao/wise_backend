from django.shortcuts import render
from django.db.models import Count, Avg

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView

from django_filters import rest_framework as filters

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from .models import EmotionRecord
from .serializers import EmotionRecordSerializer, EmotionRecordAggregateSerializer

class EmotionRecordFilterSet(filters.FilterSet):
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
    filterset_class = EmotionRecordFilterSet


class EmotionRecordAggregateView(GenericAPIView):  # this provides get_queryset method
    queryset = EmotionRecord.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmotionRecordFilterSet


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='func',
                description='The aggregation function to apply. Supported values: count, average.',
                required=True,
                type=OpenApiTypes.STR,
                enum=['count', 'average']
            ),
        ],
        responses={200: EmotionRecordAggregateSerializer(many=True)},  # Adjust the response schema as needed
    )
    def get(self, request, *args, **kwargs):

        # Check if 'aggregate' query parameter is present
        aggregate = request.query_params.get('func')
        if not aggregate:
            return Response({'error': 'The "func" query parameter is required.'}, status=400)
        
        # Apply filters to the queryset
        # print(request.GET)
        # filtered_queryset = self.filter_queryset(self.queryset)
        filterset = self.filterset_class(request.GET, queryset=self.queryset)
        if not filterset.is_valid():
            return Response(filterset.errors, status=400)
        
        filtered_queryset = filterset.qs
        # Dictionary mapping supported aggregation operations to Django ORM functions
        aggregation_operations = {
            'count': Count('id'),
            'average': Avg('confidence'),
        }

        if aggregate in aggregation_operations:
            # Perform the requested aggregation
            aggregation_result = filtered_queryset.values('emotion__name').annotate(result=aggregation_operations[aggregate]).order_by('emotion__id')
            
            # Return the aggregation result as a JSON response
            return Response(aggregation_result)
        
        # If 'aggregate' parameter is not present or not supported, proceed with the default behavior
        return super().list(request, *args, **kwargs)