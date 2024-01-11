#!/usr/bin/python3

'''This function determines
if all boxes can be opended'''


def canUnlockAll(boxes):
    '''Determines if all boxes can be opened'''
    open_boxes = set()
    open_boxes.add(0)
    keys_to_be_checked = boxes[0]
    while keys_to_be_checked:
        key = keys_to_be_checked.pop()
        if 0 <= key < len(boxes) and key not in open_boxes:
            open_boxes.add(key)
            keys_to_be_checked.extend(boxes[key])
    return len(open_boxes) == len(boxes)
