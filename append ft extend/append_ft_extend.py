#su khac nhau giua append va extend
#append: xem doi tuong duoc them vao la 1 phan tu
#extend: them tung phan tu cua doi tuong them
#append: co the truyen bat cu doi tuong nao
#extend: chi nhan list



print "-"*50
print "append"
x= [1,2,3]
x.append([4,5])
print(x)
print " x[3]= ",
print x[3]

print "extend"
x= [1,2,3]
x.extend([4,5])
print " x[3]= ",
print x[3]
print(x)

print "-"*50