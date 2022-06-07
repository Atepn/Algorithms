def insert_sort(list=[]):
    """implements list sort by insert method"""
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else: break
A=[1,4,5,2,5,6,7,2,4,3,6,5]
insert_sort(A)
print(A)
A=[1,4,0,2,5,0,0,0,4,3,6,5]
insert_sort(A)
print(A)
A=[1,4,5,2,-5,6,7,-2,-4,-3,6,-5]
insert_sort(A)
print(A)