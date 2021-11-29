def reverseString(string, leftIdx, rightIdx):
    '''

    '''
    if leftIdx >= rightIdx:
        return string
    string[leftIdx], string[rightIdx] = string[rightIdx], string[leftIdx]
    return reverseString(string, leftIdx + 1, rightIdx - 1)


def isPallindrome(string, leftIdx, rightIdx):
    '''

    '''
    if leftIdx >= rightIdx:
        return True
    return (string[leftIdx] == string[rightIdx]) and isPallindrome(string, leftIdx + 1, rightIdx - 1)


string = list("CappaC")

print(reverseString(string, 0, len(string)-1))
print(isPallindrome(string, 0, len(string)-1))
