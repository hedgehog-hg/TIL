def circleOfNumbers(n,firstNumber):
    return firstNumber + (n//2)*(1 if n/2 > firstNumber else -1)

def depositProfit(deposit,rate,threshold):
    year = 0
    while deposit*(1+rate/100)**year < threshold:
        year+=1
    return year

def absoluteValuesSumMinimization(arr):
    size = len(arr)
    idx= size//2 -1 if size%2 == 0 else size//2
    return arr[idx]

def stringsRearrangement(inputArray):
    return 

#print(circleOfNumbers(6,3))
#print(depositProfit(100,20,170))
#print(absoluteValuesSumMinimization([2,4,7]))
print(stringsRearrangement('aba','bbb','bab'))