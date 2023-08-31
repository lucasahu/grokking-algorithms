#Simple function that prints every item on a list
#O(n)

def print_items(list):
    for item in list:
        print(item)

print(print_items([1, 2, 3, 4]))

#Same function but now it sleeps for 1 second
#Also O(n) but slower in practice

from time import sleep
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)

print(print_items2([1, 2, 3, 4]))