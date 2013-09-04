# Write a function `bubble_sort(arr)` which will sort an array of
# integers using the "bubble sort"
# methodology. (http://en.wikipedia.org/wiki/Bubble_sort)

def bubble_sort(arr):
    answer = arr
    swapped = True
    while swapped == True:
        swapped = False
        for number in range(len(answer)-1):
            if answer[number] > answer[number+1]:
                answer[number], answer[number+1] = answer[number+1], answer[number]
                swapped = True
    return answer









