import sys, re
from collections import Counter

# === Task1. 문서를 입력받아 자주 등장하는 단어 1000개를 자주 등장하는 순서대로 출력하는 python 프로그램 작성하기 ===

# 방법1
Word_Counter = Counter({})
for line in sys.stdin:
    Word_Counter.update(re.findall("[a-z0-9]+", line.lower()))

for word in Word_Counter.most_common(1000):
    print('%s\t%d' %(word[0], word[1]))

'''
# 방법2
wc = Counter(match.group() for line in sys.stdin for match in re.finditer("[a-z0-9]+", line.lower()))

for w, c in wc.most_common(1000):
    print(f"{w}\t{c}")
'''