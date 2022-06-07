def insert_sort(list=[]):
    """implements list sort by insert method"""
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else: break
print('hoba')
