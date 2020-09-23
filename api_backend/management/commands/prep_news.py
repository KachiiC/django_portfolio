import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/api_backend/data/news"

url = "https://mma-ufc-news.p.rapidapi.com/latest"

headers = {
    'x-rapidapi-host': "mma-ufc-news.p.rapidapi.com",
    'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591"
    }


class Command(BaseCommand):

    def handle(self, *args, **options):

        mynewsrequest = requests.request("GET", url, headers=headers)
        payload = mynewsrequest.json()

        with open(f"{OUTFILE_LOCATION}/mmaNewsData.json", 'w', encoding='utf8') as json_file:
            json_file.write(
                json.dumps(payload, indent=4, ensure_ascii=False)
            )

        print(f"successfully prepped mmaNewsData.json")
