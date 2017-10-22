#!/bin/bash

cat $1 | python -c 'import sys; import xml.dom.minidom; s = sys.stdin.read(); print xml.dom.minidom.parseString(s).toprettyxml().encode("utf_8")'
