from matching.games import HospitalResident

# Example data
student_preferences = {
    "Alice": ["Project1", "Project2", "Project3"],
    "Bob": ["Project2", "Project3", "Project1"],
    "Charlie": ["Project3", "Project1", "Project2"]
}

# All students are listed in each project's preferences (no specific order)
all_students = list(student_preferences.keys())
project_preferences = {
    "Project1": all_students,
    "Project2": all_students,
    "Project3": all_students
}

# Capacities for each project
project_capacities = {
    "Project1": 1, 
    "Project2": 1,
    "Project3": 1
}

# Create the game and solve it
game = HospitalResident.create_from_dictionaries(
    student_preferences, project_preferences, project_capacities
)
matching = game.solve()

print(matching)
