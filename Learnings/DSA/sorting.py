list_sort_org = [1, 4, 2, 3, 9, 6, 5, 8, 7]
list_length = len(list_sort_org)

def bubbleSort(list_sort):
    interchanged = True
    while interchanged:
        for i in range(list_length-1):
            if (list_sort[i] > list_sort[i+1]):
                list_sort[i+1], list_sort[i] = list_sort[i] ,  list_sort[i+1]
                interchanged = False
    return list_sort

def selectionSort(list_sort):
    pivot = 0
    min = 0
    while (pivot < list_length):
        min = pivot 
        for i in range(pivot, list_length):
            if list_sort[min] > list_sort[i]:
                min =  i
        list_sort[pivot], list_sort[min] = list_sort[min], list_sort[pivot]
        pivot += 1
    return list_sort

#print(selectionSort(list_sort_org))
#print(bubbleSort(list_sort_org))