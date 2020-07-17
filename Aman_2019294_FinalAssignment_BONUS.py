# associative mapping
#each memory block maps with any cache line
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
cachel2=[]
cacheline=[]
cache2line=[]
#list for tag entries
tag=[]
MS=int(input("Input Memory size"))
BS=int(input("Input Block size"))
NB=(MS/BS)
#bits req for address of blocks 
BI=(math.log(NB, 2))
print("Number of bits for block indeces= "+str(BI))
CS=int(input("Input Cache Size for L1 CACHE"))
CL=CS/BS
CL2=2*CL
CI=(math.log(CS, 2))
CLI=(math.log(CL, 2))
CL2I=(math.log(CL2, 2))
print("Number of cache lines in L1 CACHE= "+str(CL))
print("Number of cache lines in L2 CACHE= "+str(CL2))
#print("Number of bits for cache line indeces: "+str(CLI))
tb=BI-CLI
filler=int(BI)
print(filler)
print("Number of bits required for tag bits: "+str(tb))
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



print("\n\n")
for j in range(int(CL)):
    addc=str(tobin(j))
    diffc=CLI-len(addc)
    filledc=(int(diffc)*"0")+addc
    cacheline.append(filledc)
for j in range(int(CL2)):
    addc=str(tobin(j))
    diffc=CL2I-len(addc)
    filledc=(int(diffc)*"0")+addc
    cache2line.append(filledc)

print("L1 CACHE: ")
print(cacheline)
print("L2 CACHE: ")
print(cache2line)

#adding address from memory to cache


def addtocache():
	addr=input("ENTER ADDRESS OF BLOCK TO ADD TO CACHE")
	pos=memorindeces.index(addr)
	bid=memoryblocks[pos]
	if len(cache)<int(CL) and len(cachel2)<int(CL2) and addr not in cache:
		
		print("ADDING TO CACHE  ")
		cache.append(addr)
		cachel2.append(addr)
		print(bid+" ADDED TO CACHE L1 AND L2")
		print(cache)
		print(cachel2)
	elif len(cache)>=int(CL) and len(cachel2)<int(CL2):
		print("L1 FULL, REPLACING BLOCK")
		cache.pop(0)
		cache.append(addr)
		if addr not in cachel2:
			cachel2.append(addr)
		print(bid+" ADDED TO CACHE L1 and L2")
		print(cache)
		print(cachel2)
	else:
		print("L1 and L2 FULL, REPLACING BLOCKS ")
		pop=cachel2.index(cache[0])
		cache.pop(0)
		cachel2.pop(pop)
		cache.append(addr)
		cachel2.append(addr)
		print(cache)
		print(cachel2)



#searching for address in cache
def search():

	PA=math.log(MS, 2)
	print("BITS REQUIRES FOR PHYSICAL ADDRESS BITS: "+str(PA))           
	ad=input("ENTER PHYSICAL ADDRESS TO SEARCH IN CACHE MEMORY")
	cacheaddress=ad
	cacheaddress=cacheaddress[:int(CI-1)]
	 
	blockoffsetbits=math.log(BS, 2)
	blockoffset=ad[::-1]
	blockoffset=blockoffset[:int(blockoffsetbits)]
	blockoffset=blockoffset[::-1]
	 
	blockindexbits=PA-blockoffsetbits
	blockindex=ad[:int(blockindexbits)]
	 
	cacheindexsize=CI-blockoffsetbits

	cacheindex=cacheaddress[:int(cacheindexsize)]
	cacheindex=cacheindex[::-1]
	 
	print("PHYSICAL ADDRESS: "+str(ad)+"\n")
	print("CACHE ADDRESS: "+str(cacheaddress)+"\n")
	#print("CACHE LINE: "+str(cacheindex)+"\n")
	print("BLOCK OFFSET: "+str(blockoffset)+"\n")
	print("BLOCK INDEX: "+str(blockindex)+"\n")
	cachead=cacheaddress
	addr=cachead

	
	if cachead in cache:
		loc=cache.index(cachead)
		line=cacheline[loc]
		loc1=memorindeces.index(cachead)
		blo=memoryblocks[loc1]
		print(blo+" FOUND IN L1 CACHE")
		print("L1 CACHE HIT")
	elif cachead not in cache and cachead in cachel2:
		print("CACHE MISS : L1")
		print("CACHE HIT : L2")
		pos=memorindeces.index(addr)
		bid=memoryblocks[pos]
		if len(cache)<int(CL):
			print("ADDING TO L1")
			cache.append(addr)
			print(bid+"ADDED TO L1")
			print(cache)
		else:
			print("L1 IS FULL, REPLACING BLOCK")
			cache.pop(0)
			cache.append(addr)
			print(bid+ " ADDED TO CACHE")
			print(cache)
	else:
		print("CACHE MISS : L1")
		print("CACHE MISS : L2")
		if len(cache)<int(CL) and len(cachel2)<int(CL2):
			cache.append(addr)
			cachel2.append(addr)
			print("ADDED TO L1 and L2")
		elif len(cache)>=int(CL) and len(cachel2)<int(CL2):
			cache.pop(0)
			cache.append(addr)
			if addr not in cachel2:
				cachel2.append(addr)
			print("ADDED TO L1 and L2")
		else:
			pop=cachel2.index(cache[0])
			cache.pop(0)
			cachel2.pop(pop)
			cache.append(addr)
			cachel2.append(addr)
			print("ADDED TO L1 and L2")




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
