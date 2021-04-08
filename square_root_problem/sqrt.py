def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 2:
        return number
    
    left = 0
    right = number
    
    while left<right:
        mid = (left + right) // 2
        square = mid*mid
        
        if square == number:
            return mid
        
        elif square < number:
            left = mid + 1
            
        else:
            right = mid
           
    return left-1 
            

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(196)) else "Fail")

