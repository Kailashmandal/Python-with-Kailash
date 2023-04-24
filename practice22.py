
def avg(*args):
    avgList=[]
    for pair in zip(*args):
        avgList.append(sum(pair)/len(pair))
    return avgList

print(
    avg([1,2,3],[4,5,6],[7,8,9] )
)

## by other method
    
avg_fun=lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(
    avg_fun([1,2,3],[4,5,6],[7,8,9])
)
