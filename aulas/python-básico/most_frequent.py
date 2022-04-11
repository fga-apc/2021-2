def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    freqs = {}
    for s in data:
        for c in s:
            freqs[c] = freqs.get(c, 0) + 1
    key_fn = freqs.get
    return max(freqs.keys(), key=key_fn)


print(most_frequent(["foo", "bar", "baz", "foo", "foo", "bar"]))
