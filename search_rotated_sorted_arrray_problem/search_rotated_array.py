def binary_search(input_list, number, start_index, end_index):
    
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index) // 2
    mid_item = input_list[mid_index]
    if mid_item == number:
        return mid_index
    
    elif number < mid_item:
        return binary_search(input_list, number, start_index, mid_index-1)
    
    elif number > mid_item:
        return binary_search(input_list, number,mid_index+1, end_index)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    start_index= 0
    end_index = len(input_list)-1
    mid_index = (start_index + end_index)//2
    if number == input_list[mid_index]:
        return mid_index
    
    # applying binary search on the left side of the mid 
    number_index = binary_search(input_list, number, start_index, mid_index-1)

    if number_index!=-1:
        return number_index
    else:
        # applying binary search on the right side of the mid 
        return binary_search(input_list, number, mid_index+1, end_index)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    linear_search_output = linear_search(input_list, number)
    rotated_array_output = rotated_array_search(input_list, number)
    #print(rotated_array_output)
    if linear_search_output == rotated_array_output:
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[8,9,11,5,6,7], 7])
test_function([[8,9,11,5,6,7], 5])
test_function([[], 1])