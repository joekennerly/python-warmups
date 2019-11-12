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
