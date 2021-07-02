# Non-primatives types are copied by Refernce
nums = [1,2,3,4,5,6]

# I need each item in nums ???
my_list = nums;
print(my_list, nums)


nums[0] = 99;
print(my_list, nums)

# primatives types are copied by value
num = 1
new_num = num
print(new_num, num)

new_num = 99
print(new_num, num)


