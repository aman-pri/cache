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
cacheline=[]
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
CLI=(math.log(CL, 2))
print("Number of cache lines= "+str(CL))
print("Number of bits for cache line indeces: "+str(CLI))
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


#print("1. ADD TO CACHE\n2. SEARCH IN CACHE\n3. EXIT PROGRAM\n")
#adding address from memory to cache


def addtocache():
	addr=input("ENTER ADDRESS OF BLOCK TO ADD TO CACHE")
	pos=memorindeces.index(addr)
	bid=memoryblocks[pos]
	if len(cache)<int(CL):
		
		print("ADDING TO CACHE  ")
		cache.append(addr)
		print(bid+" ADDED TO CACHE")
		print(cache)
	else:
		print("CACHE FULL REMOVING ONE BLOCK")
		cache.pop(0)
		cache.append(addr)
		print(bid+" ADDED TO CACHE")
		print(cache)



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
	if cachead in cache:
		loc=cache.index(cachead)
		line=cacheline[loc]
		loc1=memorindeces.index(cachead)
		blo=memoryblocks[loc1]
		print(blo+" FOUND IN CACHE")
		print("!!!CACHE HIT!!!")
	else:
		addr=cachead
		pos=memorindeces.index(addr)
		bid=memoryblocks[pos]
		if len(cache)<int(CL):
			print("ADDING TO CACHE")
			cache.append(addr)
			print(bid+"ADDED TO CACHE")
			print(cache)
		else:
			print("CACHE IS FULL, REMOVING ONE BLOCK")
			cache.pop(0)
			cache.append(addr)
			print(bid+ " ADDED TO CACHE")
			print(cache)
	# if cachead in cache:
	#  	loc=cache.index(cachead)
	#  	line=cacheline[loc]
	#  	loc1=memorindeces.index(cachead)
	#  	blo=memoryblocks[loc1]
	#  	print(blo+" FOUND IN CACHE ")
	#  	print("\n!!!CACHE HIT!!!")
	# else :
 #            if len(cache)<int(CL):
 #                addr=cachead
 #                pos=memorindeces.index(addr)
	# 	 #pos=memorindeces.index(addr)
	# 	bid=memoryblocks[pos]
	# 	print("ADDING TO CACHE  ")
	# 	cache.append(addr)
	# 		print(bid+" ADDED TO CACHE")
	# 		print(cache)
		
	#     else:
 #            print("CACHE IS FULL\n REMOVING ONE BLOCK")
	# 	 	cache.pop(0)
	# 	 	cache.append(addr)
	# 		print(bid+" ADDED TO CACHE")
	# 	 	print(cache)

	





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
