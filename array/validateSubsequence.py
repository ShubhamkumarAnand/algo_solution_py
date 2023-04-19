# O(n) | O(1)
def validateSubsequence(array, subsequence):
    subIdx = 0
    arrIdx = 0
    while subIdx < len(subsequence) and arrIdx < len(array):
        if subsequence[subIdx] == array[arrIdx]:
            subIdx += 1
        arrIdx += 1
    return subIdx == len(subsequence)

# O(n) | O(1)
def validateSubsequenceFor(array, subsequence):
    subIdx = 0
    for value in array:
        if subIdx == len(subsequence):
            return True
        if value == subsequence[subIdx]:
            subIdx += 1
    return subIdx == len(subsequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
subsequence = [1, 6, -1]

res1 = validateSubsequence(array, subsequence)
res2 = validateSubsequenceFor(array, subsequence)
print(res2)
