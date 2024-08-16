from django.core.management.base import BaseCommand
from main.models import EmotionRecord


class Command(BaseCommand):
  help = 'Undo the seeding of the database'

  def handle(self, *args, **options):
    EmotionRecord.objects.all().delete()
    self.stdout.write(self.style.SUCCESS('Data deleted successfully'))