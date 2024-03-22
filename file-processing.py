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
            odd += 1
    print(f"There are {even} even numbers and {odd} odd numbers.")
    first = arr[0]
    #array [-1] same as arr[len(arr)-1]
    last = arr[-1]
    print(arr[2])

def process_csv():
#use underscores for file names
    with open(r"C:\Users\scott\OneDrive\Python\Coding Projects\US Stock Market Dataset.csv") as csvfile:
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
    twoFor()
    # process_csv(10)