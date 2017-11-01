# Iterating on a diictionary

course_minutes = {'python basics': 234, 'python _collections': 200, 'ruby_rails': 240}

for course in course_minutes:
    print(course_minutes[course])


# Using keys

for key in course_minutes.keys():
    print(key)

for value in course_minutes.values():
    print(value)

for item in course_minutes.items():
    print(item)
