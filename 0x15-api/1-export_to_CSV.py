#!/usr/bin/python3

""" Python script that, using this REST API, for a given employee ID """

import csv
import requests
import sys

if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    num_tasks = 0
    num_comp_tasks = 0
    tasks = []
    user_id = int(sys.argv[1])
    user_name = None

    user_info = (requests.get(url_user)).json()
    todo_info = (requests.get(url_todo)).json()

    for i in user_info:
        if i.get('id') == user_id:
            user_name = i.get('username')

    for i in todo_info:
        if i.get('userId') == user_id:
            num_tasks += 1
            task_completed = i.get('completed')
            if task_completed:
                num_comp_tasks += 1
            tasks.append((user_id, user_name, task_completed, i.get('title')))

    csv_file_name = str(user_id) + ".csv"
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(tasks)
