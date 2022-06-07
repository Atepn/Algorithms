def shift_to_left(list=[], shift=0):
    """implements shift of list elements to left"""
    if shift <= 0 or len(list)<2:
        return
    for i in range(shift):
        tmp = list[0]
        for j in range(len(list)-1):
            list[j] = list[j+1]
        list[len(list)-1] = tmp

def shift_to_right(list=[], shift=0):
    """implements shift of list elements to right"""
    if shift <= 0 or len(list)<2:
        return
    for i in range(shift):
        tmp = list[len(list)-1]
        for j in range(len(list)-1, 0, -1):
            list[j] = list[j-1]
        list[0] = tmp