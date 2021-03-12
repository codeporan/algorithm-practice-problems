
# Two Number Sum:

# [3,5,-4,8,11,1,-1,6], 10

# 1st method: using two loop
# Time: 0(n^2) | 0(1) space
def twoNumberSum (array, targetSum):
	for i in range(len(array)-1):
		firstNum = array[i]
		for x in range(i+1,len(array)):
			secondNum = array[x]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
return []


# 2nd method:
def twoNumberSum (array, targetSum):
	nums = {}
	for num in array :
		patentialMatch = targetSum - num
		if patentialMatch in nums:
			return [patentialMatch, num]
		else 
			nums[num] = True
	return []
# 	using Hash table:
# 	{
# 		3:true
# 	    5:true
# 	    -4:true,
# 	    8 :true,
# 	    11: true,
# 	    1:true
# 	}

# 	Target sum = 10 
# 	Current Num = x 
# 	x + y 
# 	y 	= 10 - x 
# 		= 10-3 = 7
# 		= 10 - 5 = 5  
# 		= 10 - (-4) = 14
# 		= 10 - 8 = 2
# 		= 10 - 11 = -1 
# 		= 10 - 1 = 9
# 		= 10 - (-1) = 11 [ we are done ]

# 	return [11, -1]

#  Time : 0(N)
#  space: 0(N)




#  3rd Method :
 
def twoNumberSum (array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1

	while left<right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum 
			return [ array[left], array[right]]
		elif currentSum< targetSum: 
			left +=1
		elif currentSum> targetSum:
			right -=1
    return []


#  [4,-1,1,3,5,6,8,11], 13
#    L 			 R 

#  if 7 is less than 10 , then L will move to Right 

#  if 14 is greater than 13 , then R will move to LEFT 

#   - 4 + 11 = 7
#   - 1 + 11 = 10 
#     1 + 11 = 12 
#     3 + 11 = 14
#     3 + 8  = 11
#     5 + 8 =  13

#  Time : 0(nLog(n))
#  space: 0(N)









