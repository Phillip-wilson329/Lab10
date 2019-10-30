def backwardslist(array):
    return array.reverse()
    """ Takes in a list and returns the list backwards"""


def min(array):
    mini = array[0]
    for i in array:
        if mini > array[i]:
            mini = array[i]
            return mini
    """ Returns the lowest number in an list of numbers"""


def firsthalfsum(array):
    sum = 0
    if len(array) % 2 == 1:
        middle_num = (len(array) / 2.0) + 0.5
        sum = (array[middle_num] / 2)
    for i in range(0 , middle_num):
        sum = sum + array[i]
    return sum

    """Returns the sum of the first half of the list.
        ***IF THE LIST HAS AN ODD NUMBER OF ELEMENTS, split the middle element in
        half and add it to the sum.
        """


def divisibleby(array, divisor):
    """ Returns each element divisible by the paramater 'divisor'
    """


def max(array):
    """ Returns the highest number in a list of numbers """


def avg(array):
    """ Returns the average of a list of numbers"""


def suprise():
    """ Create a surprise function for the person that receives your code.
        Feel free to get creative change parameters, print out shapes,  etc.

        """

def gcd(array):
    """ Returns the greatest common Divisor of a list of numbers """
    """ Greatest Common Divisor is the greatest number that each number in the list is 
        divisible by. 
        EXAMPLE: [500, 50, 20] Greatest Common Divisor = 10
                 [18, 30, 42]  Greatest Common Divisor = 6
                 [33, 66, 99, 101] Greatest Common Divisor = 1

                 """



