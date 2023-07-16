# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:23:32 2023

@author: ruhul
"""

def maxValue(arr,low,high):
    l = len(arr)
    
    mid = low + ((high-low)//2)
    if mid == l-1 :
        return mid
    print(mid)
    if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
        return mid
    elif arr[mid]>arr[mid+1] and arr[mid]<arr[mid-1]:
        return maxValue(arr, low, mid-1)
    elif arr[mid]<arr[mid+1]:
        return maxValue(arr, mid+1, high)
    
    
a= [6,9,15,25,35,50,41,29,23,8]

b= [6,9,15,25,35]

c= [35,50]

l=len(a)
f=maxValue(a, 0, l-1)
a[f]