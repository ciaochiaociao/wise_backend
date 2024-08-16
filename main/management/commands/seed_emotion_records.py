import datetime
import random
from django.core.management.base import BaseCommand
from main.models import EmotionRecord

class Command(BaseCommand):
  help = 'Seeds the database with some initial data'

  def handle(self, *args, **options):
    # Define the data to be inserted

    # a simulation of the random data that has 6 emotions and 1000 records, confidence ranges from 0.5 to 1.0, and time ranges from 2024-08-01 09:00:00.000000 to 2024-08-01 21:000:00.000000 chronologically

    for i in range(1000):
      # normally distributed with the highest probability at id 6, which is 'Neutral', and second highest at id 7, which is 'Sad'
      emotion_id = random.choices(range(1, 9), weights=[0.05, 0.05, 0.05, 0.05, 0.05, 0.6, 0.1, 0.05])[0]
      confidence = random.uniform(0.5, 1.0)
      created_at = datetime.datetime(2024, 8, 1, 9, 0, 0) + datetime.timedelta(minutes=i)
      record = EmotionRecord(emotion_id=emotion_id, confidence=confidence, created_at=created_at)
      record.save(force_insert=True)
      EmotionRecord.objects.filter(id=record.id).update(created_at=created_at)
      
      # force the datetime to ignore auto_now_add behavior

    
    self.stdout.write(self.style.SUCCESS('Data imported successfully'))
