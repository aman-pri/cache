# n-way mapping
#each memory block maps with 1 cache line
# size of block is same


import math 
#helper function for converting decimal to binary
def tobin(n):  
    return bin(n).replace("0b", "")  


#Main memory array
memorindeces=[]
memoryblocks=[]

#Cache memorty lidt
cache=[]
cacheline=[]
addcacheline=[]
#list for tag entries
tag=[]

MS=int(input("Input Memory size"))
BS=int(input("Input Block size"))
NB=(MS/BS)
#bits req for address of blocks 
BI=(math.log(NB, 2))
print("Number of bits for block indeces= "+str(BI))
CS=int(input("Input Cache Size"))
CL=CS/BS
CI=(math.log(CS, 2))


K=int(input("ENTER K FOR K-WAY ASSOCIATIVE MAPPING"))
numberofsets=CL/K
print("NUMBER OF SETS FORMED= "+str(numberofsets))
setbits=math.log(numberofsets, 2)
print("NUMBER OF BITS REQUIRED FOR REPRESENTING SETS= "+str(setbits))


CLI=(math.log(CL, 2))
print("Number of cache lines= "+str(CL))
print("Number of bits for cache line indeces: "+str(CLI))
tb=BI-CLI
filler=int(BI) 
print(filler)
# print("Number of bits required for tag bits: "+str(tb))
print("\n\n\tMAIN MENORY\n\n")
for i in range (0,int(NB)):
	add=str(tobin(i))
	diff=filler-len(add)
	filled=(diff*"0")+add
	#filled=add.zfill(filler)
	memorindeces.append(filled)
	blockid=" B"+str(i)
	memoryblocks.append(blockid)
	print(filled+" "+blockid)

sets=K
setarray=[]
print("\n\n")
for q in range(0, int(numberofsets)):
	for w in range(0, int(sets)):
		d=int(setbits)-len(tobin(q))
		filled=("0"*d)+str(tobin(q))
		setarray.append(filled)
	q=q+2

print(setarray)
flaglen=len(setarray)
flag=[]

for i in range(0, flaglen):
    flag.append(0)

#print(flag)

#print("1. ADD TO CACHE\n2. SEARCH IN CACHE\n3. EXIT PROGRAM\n")
#adding address from memory to cache
newccache=[]
newset=[]
def addtocache():
	addr=input("ENTER ADDRESS OF BLOCK TO ADD TO CACHE")
	breakaddr=addr[::-1]
	setno=breakaddr[0:int(setbits)]
	setno=setno[::-1]
	taglen=len(addr)-setbits
	tagval=addr[:int(taglen)]
	print("set: "+str(setno))
	print("tag: "+str(tagval))
	if setno in setarray:
		pointer=setarray.index(setno)
		tag.append(addr)
		newset.append(setno)
		setarray.pop(pointer)
	else:
		np=newset.index(setno)
		tag[np]=addr
	print(newset)
	print(tag)

      

            



#searching for address in cache
def search():

	PA=math.log(MS, 2)
	print("BITS REQUIRES FOR PHYSICAL ADDRESS BITS: "+str(PA))           
	ad=input("ENTER PHYSICAL ADDRESS TO SEARCH IN CACHE MEMORY")
	
	addr=ad[:int(BI)]
	breakaddr=addr[::-1]
	setno=breakaddr[:int(setbits)]
	setno=setno[::-1]
	taglen=len(addr)-setbits
	tagval=addr[:int(taglen)]
	#print("address:"+addr)
	#print("setno: "+setno)
	#print("tagval"+tagval)
	if addr in tag:
		pos=tag.index(addr)
		print("CACHE HIT")
		print(addr+" FOUND")
		print("SET NUMBER: "+setno)
	else:
		print("CACHE MISS")
		breakaddr=addr[::-1]
		setno=breakaddr[0:int(setbits)]
		setno=setno[::-1]
		taglen=addr[:int(taglen)]
		if setno in setarray:
			pointer=setarray.index(setno)
			tag.append(addr)
			newset.append(setno)
			setarray.pop(pointer)
		else:
			np=newset.index(setno)
			tag[np]=addr
		print(addr+ " ADDED TO CACHE")
		print(newset)
		print(tag)





	# taglen=len(addr)-setbits
	# tagval=addr[:int(taglen)]
	# print("set: "+str(setno))
	# print("tag: "+str(tagval))
	# if setno in setarray:
	# 	pointer=setarray.index(setno)
	# 	tag.append(addr)
	# 	newset.append(setno)
	# 	setarray.pop(pointer)
	# else:
	# 	np=newset.index(setno)
	# 	tag[np]=addr
	#print(newset)
	#print(tag)



            




ch='y'
while(ch=="y" or ch=="Y"):

	print("1. PRINT MAIN MEMORY\n2.PRINT CACHE MEMORY\n3.ADD TO CACHE MEMORY\n4.SEARCH IN CACHE MEMORY\n5.EXIT")
	num=int(input())
	if(num==1):
		print(memorindeces)
		print(memoryblocks)
		continue
	if num==2 :
		print(cache)
		continue
	if num==3 :
		addtocache()
		continue
	if num==4 :
		search()
		continue
	else:
		exit(0)

	ch=input("\n\nDO YOU WISH TO CONTINUE? (y/n)")

	 
# print(addtocache())













