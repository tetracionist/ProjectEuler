# need to edit this every time I add a new solution
from time import time
import os

# solution to https://projecteuler.net/problem=32
from solutions.PandigitalProducts import pandigitalSum
start_time = time()

def test_problem_32():
  assert pandigitalSum("123456789") == os.environ['SOLUTION_32']
  
print("pandigitalSum finished in --- %s seconds ---" % (time() - start_time))
    
