#!/usr/bin/env checkio --domain=py run compress-list

# A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another, there is only one in the result Iterable (list, tuple, iterator ...).
# 
# 
# 
# Input:List.
# 
# Output:"Compressed" Iterable (list, tuple, iterator ...).
# 
# 
# END_DESC

from typing import Iterable


def compress(items: list) -> Iterable:
    if not items:
        return []
    
    result=[items[0]]
    
    for i in range(1,len(items)):
        if(items[i] != result[-1]):
            result.append(items[i])
    
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])) == [5, 4, 5, 6, 5, 7, 8, 0]
    assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
    print("Coding complete? Click 'Check' to earn cool rewards!")