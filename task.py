import sys
import math

# Provides the overall memory consumption of a list of processes at a given time
def overall_mem_consuption(t, lst):
    return sum(t/v for v in lst)

# binary search for the time when the process will die
def time_binary_search(arr, low, high, lst, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if overall_mem_consuption(arr[mid], lst) == x or (overall_mem_consuption(arr[mid], lst) > x and overall_mem_consuption(arr[mid-1], lst) < x):
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif sum(arr[mid]/v for v in lst) > x:
            return time_binary_search(arr, low, mid - 1, lst, x)
        # Else the element can only be present in right subarray
        else:
            return time_binary_search(arr, mid + 1, high, lst, x)
    else:
        # Element is not present in the array
        return -1

# searchs for the time when the process will die
def timetodie(lst, x):
    start = math.floor(x / sum(1/v for v in lst))
    if (x * min(lst))+1 > sys.maxsize:
        end = start + sys.maxsize-1
    else :    
        end = (x * min(lst))+1
    arr = range(start, end)
    # print(arr)
    try:
        seconds_to_meltdown = arr[time_binary_search(arr, 0, len(arr)-1, lst, x)]
    except OverflowError:
        error = OverflowError.with_traceback(None)
        return error
    return seconds_to_meltdown

def main():
    for line in sys.stdin:  
        input = [int(x) for x in line.split(' ')]
        print(timetodie(input[1:], input[0]))
  

if __name__=="__main__":
    main()