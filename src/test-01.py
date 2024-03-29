# This is the code generated by ChatGPT
# it does not work because the hospital resident match
# requires three parameters:
# https://daffidwilde.github.io/matching/docs/tutorials/hospital_resident.html
#

from matching.games import HospitalResident

# Example data
students = {
    "Alice": ["Project1", "Project2", "Project3"],
    "Bob": ["Project2", "Project3", "Project1"],
    "Charlie": ["Project3", "Project1", "Project2"]
}

# Capacity of each project
projects = {
    "Project1": {"capacity": 1, "preferences": []},
    "Project2": {"capacity": 1, "preferences": []},
    "Project3": {"capacity": 1, "preferences": []}
}

# Create the game and solve it
game = HospitalResident.create_from_dictionaries(students, projects)
matching = game.solve()

print(matching)
