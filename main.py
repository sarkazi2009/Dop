grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list_sorted = sorted(students)
new_dict = {my_list_sorted[0]: sum(grades[0]) / len(grades[0]), my_list_sorted[1]: sum(grades[1]) / len(grades[1]),
            my_list_sorted[2]: sum(grades[2]) / len(grades[2]), my_list_sorted[3]: sum(grades[3]) / len(grades[3]),
            my_list_sorted[4]: sum(grades[4]) / len(grades[4])}
print(new_dict)
