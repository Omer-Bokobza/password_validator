lst = [31, 99, 3, 1943, 312, 12, 12]

num = max(lst)

max_list = [int(i) for i in str(num)]

print("sort order - asc :", sorted(max_list))
print("sort order - desc :", sorted(max_list, reverse=True))
