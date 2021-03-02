# -*- coding: utf-8 -*-
from enum import Enum
import math
class Strategy(Enum):
	LOWER    = "lower"
	HIGHER   = "higher"
	MIDPOINT = "midpoint"
	NEAREST  = "nearest"
	LINEAR   = "linear"


def my_name():
	return "SAAL_Fatma"

def my_min(arr: list):
    minValue=arr[0]
    if len(arr)==0:
        return None
    for i in range(len(arr)):
        if(arr[i]<minValue):
            minValue=arr[i]
    return minValue

def my_max(arr: list):
    maxValue=arr[0]
    if len(arr)==0:
        return None
    for i in range(len(arr)):
        if(arr[i]>maxValue):
            maxValue=arr[i]
    return maxValue


def decimales(f):
    if math.fabs(f - 0.0) > 1e-5:
        return f - math.floor(f)


def my_median(arr: list, strategy: Strategy):
    arr.sort()
    medianIndex=len(arr)//2
    if strategy == Strategy.LOWER:
        return (arr[medianIndex-1])
    elif strategy == Strategy.HIGHER:
        return arr[medianIndex]
    elif strategy == Strategy.MIDPOINT:
        return (arr[medianIndex-1]+arr[medianIndex])/2
    elif strategy == Strategy.NEAREST:
        m=len(arr)/2
        if(decimales(m)<0.50):
            return arr[round(m)-1]
        elif decimales(m)>0.50:
            return arr[round(m)]
        else:
            return (arr[round(m)-1],arr[round(m)])
    elif strategy == Strategy.LINEAR:
        return None    



def my_mean(arr: list, strategy: Strategy):
    somme=0
    nbElements=0
    for i in range(len(arr)):
        somme=somme+arr[i]
        nbElements=nbElements+1
    moyenne=somme/nbElements
    if strategy == Strategy.LOWER:
        return round(moyenne)
    elif strategy == Strategy.HIGHER:
        return round(moyenne)+1
    elif strategy == Strategy.MIDPOINT:
        return (round(moyenne)+1)+(round(moyenne))/2
    elif strategy == Strategy.NEAREST:
        if(decimales(moyenne)<0.5):
            return round(moyenne)
        elif(decimales(moyenne)>0.5):
            return round(moyenne)+1
        else:
            return (round(moyenne),round(moyenne)+1)

    
        
        


def my_quartile(n: int, arr: list, strategy: Strategy):
    arr.sort()
    Q1=len(arr)/4
    Q3=3*len(arr)/4
    if strategy == Strategy.LOWER:
        if n==1:
           return arr[round(Q1)-1]
        elif n==2:
           return my_median(arr, Strategy.LOWER)
        elif n==3:
            return arr[round(Q3)-1]
    
    elif strategy == Strategy.HIGHER:
        if n==1:
           return arr[round(Q1)]
        elif n==2:
           return my_median(arr, Strategy.HIGHER)
        elif n==3:
            return arr[round(Q3)]
    elif strategy == Strategy.MIDPOINT:
        if n==1:
           return (arr[round(Q1)]+arr[round(Q1)-1])/2
        elif n==2:
           return my_median(arr, Strategy.MIDPOINT)
        elif n==3:
            return (arr[round(Q3)]+arr[round(Q3)-1])/2
    elif strategy == Strategy.NEAREST:
        if n==1:
            if(decimales(Q1)<0.50):
                return arr[round(Q1)-1]
            elif decimales(Q1)>0.50:
                return arr[round(Q1)]
            else:
                return (arr[round(Q1)-1],arr[round(Q1)])
        elif n==2:
            return my_median(arr, Strategy.NEAREST)
        elif n==3:
            if(decimales(Q3)<0.50):
                return arr[round(Q3)-1]
            elif decimales(Q3)>0.50:
                return arr[round(Q3)]
            else:
                return (arr[round(Q3)-1],arr[round(Q3)])
        

    
        
    
def my_interquartile(arr: list, strategy: Strategy):
    arr.sort()        
    if strategy == Strategy.LOWER:
        q1= my_percentile(25, arr, Strategy.LOWER)
        q3= my_percentile(75, arr, Strategy.LOWER)
        return q3-q1
    elif strategy == Strategy.HIGHER:
        q1= my_percentile(25, arr, Strategy.HIGHER)
        q3= my_percentile(75, arr, Strategy.HIGHER)
        return q3-q1
    elif strategy == Strategy.MIDPOINT:
        q1= my_percentile(25, arr, Strategy.MIDPOINT)
        q3= my_percentile(75, arr, Strategy.MIDPOINT)
        return q3-q1
    elif strategy == Strategy.NEAREST:
        q1= my_percentile(25, arr, Strategy.NEAREST)
        q3= my_percentile(75, arr, Strategy.NEAREST)
        return q3-q1





def my_percentile(p: int, arr: list, strategy: Strategy):
    arr.sort()
    k=(p/100)*len(arr)
    f=decimales(k)
    print(f)
    n = p/100 * len(arr) + 0.5
    if strategy == Strategy.LOWER:
        return arr[round(n-1)]
    elif strategy == Strategy.HIGHER:
        return arr[round(n-1)+1]
    elif strategy == Strategy.MIDPOINT:
        return ((arr[round(n-1)])+(arr[round(n-1)]+1))/2
    elif strategy == Strategy.NEAREST:
        if decimales(n)<0.5:
            return arr[round(n-1)]
        elif decimales(n)>0.5 :
            return arr[round(n-1)]+1
        else:
            return (arr[round(n-1)],arr[round(n-1)]+1)
    elif strategy == Strategy.LINEAR:
        return ((arr[round(n-1)]+1)-(arr[round(n-1)]))/((round(n-1)+1)-round(n-1))
    


def count_nonzero(arr: list):
    cpt = 0
    for i in range(len(arr)):
        if(arr[i]!=0):
            cpt=cpt+1
    return cpt



def count_empty(arr: list):
    cpt = 0
    for i in range(len(arr)):
        if(arr[i]==None):
            cpt=cpt+1
    return cpt
