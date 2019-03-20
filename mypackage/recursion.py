def sum_array(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-2) + fibonacci(n-1))

def reverse(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse(word[:-1])



def factorial(n):

    '''Return n!'''
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
