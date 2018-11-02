limit = int(input("Number"))
numsum = (limit*(limit+1))/2
numsqsum = ((2*limit+1)*(limit+1)*limit)/6
def sumsquaredif():
    return (numsum**2)-numsqsum
print(numsum)
print(numsum**2)
print(numsqsum)
print(sumsquaredif())
