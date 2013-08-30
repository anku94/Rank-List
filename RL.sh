#!/bin/bash
cd ~/Current; 
python ~/Current/status.bak.py
mv status.html ~/public_html/
python ~/Current/RLprintV3.py > out.txt
cp -f out.txt ~/public_html/
