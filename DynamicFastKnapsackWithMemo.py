from itemClasses import *
import random

def fastMaxVal(toConsider,avail,memo={}):
    if(len(toConsider),avail) in memo:
        result=memo[(len(toConsider),avail)]
    elif toConsider==[] or avail==0:
        result=(0,())
        return result
    elif toConsider[0].getWeight()>avail:
        result=fastMaxVal(toConsider[1:],avail,memo)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=fastMaxVal(toConsider[1:],avail-nextItem.getWeight(),memo)
        withVal+=nextItem.getValue()
        withoutVal,withoutToTake=fastMaxVal(toConsider[1:],avail,memo)
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    memo[(len(toConsider),avail)] = result
    return result



def buildManyItems(numItems,maxVal,maxWeight):
    items=[]
    for i in range(numItems):
        items.append(Item(str(i),random.randint(1,maxVal),random.randint(1,maxWeight)))
    return items
def bigTest(numItems):
    items=buildManyItems(numItems,10,10)
    val,taken=fastMaxVal(items,40)
    print("Items Taken")
    for item in taken:
        print(item)
    print("Total value of items taken=",val)
bigTest(20)
