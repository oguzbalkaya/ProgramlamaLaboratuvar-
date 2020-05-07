class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<'+self.name+','+str(self.value)+','+str(self.weight)+'>'
def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()
def buildItems(names,values,weights):
    Items =  []
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items