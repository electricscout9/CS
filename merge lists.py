def merge_lists(list1, list2):
    merged_list = []
    while list1 and list2:
        if list1[0] > list2[0]:
            merged_list.append(list2.pop(0))
        else:
            merged_list.append(list1.pop(0))
    if list1:
        merged_list.append(list1.pop(0))
    if list2:
        merged_list.append(list2.pop(0))
    return(merged_list)

def merge_sort(list1):
    result1 = [list1]
    result2 = []
    x = 0
    while len(result2) < len(list1) and len(result1) < len(list1):
        if x%2==0:
            result2 = []
            while result1:
                temp = result1.pop(0)
                
                if temp[:len(temp)//2]:
                    result2.append(temp[:len(temp)//2])
                if temp[len(temp)//2:]:
                    result2.append(temp[len(temp)//2:])

        else:
            result1 = []
            while result2:
                temp = result2.pop(0)
                
                if temp[:len(temp)//2]:
                    result1.append(temp[:len(temp)//2])
                if temp[len(temp)//2:]:
                    result1.append(temp[len(temp)//2:])

        x+=1
    
    if result2:
        result1 = result2
        result2 = []
    x = 0
    while not ((len(result1) == 0 and len(result2) == 1) or  (len(result2) == 0 and len(result1) == 1)):
        if x%2==0:
            while result1:

                if len(result1) != 1:
                    result2.append(merge_lists(result1.pop(0), result1.pop(0)))
                else:
                    result2.append(result1.pop(0))
        else:
            while result2:
                if len(result2) != 1:
                    result1.append(merge_lists(result2.pop(0), result2.pop(0)))
                else:
                    result1.append(result2.pop(0))

        x+=1
        
    if result2:
        result1 = result2
        result2 = []
    return result1
        
    
    
    
            
            
        


print(merge_sort([7,5,9,2,4,1,10]))