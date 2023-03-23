#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# top ten keys
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_ten_items = items[0:10]

keys = []
values = []
for key, value in top_ten_items:
    keys.append(key)
    values.append(value)

keys.reverse()
values.reverse()
print(keys, values)

if args.input_path == "reduced.lang":
    plt.title(f'Usage of {args.key} in 2020 Tweets, by Language')
    plt.xlabel('Language')
    category = "language"

else: #reduced.country
    plt.title(f'Usage of {args.key} in 2020 Tweets, by Country')
    plt.xlabel('Country')
    category = "country"

plt.ylabel('Tweet Count')
plt.bar(keys, values)
plt.savefig(f'plots/{category}_{args.key}_barchart.png')
