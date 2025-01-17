import csv
'''
Process CSV files line by line
'''
def array_practice(arr):
    print(f"The length is {len(arr)}")
    even = 0
    odd = 0
    for val in arr:
        if val % 2 == 0:
            even += 1
        else:

test
            odd += 1
    print(f"There are {even} even numbers and {odd} odd numbers.")
    first = arr[0]
    #array [-1] same as arr[len(arr)-1]
    last = arr[-1]
    print(arr[2])

def process_csv():
#use underscores for file names
    with open(r"C:\Users\scott\OneDrive\Python\Projects\dataset.csv") as csvfile:
        lines=csv.reader(csvfile)
        data = list(csv.reader(csvfile))
        print("rows:", len(data))
        print("columns:", len(data[0]))
   
        print(csvfile)
        #i stands for index in a loop
        # i = 0
        # for line in lines:
        #     print(len(line))
        #     i += 1
        #     if i > num_lines:
        #         break


def practice():
    a = [1, 3, 5]
    len(a)
    b = a[0]
    l = [[2, 4, 6],
         [10,20,30]]
    c = len(l)
    cc = len(l[0])
    t = a[1]
    find = l[1] #[10,20,30]
    d = find[1]
    e = l[1][1]

def array_range(arr):#get smallest and largest elemnts of array
    print(f"Before sorting: {arr}")
    arr.sort()
    print(arr)
    small_list = arr[0]
    print(f"Small list: {small_list}")
    large_list = arr[-1]
    large_list2 = arr[len(arr)-1]#Used for general programming languages
    print(large_list, large_list2)

def array_range_python(arr):
    small = min(arr)
    large = max(arr)
    print(small,large)#Standard way to find small value is to initialize to a very large value, and then look for the smal l value.
    #Standard way to find large value is to initialize to a very small value, then look for large value

def array_range_for(arr):
    small = float('inf')
    large = float('-inf')
    for val in arr:
        if val < small:
            small = val
        if val > large:
            large = val
    return small, large

#two types of arrays.  even and odd ones.
def med_arr(arr):
    arr.sort()
    print(arr)
    arr_length = len(arr)
    if is_even(arr_length):
#5/2 -> 2.5(leaves decimal), 5//2 2 (chops off all decimals)
#[4,6,8,10], med[1,2]
#half_len The length of the array // 2
#close_len = half_len // 2
#[4,6,8,10,13,15], med[2,3]
#half_len = length of the // 2 = 6 // 2 = 3
#close_len = half_len - 1
        half_len  = arr_length // 2
        close_len = half_len - 1
        med_sum = arr[half_len] + arr[close_len]
        return med_sum / 2
    else:
        med_index = arr_length // 2 #5 -> 2
        return arr[med_index]


        
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def div_practice():
    odd = 5
    even = 4
    print(f"The even result is {even // 2}")
    print(f"The odd result is {odd // 2}")    
    print(f"The odd result is {odd / 2}")#single division is w/ float.  // int is not.

def array_practice():
    arr = [1,10,-10,2,3,4,5,-15,-3]
    count = 0
    total = 0
    for val in arr:
        if val >= 2:
            total += val
            count += 1
    avg = total / count
    print(f"Total is {total}")
    print(f"The average is {avg}")
    python_total = sum(arr)
    python_average = python_total / len(arr)
    print(f"The Python average is {python_average}")

def swap_practice():
    a = 1
    b = 2
    temp = b
#place one variable in memory, do the swap
    b = a
    a = temp
    print(f"a = {a} and b = {b}")

def arr_swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    
def reverse_arr(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        arr_swap(arr,i,j)
        print(arr)
        i += 1
        j -= 1

def review():
    a = [[1,5],
         [5,10]]
    d = a[1][1]
    print(d)

def twoFor():
    nums = [10,20,30,35,40]
    for value in nums:
        print(value)
    for i in range(len(nums)):
        print(nums[i])
    
if __name__ == '__main__':
    # array_practice([1,56,3,324,89,100])
    # process_csv()
    # review()
    arr = [-5, 3, -2, 10, -21]#makes array more dynamic because we can use it for any array
    # array_range(arr)
    # array_practice()
    arr1 = [4, 2, 1, 3]
    arr2 = [1, 3, 2, 4, 5]
    med_2 = med_arr([4,6,8,10,13,15])
    print(med_2)
#when we are calling a function in main, how do we know what variables to call in ()
    # swap_practice()
    # arr_swap(arr, 0, 1)
    reverse_arr(arr)
    print(arr)
    # array_range_python(arr)
    # small, large = array_range_for(arr)
    # print(small,large)
    # process_csv(10)