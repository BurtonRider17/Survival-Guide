#!/bin/bash
# usage: q.sh "query terms" [beforeYYYYMMDD] [num]  -> parse.py rows
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
B=${2:-19500101}; N=${3:-20}
U="https://patents.google.com/xhr/query?url=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1],safe=''))" "q=$1&country=US&before=priority:$B&num=$N")&exp="
curl -s -A "Mozilla/5.0" "$U" -o /tmp/q.json && python3 /workspace/survival-info/patents/parse.py /tmp/q.json
