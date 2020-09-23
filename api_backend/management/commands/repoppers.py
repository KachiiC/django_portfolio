import json
from api_backend.models import MMANews


def create_new_mma_news(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)
        news = data["latestNews"]

        for x in news:
            MMANews(
                title=x["title"],
                article=x["sourceUrl"],
                thumbnail_url=x["thumbnail"],
                img_url=x["imgUrl"]
            ).save()

    print("repop successful MMA News")