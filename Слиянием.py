# способен сортировать огромные обьёмы данных
import random

n = 50
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
    
print('Not sorted: ')
print(arr)
print('----------')

############################################################    
# нужно две функции:

#    1я производит слияния
def merge(arrl, arrr ):#  принимает левый и правый список
    sorted_arr = list() # cоздаём пустой список
    current_left = 0
    current_right = 0
    
    # ищем длину левого и правого списка
    len_l = len(arrl)
    len_r = len(arrr)
    
    for i in range(len_l + len_r):
        if current_left < len_l and current_right < len_r:
            if arrl[current_left] < arrr[current_right]: # < для сортировки от меньшего к большему > для сортировки от большего к меньшему
                sorted_arr.append(arrl[current_left])
                current_left += 1
            else:
                sorted_arr.append(arrr[current_right])
                current_right += 1
        else:
            if current_left == len_l:
                for j in range(current_right, len_r):
                    sorted_arr.append(arrr[j])
            else:
                for j in range(current_left, len_l):
                    sorted_arr.append(arrl[j])       
            break
    return sorted_arr    


#    2я что бы отсортировать данным способом
def merge_sort(arr): # на вход подаётся список
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2 #находим середину списка
    left_side = list() # левая половина списка
    right_side = list() # правая половина списка
    
    #left_side = arr[:mid]
    for i in range(0, mid):
        val = arr[i]
        left_side.append(val) # добавляем значения в левый список
        
    #right_side = arr[mid]   
    for i in range(mid, len(arr)):
        val = arr[i]
        right_side.append(val) # добавляем значения в правый список
        
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    
    result = merge(left_side, right_side)
    return result
############################################################ 

arr = merge_sort(arr) # вызов функции
print('Sorted: ')
print(arr)
    