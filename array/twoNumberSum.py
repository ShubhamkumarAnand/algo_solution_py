import time

# O(n) space | O(n) time
def twoNumberSumOp(array, targetSum):
    nums = {}
    for value in array:
        sum = targetSum - value
        if sum in nums:
            return [value, sum]
        else:
            nums[value] = True
    return []


# O(n(log(n))) Time | O(1) Space
def twoNumberSum(array, targetSum):
    array.sort()
    i = 0
    j = len(array)-1
    while i < j:
        sum = array[i] + array[j]
        if (sum == targetSum):
            return [array[i], array[j]]
        elif (sum > targetSum):
            j -= 1
        else:
            i += 1
    return []


# O(n^2) time | O(1) space
def twoNumberSumBf(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            sum = firstNum + secondNum
            if sum == targetSum:
                return [firstNum, secondNum]
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 14

start = time.time()
res = twoNumberSumOp(array, targetSum)
end = time.time()
print(res)
print(end-start)
