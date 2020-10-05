

def age_assignment(*names, **age_data):
    ages_by_name = {}

    for name in names:
        first_letter = name[0]
        ages_by_name[name] = age_data[first_letter]

    return ages_by_name


# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
