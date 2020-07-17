# direct mapping
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

#print(cacheline)

#print("1. ADD TO CACHE\n2. SEARCH IN CACHE\n3. EXIT PROGRAM\n")
#adding address from memory to cache


def addtocache():
	addr=input("ENTER ADDRESS OF BLOCK TO ADD TO CACHE")
	pos=memorindeces.index(addr)
	bid=memoryblocks[pos]
	addr2=addr[::-1]
	addr2=addr2[:int(CLI)]
	addr2=addr2[::-1]
	if addr2 in addcacheline:
		locc3=addcacheline.index(addr2)
		addcacheline.pop(locc3)
		cache.pop(locc3)
	print("ADDING TO CACHE LINE NO.: "+str(addr2))
	ntb=int(BI-CLI)
	tagbits=addr[:ntb]
	pos1=cacheline.index(addr2)
	cache.insert(pos1, addr)
	addcacheline.insert(pos1, addr2)
	tag.insert(pos1, tagbits)
	print(bid+" ADDED TO CACHE")
	print(cache)


#searching for address in cache
def search():
	 PA=math.log(MS, 2)
	 print("BITS REQUIRES FOR PHYSICAL ADDRESS BITS: "+str(PA))           
	 ad=input("ENTER PHYSICAL ADDRESS TO SEARCH IN CACHE MEMORY")
	 ntb=int(BI-CLI)
	 tagbits=ad[:ntb]
	 cacheaddress=ad
	 cacheaddress=cacheaddress[:int(CI)]
	 cacheaddress=cacheaddress[::-1]
	 
	 blockoffsetbits=math.log(BS, 2)
	 blockoffset=ad[::-1]
	 blockoffset=blockoffset[:int(blockoffsetbits)]
	 blockoffset=blockoffset[::-1]
	 
	 blockindexbits=PA-blockoffsetbits
	 blockindex=ad[:int(blockindexbits)]
	 
	 cacheindexsize=CI-blockoffsetbits
	 cacheaddress=cacheaddress[::-1]
	 cacheindex=cacheaddress[:int(cacheindexsize)]
	 cacheaddress=cacheaddress[::-1]
	 cacheindex=cacheindex[::-1]
	 print("PHYSICAL ADDRESS: "+str(ad)+"\n")
	 print("CACHE ADDRESS: "+str(cacheaddress)+"\n")
	 print("CACHE LINE: "+str(cacheindex)+"\n")
	 print("BLOCK OFFSET: "+str(blockoffset)+"\n")
	 print("BLOCK INDEX: "+str(blockindex)+"\n")
	 print("TAG: "+str(tagbits)+"\n")
	 cachead=tagbits+cacheindex
	 if cachead in cache:
	 	loc=cache.index(cachead)
	 	line=cacheline[loc]
	 	loc1=memorindeces.index(cachead)
	 	blo=memoryblocks[loc1]
	 	print(blo+" FOUND IN CACHE LINE NUMBER "+cacheindex)
	 	print("\n!!!CACHE HIT!!!")
	 else:
	 	print("\n!!!CACHE MISS!!!")
	 	print("\nADDING BLOCK TO CACHE")
	 	position=memorindeces.index(cachead)
	 	bloid=memoryblocks[position]
	 	cachead2=cachead[::-1]
	 	cachead2=cachead2[:int(CLI)]
	 	cachead2=cachead2[::-1]
	 	if cachead2 in cacheline:
		    locc3=cacheline.index(cachead2)
		    cacheline.pop(locc3)
		    cache.pop(locc3)
	 	print("ADDING TO CACHE LINE: "+str(cachead2))
	 	nt=int(BI-CLI)
	 	tags=cachead[:nt]
	 	loc2=cacheline.index(cachead2)
	 	cache.insert(loc2, cachead)
	 	tag.insert(loc2, tags)
	 	print(bloid+ "ADDED TO CACHE")
	 	print(cache)





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

	 













