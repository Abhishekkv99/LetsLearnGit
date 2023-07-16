# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:04:06 2023

@author: ruhul
"""

def pivot(arr,low,high):
    
    mid = low + ((high-low)//2)
    l = len(arr)
    if arr[low]<arr[high]:
        
        return high
    
    
    
    if arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid]<arr[high]:
        return pivot(arr,low,mid-1)
    elif arr[mid]>arr[high]:
        return pivot(arr, mid+1, high)
    
    
    
    
    
a = [10,7,8,9,9]


p=pivot(a,0,len(a)-1)

print(p)
    
    
    
