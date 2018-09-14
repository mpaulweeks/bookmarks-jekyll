import copy
import json
import os
import requests


def main():
    API_KEY = os.environ['YOUTUBE_bookmarks']
    BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=%s&key=" + API_KEY

    with open('_data/youtube-raw.json') as f:
        youtube_raw = json.load(f)
    with open('_data/youtube-generated.json') as f:
        youtube_gen = json.load(f)

    gen_by_id = {video['vid']: video for video in youtube_gen}
    youtube_new = []

    for video in youtube_raw:
        vid = video['vid']
        if vid in gen_by_id:
            result = gen_by_id[vid]
        else:
            # scrape from api
            print('scraping ' + video['title'])
            url = BASE_URL % video['vid']
            resp = requests.get(url)
            data = resp.json()['items'][0]

            result = copy.deepcopy(video)
            result['meta'] = data['snippet']
        youtube_new.append(result)

    youtube_sorted = sorted(
        youtube_new,
        key=lambda video: video['meta']['publishedAt'],
        reverse=True,
    )

    with open('_data/youtube-generated.json', 'w') as f:
        json.dump(
            youtube_sorted, f,
            ensure_ascii=False,
            indent=2,
            separators=(',', ': '),
            sort_keys=True,
        )


if __name__ == "__main__":
    main()
