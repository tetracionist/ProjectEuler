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
from itertools import permutations

def pandigitalSum(n):
    # create permutations of pandigital number
    perms = list(permutations(n))

    #define a list to store the products
    products = [] 
    
    # with three digits there are six permutations we can make
    # within the created tuple we can use the commas to make the expression and the equals
    for perm in perms:

        # create left-hand and right-hand sides of the equation
        lhs_1 = int(perm[0]) * int(''.join(perm[1:5]))
        lhs_2 = int(''.join(perm[0:2])) * int(''.join(perm[2:5]))
        rhs = int(''.join(perm[5:9]))

        if (lhs_1 == rhs) or (lhs_2 == rhs) and rhs not in products:
            products.append(rhs)
 

    return sum(products)
    