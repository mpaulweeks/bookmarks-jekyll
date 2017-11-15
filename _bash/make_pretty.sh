prettify() {
  python -c "import sys,json;print json.dumps(json.load(sys.stdin),indent=2,separators=(',', ': '))"
}

cp _data/bookmarks.json temp.json
cat temp.json | prettify > _data/bookmarks.json
rm temp.json

cp _data/conventions.json temp.json
cat temp.json | prettify > _data/conventions.json
rm temp.json
