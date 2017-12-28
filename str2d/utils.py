"""General string parsing and manipulation functions"""
import random
import operator


def chunk(s, n):
    return map(''.join, zip(*(s[i::n] for i in range(n))))


def shuffle(s, seed=None):
    random.seed(seed)
    l = list(s)
    random.shuffle(l)
    return ''.join(l)


def mask(inp, msk, char=' ', replace=None, invert=False):
    op = operator.ne if invert else operator.eq
    return ''.join(
        s if op(m, char) else (replace or m)
        for s, m in zip(inp, msk)
    )
