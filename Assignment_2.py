lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]

all_lists_dic = {"lst1": lst1, "lst2": lst2, "lst3": lst3}
fit_dict = {}

for name, lst in all_lists_dic.items():
    tmp_set = set(lst)
    if len(tmp_set) == len(lst):
        fit_dict[name] = tmp_set

print(fit_dict)
common_values = set.intersection(*fit_dict.values())
print("The common values are :", common_values, "of lists: ", fit_dict.keys())
