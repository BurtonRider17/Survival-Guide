#!/bin/bash
# usage: pipeline.sh <Guide>   (after add_patents.py)
set -e
cd /workspace/survival-info/build-xref && python3 xref.py "$1" 2>&1 | grep -v -i warn
cd /workspace/survival-info && python3 split_guides.py "$1" 2>&1 | grep -v -i warn
python3 pack_sources.py "$1" 2>&1 | grep -E "wrote|Sources_" | sort -u
ls -la "$1-parts" 2>/dev/null | grep pdf || true
