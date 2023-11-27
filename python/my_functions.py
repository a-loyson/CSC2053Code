#Abigail Loyson

def even_nums(nums):
    """
    given a list of numbers, returns number of even numbers in the list
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count

def rev_string(string):
    """
    given a string, return string in reversed order
    """
    string_new = ""
    for l in range(len(string)-1,-1,-1):
        string_new = string_new + string[l]
    return string_new

#Test Functions

list_t = [1,2,6,11,35,12,5]
print(even_nums(list_t))
list_t2 = [1,3,5,7,9]
print(even_nums(list_t2))
list_t3 = [20,40,60,80,100]
print(even_nums(list_t3))

string_t = "hi there!"
print(rev_string(string_t))
string_t2 = "this is a really good function"
print(rev_string(string_t2))
string_t3 = "racecar"
print(rev_string(string_t3))