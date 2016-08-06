#---------------------------------
#cau truc cua lenh if
#if (dieu_kien) :
#	cau lenh neu dieu kien dung
#(note: chu y su thut dong)
#vi du
#---------------------------------
print "-"*50
print " so sanh 2 so a va b:"
a=raw_input("Nhap a:")
b=raw_input("Nhap b:")
if a>b:
	print " %s lon hon %s" % (a,b)
if a<b:
	print " %s nho hon %s" % (a,b)
if a == b:
    print " %s bang %s" % (a,b)
print "-"*50