from typing import List
from collections import Counter
import re

SPACE_RE = re.compile(r"[ \t]+")


def is_valid_permutation(src_a: str, src_b: str) -> bool:
    """
    Checks if src_a is simply a permutation of lines of src_b.

    Empty lines and identation are ignored.
    """
    return Counter(normalize(src_a)) == Counter(normalize(src_b))


def normalize(src: str) -> List[str]:
    """
    Normalize source code into a list of linwes.

    Empty lines and identation are removed.

    Example
    >>> normalize(" foo \n\n  bar  ")
    ["foo", "bar"]
    """
    lines = map(lambda x: SPACE_RE.sub("", x), src.splitlines())
    return [*filter(None, lines)]
