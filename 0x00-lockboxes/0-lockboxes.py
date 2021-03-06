#!/usr/bin/python3

"""
__SUMMARY__
0 Lockboxes

You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes

Write a method that determines if all the boxes can be opened

Prototype: def canUnlockAll(boxes)
boxes is a list of lists

"""


def canUnlockAll(boxes):
    """
    The method will loop through the list of boxes
    and check if all the boxes can be opened
    """
    keyset = {0}

    for key in boxes[0]:
        if (0 <= key < len(boxes)) and key not in keyset:
            boxes[0].extend(boxes[key])
            keyset.add(key)

    # print(keyset)
    return len(keyset) == len(boxes)
