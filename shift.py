n=int(input())
List = list(map(int,input().split()))
result = 0
for digits in List:
  result = (result << 1) | digits
print (str(result))
