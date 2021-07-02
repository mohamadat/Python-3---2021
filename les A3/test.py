# Data structures

name = "Atwa-ICT";

skills = 15;

new_skills = skills + 10;


on = True; # False

years_list = [2009, 1980, 2010, 2006];
years_tuple = (2009, 1980, 2010, 2006);
years_dictionary = {"warm": 2006, "cold": [2000, 2020, 2021]};

print(years_list, years_tuple);

# print(years_list[0]);
# print(years_list[1]);
# print(years_list[2]);

# for item in years_tuple:
#     print(item);

# years_tuple[0] = 0;
print(years_list, years_tuple, years_dictionary);
print("years_dictionary ",years_dictionary['cold']);
print("one item: ",years_dictionary.get('eee', "No item with this key in the dict"));
