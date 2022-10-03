
N = int(input())
data = [int(x) for x in input().split()]
string=''
for i in range(N):
    string+=str(data[i])[-1]
if int(string)%10==0:
    print('Yes')
else:
    print('No')
