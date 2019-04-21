def split_and_join(line):
   #print(line)
   n=line.split(" ")
   m="-".join(n)

   #print(n)
   #print(m)
   return m
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
