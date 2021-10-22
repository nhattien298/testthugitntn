# X = [1,2,3,4,5]
# Gio co cach nao lay tong cung 345 k man
x=[1,2,3,4,5]
ketqua=0
dodai = len(x)
for i in range(dodai):
    if i>=2:
        ketqua+=x[i]
print(ketqua)