# need to edit this every time I add a new solution
import time

# solution to https://projecteuler.net/problem=32
from ProjecEuler.solutions.PandigitalProducts32 import pandigitalSum

def test_problem_32():
  start_time = time.time()
  pandigitalSum("123456789")
  
print("pandigitalSum finished in --- %s seconds ---" % (time.time() - start_time))
    
