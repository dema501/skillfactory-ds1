#num_1 = int(input())
#num_2 = int(input())
num_1 = 1812
num_2 = 2500
for i in range(max(num_1,num_2), 1, -1):
    if num_2%i == 0 and num_1%i == 0:
        print(i)
        break