'''
Problem 32
==========
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Notes
=====
Essentially we want to find pairs of numbers that multiply to give us the missing numbers required to make a pandigital number and sum the products
Find a way to select pairs of numbers and evaluate if the string of numbers is equivalent to 123456789
by definition, the largest pandigital number would look like 98654321

'''



def pandigitalSum(n):

    # create pandigital number based on digits
    target = ''.join([str(i) for i in range(1, n+1, 1)])
    


pandigitalSum(5)



