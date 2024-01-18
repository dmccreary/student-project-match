import csv
import re

def process_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            processed_row = [row[0]]  # Keep the first column as it is
            for item in row[1:]:
                # Remove all non-numeric characters
                numeric_part = re.sub("[^0-9]", "", item)
                processed_row.append(numeric_part)
            writer.writerow(processed_row)

# Example usage
print('processing data')
process_csv('../data/stu-pref-v1.csv', '../data/stu-pref-v2.csv')
