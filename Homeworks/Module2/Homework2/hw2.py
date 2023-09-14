from typing import Dict, List


def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    new_format_data = dict()
    for score, letters in legacy_data.items():
        for letter in letters:
            new_format_data[letter.lower()] = score
    return new_format_data
