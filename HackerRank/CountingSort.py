'''
Approach:
So first We need to have the the maximum value in our array
2. Then create a new array called "Result" with the size of the max value of the given array:
3. After creating the array now we should iterate through the first array then get the values so 
while iterating we get the value of each index and then append the number of count that value has and
use that value as the index of the Result array.
4. IncreaSE count whenever we counter the same value
'''
arr = [1, 1, 3, 2, 1]

 
Range_Value = max(arr)
print(Range_Value)

result = [0] * Range_Value

count = 0

for i in range(len(arr) - 1):
    temp = arr[i]
    result[temp] += 1

print(result)










