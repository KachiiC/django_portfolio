import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/api_backend/data/stock"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary"

querystring = {"region": "US", "lang":"en"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591"
    }


class Command(BaseCommand):

    def handle(self, *args, **options):
        mystockrequest = requests.request("GET", url, headers=headers, params=querystring)
        payload = mystockrequest.json()

        with open(f"{OUTFILE_LOCATION}/mySummary.json", 'w', encoding='utf8') as json_file:
            json_file.write(
                json.dumps(payload, indent=4, ensure_ascii=False)
            )

        print(f"successfully prepped mySummary.json")