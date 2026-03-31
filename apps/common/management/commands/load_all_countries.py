import json
from django.core.management.base import BaseCommand
from core.settings import BASE_DIR
from apps.common.models import Country


class Command(BaseCommand):
    help = 'Load all Contries'
    def handle(self, *args, **kwargs):
        try:
            with open(str(BASE_DIR)+"/data/contries.json", encoding='utf-8-sig') as f:
                contries = json.load(f)
                for contry in contries:
                    Country.objects.get_or_create(name=contry['name_uz'],code=contry['code'])

                self.stdout.write(self.style.SUCCESS('Successfully loaded successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))