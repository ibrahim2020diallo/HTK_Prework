def getLargestName(names_list):
    max_len = -1
    for name in names_list:
        if len(name) > max_len:
            max_len = len(name)
            find_name = name

        return find_name

names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
big_name = getLargestName(names_list)
print(big_name)
