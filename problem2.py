#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(a, b ,c):
    myList = [a, b ,c]
    a = max(myList)
    myList.remove(a)
    b = min(myList)
    myList.remove(b)
    c = myList[0]
    try:
        if a*a == b*b + c*c :
            number = 2
        if a*a > b*b + c*c:
            number = 3
        if a*a < b*b + c*c:
            number = 1
        if c + b < a: 
            number = 0
       
    except:
        number = 0

    return number

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
