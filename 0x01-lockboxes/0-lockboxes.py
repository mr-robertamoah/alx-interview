#!/usr/bin/python3

'''
a function which checkes if all boxes in a list of boxes
can be unlocked
'''

def canUnlockAll(boxes):
    '''
    boxes: list of lists
    '''

    def getBoxKeys(keys, boxes, gottenKeys):
        '''
        keys: list of current box
        boxes: list of lists
        gottenKeys: set of keys of unlocked boxes
        '''

        for key in keys:
            if key < len(boxes) and key not in gottenKeys:
                gottenKeys.add(key)
                getBoxKeys(boxes[key], boxes, gottenKeys)

    gottenKeys = set()
    gottenKeys.add(0)

    getBoxKeys(boxes[0], boxes, gottenKeys)

    return len(gottenKeys) == len(boxes)
