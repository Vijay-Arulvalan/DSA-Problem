#Method 1 

def TwoNumSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return[firstNum, secondNum]
    return[]

#method 2 // hash table

def TwoNumSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return[potentialMatch, num]
        else:
            nums[num]= True
    return[]

#method 3 to solve the proble using pointer

def TwoNumSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return[array[left], array[right]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1