"""
cpp : a == b ? "123" : "456"

"""

def isSmaller(a, b):
    print(a, "is smaller than", b)

def isBigger(a, b):
    print(a, "is bigger than", b)

a , b = 100, 50

""" Case1 : both function will be called """
"""
100 is smaller than 50
100 is bigger than 50
"""
#x = {True: isSmaller(a, b), False: isBigger(a, b)}[a < b]

""" Case2 : work as except """
"""
100 is bigger than 50
"""
#isSmaller(a, b) if a < b else isBigger(a, b)

""" Case3 """
"""
Both will be executed
456
"""
#x = (isSmaller(a, b), isBigger(a, b))[bool(a < b)]
# (falseValue, trueValue)[bool(<expression>)]
x = ("123", "456")[bool(a > b)]
print(x)


