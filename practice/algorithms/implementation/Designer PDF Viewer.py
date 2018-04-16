import sys
from functools import reduce
from io import StringIO


def designerPdfViewer(h, word):
    return len(word) * reduce(lambda x, y: max(x, h[ord(y) - ord('a')]), word, 0)


sys.stdin = StringIO("""1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
""")
while 1:
    try:
        h = list(map(int, input().strip().split(' ')))
        word = input().strip()
        result = designerPdfViewer(h, word)
        print(result)
    except EOFError:
        break
