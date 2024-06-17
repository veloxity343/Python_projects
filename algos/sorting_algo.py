def read_days_from_file(filename):
    with open(filename, 'r') as file:
        days = [line.strip() for line in file.readlines()]
    return days

def custom_sort(days):
    t_days = [day for day in days if day.startswith('T')]
    other_days = [day for day in days if not day.startswith('T')]
    t_days_sorted = sorted(t_days, key=lambda x: x[1])
    other_days_sorted = sorted(other_days)
    return t_days_sorted + other_days_sorted

# def write_days_to_file(filename, days):
#     with open(filename, 'w') as file:
#         for day in days:
#             file.write(day + "\n")

days_of_the_week = read_days_from_file('dotw')

sorted_days = custom_sort(days_of_the_week)

for day in sorted_days:
    print(day)

# write_days_to_file('sorted_days', sorted_days)