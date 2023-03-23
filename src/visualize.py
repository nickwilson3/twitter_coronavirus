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
from collections import Counter,defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_ten = items[0:10]

keys = []
values = []
for key, value in top_ten:
    keys.append(key)
    values.append(value)

keys.reverse()
values.reverse()
print(keys, values)

if args.input_path == 'reduced.lang':
    plt.xlabel("Language")
    plt.ylabel("Usage level of " + args.key)
    plt.title("Tweets with " + args.key + " in each language in 2020")
else:
    plt.xlabel("Country")
    plt.ylabel("Usage level of " + args.key)
    plt.title("Tweets with " + args.key + " from each country in 2020")

plt.bar(keys, values)
# save bar graph file to plots folder
plt.savefig(f'graphs/{args.input_path}__{args.key}_bar.png')
