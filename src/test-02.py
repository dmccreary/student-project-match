from matching.games import StableMarriage

student_preferences = {
     "s1": ["p1", "p2", "p3"], 
     "s2": ["p2", "p3", "p1"], 
     "s3": ["p3", "p1", "p2"]
}

project_preferences = {
        "p1": ["s1", "s2", "s3"], 
        "p2": ["s1", "s2", "s3"], 
        "p3": ["s1", "s2", "s3"]
}


game = StableMarriage.create_from_dictionaries(project_preferences, 
                                               student_preferences)
result = game.solve()
print(result)

# I got the following result
# {p1: s1, p2: s2, p3: s3}
# which is what I expected