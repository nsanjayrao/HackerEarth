string=input().lower()
count_z=string.count('z')
count_o=string.count('o')
if 2 * count_z == count_o:
    print('Yes')
else:
    print('No')
