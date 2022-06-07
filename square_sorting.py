def insert_sort(var_list=[]):
    """implements list sort by insert method"""
    for i in range(1, len(var_list)):
        for j in range(i, 0, -1):
            if var_list[j] < var_list[j-1]:
                var_list[j], var_list[j-1] = var_list[j-1], var_list[j]
            else: break

def choice_sort(var_list=[]):
    """implements list sort by choice method"""
    for i in range(len(var_list)):
        for j in range(i, len(var_list)):
            if var_list[j] < var_list[i]:
                var_list[j], var_list[i] = var_list[i], var_list[j]
                
def bubble_sort(var_list=[]):
    """implements list sort by bubble method"""
    for i in range(len(var_list)):
        for j in range(len(var_list)-i-1):
            if var_list[j] > var_list[j+1]:
                var_list[j], var_list[j+1] = var_list[j+1], var_list[j]
