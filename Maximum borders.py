for i in range(int(input())):
    list_1=[]
    list_2=[]
    n,m=map(int,input().split())
    for i in range(n):
        string=input()
        list_1.append(string)
    for i in list_1:
        a=i.count('#')
        list_2.append(a)
    print(max(list_2))
