# The next step is to save this converted JSON data to a new file
json_file_path = '../data/results.txt'

# Writing JSON data to a file
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

json_file_path
