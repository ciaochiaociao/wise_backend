"""wise_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, viewsets, serializers
from main.models import Emotion, EmotionRecord

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ['name']

class EmotionRecordSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = EmotionRecord
        fields = ['emotion', 'confidence', 'created_at']
  
class EmotionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmotionRecord.objects.all()
    serializer_class = EmotionRecordSerializer
router = routers.DefaultRouter()
router.register(r'emotionrecords', EmotionRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api/', include('main.urls'))
]
