import utils


#method 1
utils.greet("DSCI510")

#method 2
from utils import greet

greet("DSCI510")

#method 3
import utils as ut

ut.farewell("DSCI510")

#method 4
from utils import farewell as goodbye
goodbye("lab again")

#import from a subdirectory
#method 1 - not preferred sys.path

# import sys
# sys.path.append("./helpers_1")
# from tool_1 import add
# print(add(1,2))

#method 2 - blank __init__.py file
from helpers_2.tool_2 import multiply
print(multiply(5,2))

#also do
from helpers_2 import tool_2
print(tool_2.multiply(20,3))



#show directory using os

import os
print(os.path.dirname(__file__))





if __name__ == "__main__":
    print(f"Running {__file__}, name = {__name__}")
else:
    print(f"{__file__} is being imported, name = {__name__}")

