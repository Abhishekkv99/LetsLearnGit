# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def binary_search(arr,key,low,high):
    
    if low>high:
        return -1
    
    mid = low + ((high-low)//2)  
    
    
    if arr[mid] == key:
        
        return mid
    elif key<arr[mid]: 
        
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)
        
        
a=[2,4,5,6,7,8,9]

b=binary_search(a, 9, 0, 6)
print("The result is"+b)