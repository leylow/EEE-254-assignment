# Using functions in programming is important because they:
# Promote Code Reusability – Once a function is written, it can be reused multiple times without rewriting the same code.
#Improve Readability and Organization – Functions break the program into smaller chunks, making it easier to understand and debug.
#Support Modularity – Each function can be tested and maintained independently.
#Reduce Errors – Since a function performs a specific task, it reduces chances of mistakes when used repeatedly.
#Make Collaboration Easier – Developers can work on different functions independently without interfering with one another.


"""Return the nth root of x."""
def nth_root(x, n):
    
    return x ** (1 / n)


number = 27
root = 3
result = nth_root(number, root)
print(f"The {root}rd root of {number} is {result}")



"""Calculate Euclidean distance between two points (x1, y1) and (x2, y2)."""

import math

def euclidean_distance(x1, y1, x2, y2):
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


point1 = (3, 4)
point2 = (7, 1)
distance = euclidean_distance(*point1, *point2)
print(f"The distance between {point1} and {point2} is {distance}")
