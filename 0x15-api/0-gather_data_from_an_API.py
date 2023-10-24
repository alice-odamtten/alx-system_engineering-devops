#!/usr/bin/python3
"""
Python script that using this REST API
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = (requests.get(url + "/users/{}".format(argv[1])).json().get("name"))
    todos_list = requests.get(url + "/user/{}/todos".format(argv[1])).json()

    done = []
    completed_number = 0
    for todo in todos_list:
        if todo.get("completed"):
            completed_number += 1
            done.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed_number, len(todos_list)))
    for title in done:
        print("\t {}".format(title))
