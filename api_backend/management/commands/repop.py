import os
from django.core.management.base import BaseCommand
# Models
from api_backend.models import MMANews
# repoppers
from api_backend.management.commands.repoppers import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        MMANews.objects.all().delete()
        create_new_mma_news(os.getcwd() + "/api_backend/data/news/mmaNewsData.json")