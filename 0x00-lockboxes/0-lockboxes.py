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
    """ Returns True if all boxes can be opened"""
    # Create start list of keys
    keyList = [0]

    # Copy list of keys to new list
    testkeyList = keyList[0]

    # run through all keys in boxes
    for key in keyList:
        # run through all keys in boxes
        for box in boxes:
            # if key is in box
            if key in box:
                # add key to testkeyList
                testkeyList.append(key)
                # remove key from box
                box.remove(key)
    # if testkeyList is same as keyList
    if len(keyList) == len(testkeyList):
        return True
    else:
        return False
