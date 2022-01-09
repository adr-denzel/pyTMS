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

### Login

User prompted to enter a username and password. user.txt stores all valid user/password pairs. Error message displayed if user enters invalid username or valid username combined with invalid password. User is repeatedly prompted to enter a valid username and password.

### Register User

User ('admin' Only) submits 'r' selection, then prompted to submit a username and password to register new user. User is prompted to confirm password. New username and password is appended to user.txt. Error message displayed should user attempt to register an already allocated username.

### Display Statistics

User ('admin' Only) submits 'ds' selection, updates are made to task_overview.txt and user_overview.txt, subsequently their contents are printed to terminal.

### Add Task

User submits 'a' selection, then prompted to enter the username of the person to assign the task to, the task title, task description, and task due-date. New task is appended to tasks.txt. Task assignment date defaults to current date. Task completed attribute defaults to 'No'.

### View All

User submits ‘va’ selection and all task and their attributes get displayed to terminal.

### View My Tasks 

User submits ‘vm’ selection, index of tasks assigned to them is displayed to terminal. User then selects specific task to drilldown, or returns to main menu.

If user selects specific task to drilldown, task may either be edited or marked complete. Editing task allows for 'Task Assinged to' and 'Due Date' to be modified only. 

### Generate Report

User submits 'g' selection and contents of user_overview.txt and task_overview.txt are updated.
