# Assuming the file is named 'students.csv'

# Initialize an empty dictionary
student_preferences = {}

# Open the CSV file and read it line by line
with open('../data/stu-pref-v2.csv', 'r') as file:
    for line in file:
        # Strip whitespace and split by comma
        parts = line.strip().split(',')
        # The first part is the name, the rest are the preferences
        name = parts[0]
        preferences = parts[1:]
        # Add to the dictionary
        student_preferences[name] = preferences

# Displaying the result, with each record on a new line
print("student_preferences = {")
for name, prefs in student_preferences.items():
    print(f'    "{name}": {prefs},')
print("}")
