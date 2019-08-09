import string

from functools import reduce


def mapper(s):
    return string.ascii_lowercase.index(s.lower()) + 1


def mini_score(value):
    score_ = reduce(lambda x, y: x + y, [int(i) for i in str(value)])
    if len(str(score_)) == 1:
        return score_
    else:
        return mini_score(score_)

def score(name):
    name = name.translate({ord(c): None for c in string.whitespace})
    mapped_name = sum(list(map(mapper, name)))
    return mini_score(mapped_name)
