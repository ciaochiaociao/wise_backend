from django.db import models
from django.contrib.postgres.indexes import HashIndex


# Create your models here.
class Emotion(models.Model):
  id = models.SmallAutoField(primary_key=True)
  name = models.CharField(max_length=100, unique=True, blank=False, null=False)
  def __str__(self):
    return self.name
  class Meta:
    indexes = [
      HashIndex(fields=['name'])
    ]
  
class EmotionRecord(models.Model):
  emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
  confidence = models.FloatField(blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.emotion} - {self.confidence} - {self.created_at}'
  
  class Meta:
    # use a B-tree index for created_at by default
    indexes = [
      models.Index(fields=['created_at'])
    ]
