import random
# в лучшем варианте сортирует быстро а в худшем не быстрее чем пузырьком
n = 50
arr = []
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
    
print('Not sorted: ')
print(arr)
print('----------')

############################################################    
# быстрая сортировка это рекрусиыная сортировка и по этому нам нужна функция
def quick_sort(arr):
    # Точка выхода
    if len(arr) <= 1:
         return arr
    
    # отпределяем опорный эелемент и всё что меньше его в левую часть, а всё что больше в правую и то что равно ему в среднию часть
    index_of_strong_elem = random.randint(0, len(arr) - 1)
    strong_elm = arr[index_of_strong_elem]
   
    low = []   # список всего что меньше 
    mid = []  # список всего что равно
    high = []   # cписок всего что больше
    
    # проходимся по всему списку
    for elem in arr:
        if elem == strong_elm:
            mid.append(elem)
        elif elem < strong_elm: # < от меньшего к большему > от большего к меньшему
            low.append(elem)
        else:
            high.append(elem) 
          
    low = quick_sort(low)
    high = quick_sort(high)          
    result = low + mid + high
    return result


############################################################ 
arr = quick_sort(arr)
print('Sorted: ')
print(arr)
    