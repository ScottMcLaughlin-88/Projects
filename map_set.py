def map1():
    arr = ['a', 'a', 'c', 'c', 'b', 'b', 'd', 'e']
    counts = {}
    for i in arr:
        # Is 0 in get mean the value?
        counts[i] = counts.get(i, 0) + 1 #safe get, if the value isn't there, return none
        # if i in counts: #this is updating an entry
        #     
        # else: #creating an entry
        #     counts[i] = 1
        # I could solve this problem using for loops
        # loop 1, I would see how many unique values there are
        # Since there are 5 unique values: 
        # Loop 2, I would count all of a's, Loop 3 all the b's, etc.
        # in Total the map gives me for loop, without map.
        # There are 6 for loops worth of work.
    print(counts)
    print(len(counts))
    for key, value in counts.items():#what does the function items do?
        print(key, value)

#A set is, have I seen this?
#How many unique items are there?
#For a map, how many unique items are there?
#Have I seen this?
#I want to do more with each unique item.
#Such as, the specific counts of each item.
#And other statistics, such as average sum, etc.
#set = datastructure
#arrays
#maps
#sets

def set1():
    myset = set()
    arr = [1, 2, 3, 4, 5]
    for i in arr:
        myset.add(i)
    print(myset)

def set2():
    myset = set()
    promos = [1, 2, 3, 4, 5]
    for i in promos:
        myset.add(i)
    print(myset)
    new_promos = [5, 6, 7]
    for i in new_promos:
        if i in myset:
#This means we've seen this value
            print(f'Invalid promo {i}')
        else:
            print(f'Valid promo{i}')           
        myset.add(i)
    print(myset)

def set_count():
    arr = [1, 1, 3, 3, 3, 3, 5, 5, 5, 5, 4, 4, 4, 2]
    myset = set()
    for i in arr:
        myset.add(i)
    print(f'There were {len(myset)} unique attendees at the event.')
    count = 0
    for val in myset:
        print(f'One attendee id is: {val}')
        count += 1
    print(f'There were {count} unique attendees at the event.')
  



if __name__ == '__main__':
    map1()
    # set1()
    # set2()
    # set_count()