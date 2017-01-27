cp _data/bookmarks.json temp.json
python -m json.tool temp.json > _data/bookmarks.json
rm temp.json
