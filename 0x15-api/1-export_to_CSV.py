#!/usr/bin/python3
# Returns Todo list for a given employee id and exports data in the CSV format

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]  # Get the employee ID from command-line arguments

    # Fetch user details
    user_response = requests.get(url + f"users/{id}")
    user = user_response.json()

    # Fetch tasks for the user
    tasks_response = requests.get(url + f"todos", params={"userId": id})
    todos = tasks_response.json()

    # Prepare the CSV file name based on the user ID
    file_name = f"{id}.csv"

    # Open the CSV file in write mode
    with open(file_name, "w") as csv_file:
        # Write the header row
        csv_file.write(f'USER_ID,"USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"\n')

        # Iterate through each task and write it to the CSV file
        for task in todos:
            # Extract the required fields from the task dictionary
            user_id = id
            username = user['username']
            task_completed_status = str(task['completed']).lower()  # Convert boolean to string
            task_title = task['title']

            # Write the task details to the CSV file
            csv_file.write(f'{user_id},"{username}","{task_completed_status}","{task_title}"\n')
