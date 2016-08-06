the_count = [1, 2, 3, 4, 5]
names = ['huy', 'tuan', 'son', 'hai']
total = ['khanh', 1, 'nguyen', 2, 'khiem']

#this is the first kind of for-loop goes through a list
print "-"*50
for number in the_count:
	print " This is count %d" % number

#same as above

for name in names:
	print "A name of type: %s" % name
# also we can go through mixed lists too
for i in total:
	print " I got %r" % i

#we can also buil lists, first start with an empty one
elements = []


#-------------------------------------------------------
#ve range:
#cu phap ham range:
#range(stop):mac dinh so dau la 0
#range(start,stop): phan tu chay tu start den (Stop-1)
#rane(start,Stop,step): step la buoc nhay
#-------------------------------------------------------
for i in range(0, 6, 2):
	print "Adding %d to the list." % i
	#append is a function that list understand
	elements.append(i)
#now we can print them out too
for i in elements:
	print "elements was: %d" % i
print "-"*20

#co the truyen truc tiep ham range vao list elements

elements = range(0, 6, 2)
for i in elements:
	print "elements was: %d" % i

print "-"*50