#!/usr/bin/python3
'''
Load, add, save - Adding arguments to a python list
'''
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


# File name for the JSON file
json_filename = "add_item.json"

# Check if the JSON file exists
if os.path.exists(json_filename):
    # If it exists, load the existing content
    my_list = load_from_json_file(json_filename)
else:
    # If it doesn't exist, create an empty list
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, json_filename)

