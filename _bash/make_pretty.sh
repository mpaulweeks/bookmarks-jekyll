prettify_temp() {
  python -c "import sys,json;print(json.dumps(json.load(sys.stdin),indent=2,separators=(',', ': '),sort_keys=True))"
}

prettify() {
  echo $1
  cp $1 temp.json
  cat temp.json | prettify_temp > $1
  rm temp.json
}

for f in _data/*.json; do prettify "$f"; done
