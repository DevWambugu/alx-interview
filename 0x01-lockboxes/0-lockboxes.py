#!/usr/bin/python3

'''This function determines
if all boxes can be opended'''
def canUnlockAll(boxes):
    '''Determines if all boxes can be opened'''
    listLength = len(boxes)
    for box in range (len(boxes)):
        boxLength = len(boxes[box])
        box_opened = True
        for count in range (boxLength):
            key = boxes[box][count]
            key_found = False
            for i in range(listLength - 1):
              if key in boxes[i + 1]:
                 key_found = True
                 break
            if not key_found:
              box_opened = False
              break
        if not box_opened:
            return False
    return True
