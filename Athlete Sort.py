#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    #print(arr)

    for i in range(n-1,0,-1):
        for j in range(i):
            if(arr[j][k]>arr[j+1][k]):
                temp=arr[j][k]
                arr[j][k]=arr[j+1][k]
                arr[j+1][k]=temp

                for p in range (0,k):
                    temp=arr[j][p]
                    arr[j][p]=arr[j+1][p]
                    arr[j+1][p]=temp
                for q in range(k+1,m):
                    temp=arr[j][q]
                    arr[j][q]=arr[j+1][q]
                    arr[j+1][q]=temp

            


for i in range (0,n):
    for j in range(0,m):
        print (arr[i][j], end=" ")
    print("")
    
