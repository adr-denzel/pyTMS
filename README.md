# Py-TMS

A .txt based task management system for commandline.

This project implements string handling, lists, dictionaries, functions, and working with external data sources.

## Context

Program uses 4 files for data storage: user.txt, tasks.txt, task_overview.txt, and user_overview.txt. 

tasks.txt: Contains the following task attributes:

1. Username assigned to task
2. Task title
3. Task description
4. Task assignment date
5. Task due date
6. Task completed boolean

user.txt: Contains username-password pairs to access program.

task_overview.txt contains:

1. Total number of tasks tracked
2. Number of tasks marked complete
3. Number of tasks marked incomplete
4. Number of tasks marked incomplete and overdue
5. Percentage of tasks incomplete
6. Percentage of tasks overdue

user_overview.txt contains:

1. Total number of tasks tracked
2. Total number of registered users

Per user the following is output:

1. Number of tasks assinged to user
2. Percentage of all tasks assigned to user
3. Percentage of user's assigned tasks completed
4. Percentage of user's assigned tasks incomplete
5. Percentage of user's assigned tasks incomplete and overdue

## Program Features

Login. The user is prompted to enter a username and password. A list of valid usernames and passwords are stored in user.txt. An error message is displayed if the user enters a username that is not listed in user.txt or enters a valid username and an invalid password. The user is repeatedly be asked to enter a valid username and password until they provide appropriate credentials. The main menu is displayed upon successful login.

Register user. If the user chooses ‘r, the user is prompted to enter a new username and password. The user is then asked to confirm the password. Upon successful registration, the new username and password is written to user.txt. Only a user with the username ‘admin’ can register users.

Add task. If the user chooses ‘a’, the user is prompted to enter the username of the person the task is assigned to, the title of the task, a description of the task and the due date of the task. The new task is then written to tasks.txt. The date on which the task is assigned will be the current date. The value that indicates whether the task has been completed or not defaults to ‘No’.

View all tasks. If the user chooses ‘va’, the information for every task is displayed on the screen.

View my tasks. If the user chooses ‘vm’ the information for the tasks that are assigned to her are displayed on the screen. The user can select either a specific task by selecting a corresponding task number or input ‘-1’ to return to the main menu.

View specific task. If the user selects a specific task, they can either mark the task as complete or edit the task. When the user chooses to edit a task, the username of the person to whom the task is assigned and/or the due date of the task can be edited.

The admin user is provided with two additional menu options that allows them to display statistics, ‘s’, and generate reports, ‘g’.

Generate reports. If the user chooses ‘g’, task_overview.txt and user_overview.txt, are generated.

Display Statistics. If ‘s’ is selected, the reports generated from generate reports are read from task_overview.txt and user_overview.txt and displayed on the screen.

======================================================================

Functions in the programme:

login() – Logs a user in.

main_menu() – Displays the main menu.

reg_user() — Allows a user to add a new user.

add_task() — Allows user to add a new task.

view_all() — Displays all the tasks listed in tasks.txt.

view_mine() — Displays all the tasks assigned to logged in user. Also allows user to view a specific task.

view_task(task) – Displays a user-selected task. Allows user to edit or mark task as complete.

display_stats() – Reads and displays info from task_overview.txt, and user_overview.txt

Helper functions:

get_users() – Reads and returns users from users.txt.

get_tasks() – Reads and returns tasks from tasks.txt.

write_task([tasks], method) – Writes or appends tasks to tasks.txt.

update_tasks(updated_task) – Finds updated_task in tasks list, edits the value. Then calls write_task() with method=”w”.

generate_reports() – Writes data to task_overview.txt, and user_overview.txt.
