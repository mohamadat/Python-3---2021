nums = [1,2,3,4,5,6]
my_list = []


# I need each item in nums ???

for item in nums:
    my_list.append(item);

print("my_list: ",my_list)

nums[0] = 99
print("nums: ",nums)


def copy_only_un_even(my_list):
    answer_list = [];
    for item in my_list:
        if item % 2 != 0:
            answer_list.append(item);
    return answer_list;

numbers = [1, 44, 52, 56, 53425, 434, 13, 895]
un_even_numbers = copy_only_un_even(numbers);
print("un_even_numbers: ", un_even_numbers);



# copy to new list and add 10 to each item in the list;
numbers = [1, 44, 52, 56, 53425, 434, 13, 895]
new_numbers = [];


for item in numbers:
    new_numbers.append(item + 10)

print(numbers,new_numbers)


numbers_3 = [x+10 for x in numbers]
print("numbers_3: ", numbers_3)

numbers_4 = [item for item in numbers if item%2 != 0]
print("numbers_4: ", numbers_4)
