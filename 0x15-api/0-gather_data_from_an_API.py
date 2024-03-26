#!/usr/bin/python3

""" Python script that, using this REST API, for a given employee ID """

import requests
import sys


if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    num_tasks = 0
    num_comp_tasks = 0;
    tasks = []
    user_info = (requests.get(url_user)).json()
    if user_info.status_code != 200:
        return

    todo_info = (requests.get(url_todo)).json()
    if todo_info.status_code != 200:
        return

    for i in user_info:
        if i.get('id') == int(sys.argv[1]):
            user_name = i.get('name')


    for i in todo_info:
        if i.get('userId') == int(sys.argv[1]):
            num_tasks += 1
            if i.get('completed') is True:
                num_comp_tasks += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format
            (user_name, num_comp_tasks,num_tasks))

    for i in tasks:
        print("\t {}".format(i))



