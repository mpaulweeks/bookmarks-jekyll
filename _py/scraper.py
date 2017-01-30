
# python3 -m _py.scraper

import json


def scrape_bookmark(bookmark_data):
    filename = bookmark_data['title']
    author = bookmark_data.get('author')
    if author:
        filename = "%s - %s" % (author, filename)
    print (filename)


def main():
    with open("_data/bookmarks.json", "r") as f:
        data = json.load(f)
    bookmarks = [
        child
        for category in data
        for child in category['children']
        if 'video' not in child.get('meta', [])
    ]
    for b in bookmarks:
        scrape_bookmark(b)


if __name__ == "__main__":
    main()
