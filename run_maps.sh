#!/bin/bash

for file in /data-fast/twitter2020/*.zip; do
    nohup ./src/map.py --input_path=$file &
done
