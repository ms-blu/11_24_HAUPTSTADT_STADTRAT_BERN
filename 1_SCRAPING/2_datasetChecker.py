import json
# This script checks for completeness of session dates, as means of checking database integrity.
# Load the JSON file
with open("01_output/aggregated_responses_08_20.json", "r") as file:
    data = json.load(file)

# Extract unique session dates from nested dictionaries
session_dates = set()  # Use a set to store unique dates

# Iterate through the outer list
for inner_list in data:
    # Iterate through each dictionary in the inner list
    for item in inner_list:
        if 'entryDate' in item:  # Check if 'sessionDate' exists in the dictionary
            session_dates.add(item['entryDate'])


# Count and print the number of unique session dates
print(f"Number of unique session dates: {len(session_dates)}")
print(sorted(session_dates))