from itemClasses import *
def maxVal(toConsider,avail):
    if toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getWeight()>avail:
        result = maxVal(toConsider[1:],avail)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=maxVal(toConsider[1:],avail-nextItem.getWeight())
        withVal+=nextItem.getValue()
        withoutVal,withoutToTake=maxVal(toConsider[1:],avail)
        if(withVal>withoutVal):
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

def smallTest():
    names=['a','b','c','d']
    vals=[6,7,8,9]
    weights=[3,3,2,5]
    Items=[]
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    val,taken=maxVal(Items,5)
    for item in taken:
        print(item)
    print("Total Value of items taken = ",val)

smallTest()
