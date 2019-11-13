# 11/13/19 ------------------
"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N."""

def find_outlier(integers):

    # check whether the first two elems are both odd or even
    if integers[0] % 2 != integers[1] % 2:

        # if they have no parity, check which is wrong based off the third elem
        # return the first if the third does not match...
        if integers[2] % 2 == integers[1] % 2:
            return integers[0]

        # ...otherwise return the second
        else:
            return integers[1]

    # if all three have parity, loop through the list and compare each int based off the first elem
    for integer in integers:
        if integer % 2 != integers[0] % 2:
            return integer

integers = [2, 4, 6, 8, 10, 3] #should return 3
print(find_outlier(integers))











# 11/12/19 ------------------
"""Function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present."""
def spin_words(sentence):
    word_list = sentence.split(" ")

    new_list = []

    for word in word_list:
        if len(word) >=5:
            new_list.append(word[::-1])
        else:
            new_list.append(word)

    new_string = " ".join(new_list)
    print(new_string)

# spin_words('hello, my dearest friend')








# 11/11/19 ------------------
"""Function takes a list of integers and returns a formatted string"""
# My way
def phone_number(n):
    n.insert(0, "(")
    n.insert(4, ") ")
    n.insert(8, "-")
    string = "".join(str(num) for num in n)
    print(string)

# Better way
def better_phone_number(n):
    print('({}{}{}) {}{}{}-{}{}{}{}'.format(*n))

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# phone_number(number_list)
# better_phone_number(number_list)









# 11/10/19 ------------------
"""Function adds odd numbers based off of the number passed as arg"""
def sum_of_odd_nums(n):
    return n**3

# print(sum_of_odd_nums(1))
