def average(array):
    # your code goes here
    
    m=len(set(array))
    z=sum(set(array))
    y=z/m
  
    return y


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
