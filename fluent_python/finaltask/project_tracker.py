#! /usr/bin/python3

import sqlite3
from pathlib import Path

connection = sqlite3.connect("tracker.db")
cursor = connection.cursor()

def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        due_date TEXT NOT NULL,
        project_budget INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        project_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        complete INTEGER NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects(project_id),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workertasks (
        employee_task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER NOT NULL,
        employee_id INTEGER NOT NULL,
        FOREIGN KEY(task_id) REFERENCES tasks(task_id),
        FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
        )
    ''')

def add_project(name, description, due_date, project_budget):
    cursor.execute('''
    INSERT INTO projects (name, description, due_date, project_budget)
    VALUES (?, ?, ?, ?)
    ''', (name, description, due_date, project_budget))
    connection.commit()

def add_employee(firstname, lastname, salary):
    cursor.execute('''
    INSERT INTO employees(firstname, lastname, salary)
    VALUES (?, ?, ?)
    ''', (firstname, lastname, salary))
    connection.commit()

def add_task(project_id, worker_id, name, description):
    cursor.execute('''
    INSERT INTO tasks (project_id, worker_id, name, description, complete)
    VALUES (?, ?, ?, ?, 0)
    ''', (project_id, worker_id, name, description))
    connection.commit()

def view_projects():
    cursor.execute('''
    SELECT project_id, name FROM projects
    ''')
    projects = cursor.fetchall()
    return projects

def mark_task_complete(task_id):
    cursor.execute('''
    UPDATE tasks
    SET complete = 1
    WHERE task_id = ?
    ''', (task_id,))
    connection.commit()

def view_incomplete_tasks(task_id):
    cursor.execute('''
    SELECT *
    FROM tasks
    WHERE task_id = ? AND complete = 0
    ''', (task_id,))
    return cursor.fetchall()

def salaries():
    cursor.execute('''
    SELECT SUM(salary) AS sum_of_salaries FROM employees
    ''')
    return cursor.fetchall()

def delete_project():
    pass

def main():
    create_tables()
    while True:
        print("What would you like to do with it press the number you would want to do?")
        print("1. Add new project.")
        print("2. Add employee.")
        print("3. Add tasks for the project.")
        print("4. Mark task as complete.")
        print("5. View incomplete tasks.")
        print("6. Delete project")
        choice = input()

        if choice == "1":
            print("")
            name = input("Type name of project: ")
            description = input("Type project description: ")
            due_date = input("Type in the deadline for the project")
            budget = int(input("Type in projectbudget: "))
            add_project(name, description, due_date, budget)
            on_going_projects = view_projects()
            print(on_going_projects)

        elif choice == "2":
            print("")
            firstname = input("Give firstname: ")
            lastname = input("Give lastname: ")
            salary = int(input("Give salary of employee: "))
            add_employee(firstname, lastname, salary)

        elif choice == "3":
            amount_of_tasks = cursor.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
            amouont_of_employees = cursor.execute("SELECT COUNT(*) FROM employees").fetchone()[0]
            if amount_of_tasks < 0:
                print("Add a project first.")
                if amouont_of_employees < 0:
                    print("Not enough employees.")
                print("")
            else:
                #print(on_going_projects)
                #print(view_employees)
                project_id = int(input("Add task to project. Use project id: "))
                project_budget = cursor.execute(f"SELECT project_budget FROM projects WHERE id = {project_id}").fetchone()[0]
                print(project_budget)
                salaries()
                #if project_budget 
                worker_id = int(input("Add employee to task. Use employee id: "))
                name = input("Type name of the task: ")
                description = input("Type in description for task: ")
                add_task(project_id, worker_id, name, description)
                #else:
                #print("The budget is too small.")
                #print(salaries())

        elif choice == "4":
            task_id = int(input("Give the id of the completed task."))

        elif choice == "5":
            task_id = int(input("Give id for project you wish to check on: "))
            view_incomplete_tasks(task_id)


if __name__ == "__main__":
    main()