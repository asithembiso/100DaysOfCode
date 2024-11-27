"""
Merge two dictionaries
"""
from typing import Dict


def merge(dict1: Dict, dict2: Dict) -> Dict:
    return dict1 | dict2


if __name__ == "__main__":
    mydict1 = {'x': 1, 'z': 3}
    mydict2 = {'y': 2}
    print(merge(mydict1, mydict2))
