def main():

    with open('source_data.txt', 'r', encoding='utf8') as f:
        data = (list(f.read().split('\n')))

    name = data[0]
    id = int(data[1])

    name_without_space = name.replace(' ', '')     
    name_div_id = int(id / len(name_without_space))    
    unicode_array = []
    for char in name_without_space:
        unicode_char = ord(char)    
        unicode_array.append(unicode_char)      
    

    if name_div_id % 2 == 0:
        dirrection = 'по возрастанию'
        number = 'чётное'
        soreted_arr = bubble_sort(unicode_array)
        soreted_arr_2 = selection_sort(unicode_array)
    else:
       dirrection = 'по убыванию'
       number = 'не чётное'
       soreted_arr = bubble_sort(unicode_array, False)
       soreted_arr_2 = selection_sort(unicode_array, False)  

    
    arithmetic = arithmetic_mean(unicode_array)
    quadratic = quadratic_mean(unicode_array)

    with open("result.txt", 'w', encoding='utf8') as f:
        f.write(f"""1. Исходные данные: {name}; ID: {id} 
2. {name_div_id}
3. Направление сортировки: {dirrection}, так как число {name_div_id} - {number}
4. Набор данных: {unicode_array}
5. Отсортированный {dirrection} набор данных {soreted_arr}
6. Среднее арифметическое значение: {arithmetic}
7. Среднее квадратическое значение: {quadratic}""")
       

# алгоритм сортировки по методу пузырька
def bubble_sort(array, direction=True):
    n = len(array)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            if not direction:
                if array[j] < array[j+1]:                
                    array[j], array[j+1] = array[j+1], array[j]
            else:
                if array[j] > array[j+1]:                
                    array[j], array[j+1] = array[j+1], array[j]   
       
    return array

# алгоритм сортировки методом выборки
def selection_sort(array, direction=True):   
    for i in range(len(array)):       
        first_value = i        
        for j in range(i + 1, len(array)):
            if not direction:
                if array[j] > array[first_value]:
                    first_value = j
            else:
                 if array[j] < array[first_value]:
                    first_value = j       
        array[i], array[first_value] = array[first_value], array[i]
    
    return array

def arithmetic_mean(array):
    sum = 0
    for i in array:
         sum += i
    result = sum / len(array)    
    return round(result, 3)

def quadratic_mean(array):
    sum = 0
    for i in array:
        sum += i**2
    result =  (sum / len(array))**(1/2)
    return round(result, 3)

if __name__ == '__main__':
    main()