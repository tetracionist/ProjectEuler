'''A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
from time import time
start_time = time()

sequence_length = 0


# start with a for loop to iterate through all the numbers from 2 to 1000
for i in range(2, 1001, 1):

    foundRemainders = [0]*1000
    foundRemainders[0] = i
    value = 1
    position = 0

    # do until the remainder is 0
    while(value != 0 and foundRemainders[value] == 0):
        foundRemainders[value] = position
        value *= 10
        value %= i
        position += 1
    
    if position - foundRemainders[value] > sequence_length:
        sequence_length = position - foundRemainders[value]
        solution = i
    
print(solution, sequence_length)
print("Reciprocal cycles finished in --- %s seconds ---" % (time() - start_time))
    

