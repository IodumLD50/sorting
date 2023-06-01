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

'''
for i in range(n - 1):
    index_sorted = i # изначально он равет i
    next_index = i + 1 # следующий элемент
    for j in range(next_index, n, 1): # от следущего элемента до конца списка с шагом 1
        # Ищем максимальный элемент и вставляем его в начало списка
'''        
for i in range(n - 1): # Что бы не выйти за границы списка 'n - 1'
    min_max_index = i # текущий индекс 'Мой текущий элемент самый маленький (большой)'
    for j in range(i + 1, n, +1): # старт со следущего элемента 'i + 1'
        if arr[j] < arr[min_max_index]: # < сортировка от меньшего значения к большему. > сортировка от большего значения к меньшему
            min_max_index = j
    # В конце поменять местами
    temp = arr[i]
    arr[i] = arr[min_max_index]
    arr[min_max_index] = temp
    #print(arr)   

############################################################ 

print('Sorted: ')
print(arr)
    