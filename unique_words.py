"""
The program construct a dictionary where the keys are all unique words in all the files, regular expression used is r"\w+".
The value of each entry is a list of file names that contain the word.
"""

import glob
import re
from collections import Counter, defaultdict

files_list = glob.glob('*.txt')
unique_words = defaultdict(list)

for file in files_list:
    with open(file, 'r') as f:
        word_counter = Counter(re.findall(r"\w+", f.read().lower()))
        for (key, value) in word_counter.items():
            if value > 1:
                continue
            unique_words[key].append(file)
print(unique_words)
