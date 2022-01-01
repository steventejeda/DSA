# Time Complexity O(n^2)
# Space Complexity O(n)

def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(len(array)):
		firstNumber = array[i]
		for j in range(i + 1, len(array)):
			secondNumber = array[j]
			if firstNumber + secondNumber == targetSum:
				return [firstNumber, secondNumber]
	return []

# Solution 2
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoNumberSum(array, targetSum):
    # Write your code here.
	dict = {}
	for num in array: 
		potentialMatch = targetSum - num
		if potentialMatch in dict: 
			return [num, potentialMatch]
		else:
			dict[num] = True
	return []
