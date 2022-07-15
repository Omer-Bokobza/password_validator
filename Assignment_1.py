def split_male_female(people: dict):
    """
    :param people: dictionary
    :return: two dictionaries male and female separate
    """

    print("Split Male and Female dictionary", "\n")
    male_dict = {}
    female_dict = {}

    for i in dict(people).keys():
        if people[i]["sex"] == "male":
            male_dict[i] = people[i]
        else:
            female_dict[i] = people[i]

    return male_dict, female_dict


def find_median_average(age: dict):
    """
    :param age: dictionary
    :return: Median and average of dictionary "age"
    """

    print("Median and Average")
    num = 0
    median_age = []
    for i in age:
        num = num + age[i]["age"]
        median_age.append(age[i]["age"])

    avg = num / len(age)
    median_age.sort()

    if len(median_age) % 2 != 0:
        median = median_age[int(len(median_age) / 2)]
    else:
        median = (median_age[int(len(median_age) / 2)] + median_age[int(len(median_age) / 2 - 1)]) / 2

    print("The median age is :", median)
    print("The average age is :", avg, "\n")


def print_values_above(age_dict: dict, num=0):
    """
    :param age_dict: dictionary
    :param num: integer number to compare to
    :return:
    """

    print("Check values above num")
    if num == 0:
        print("No num was sent (Default is 0)")
    else:
        print("The num you sent to check with is :", num)
    for age in age_dict:
        if age_dict[age]["age"] > num:
            print(age_dict[age])


if __name__ == "__main__":
    data_set = {100001: {"name": "Tal", "sex": "male", "age": 22},
                100002: {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"}, \
                100003: {"name": "Sharon", "age": 27, "sex": "female"},
                100004: {"name": "David", "age": 53, "sex": "male"}}

    male, female = split_male_female(data_set)
    print("Male dictionary", male)
    print("Female dictionary", female, "\n")
    find_median_average(data_set)
    print_values_above(data_set, 27)
