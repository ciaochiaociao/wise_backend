from django.contrib import admin
from .models import Emotion, EmotionRecord

# Register your models here.
admin.site.register(Emotion)
admin.site.register(EmotionRecord)