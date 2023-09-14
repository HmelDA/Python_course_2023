from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    element_counts = defaultdict(int)
    for element in inp:
        element_counts[element] += 1
    most_common_element = max(element_counts, key=element_counts.get)
    least_common_element = min(element_counts, key=element_counts.get)
    return most_common_element, least_common_element
