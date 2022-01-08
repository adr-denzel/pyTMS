# ref: https://www.teclado.com/30-days-of-python/python-30-day-21-multiple-files
# got unhappy with the complexity of working in one file
# split the code into a functions file and the program logic
# flow main file where you initiate task_manager from

# import declaration for datetime
# reference here: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date

# function defined to create 2 lists: for all registerd users, for all passwords
def credentials(user_list, password_list):
    # open file  to access user names to test for login
    with open('user.txt', 'r') as credentials:
        # local variable to house txt file info
        all_credentials = credentials.readlines()

        # loop for every line in file
        for i in all_credentials:
            # process string data per line
            user = i.split(',')[0].strip()
            password = i.split(',')[1].strip()

            # write list of all users & list of all passwords
            user_list.append(user)
            password_list.append(password)
    
    return user_list, password_list

# functiojned defined to create a list of all registered users
# decided to do this once since i repeat this procedure about
# 3 times in the other functions after logging in
def credentials_users(user_list):
    # open file  to access user names to test for login
    with open('user.txt', 'r') as credentials:
    
        # local variable to house txt file info
        all_credentials = credentials.readlines()

        # loop for every line in file
        for i in all_credentials:
            # process string data per line
            user = i.split(',')[0].strip()
            # write list of all users & list of all passwords
            user_list.append(user)
    
    return user_list

# user registration function
def reg_user(session_name):
    # declare storage lists for password/user login authorisation
    all_users = []

    # call function to get list of all users
    credentials_users(all_users)
    
    # if statement to ensure admin user access only
    if session_name == 'admin':
        # prompt for user registration
        print('\nyou\'re about to register a new user\n')
        new_user = input('enter new username: ') 

        # if username is already in use, cannot proceed
        while new_user in all_users:
            new_user = input('\nthat username is already in use. please enter a user name: ')
        
        # password inputs
        new_password = input('enter new user\'s password: ')
        password_confirm = input('verify password entry: ')

        # had issues ovverwriting the entire
        # user.txt file: https://stackoverflow.com/questions/22441803/how-to-write-to-a-file-without-overwriting-current-contents
        # file object to append a new user
        with open('user.txt', 'a') as register_user:
            # flag for password matching
            password_match = False

            # while loop to run-until matching passwords submitted
            while not password_match:
                if new_password == password_confirm:
                        
                    # if passwords match, while will termintate from flag change
                    password_match = True
                    register_user.write('\n' + new_user + ', ' + password_confirm)
                    print(f'\nnew user \'{new_user}\' registered')

                else: 
                    print('\npasswords didn\'t match. please try again\n')
                    # prompts to resubmit new user passwords
                    new_password = input('enter new user\'s password: ')
                    password_confirm = input('verify password entry: ')

    else:
        # message for unauthorised attmpt to acces 
        print(f'\n\'{session_name}\' does not possess admin rights. access denied')

# task addition function
def add_task():
    # declare storage lists for password/user login authorisation
    all_users = []

    # call function
    credentials_users(all_users)
    
    print('\nyou\'re about to register a new task\n')

    # request who task is assigned to
    task_assigned = input('to which user is this task assigned: ')

    # if above submission not a registered user, will prompt to resubmit user
    while task_assigned not in all_users:
        task_assigned = input('\nuser not found. please try again and enter a registered user: ')

    # requesting task parameters
    task_title = input('please input task title: ')
    task_description = input('please provide a task description: ')
    # a little held for this part: https://www.geeksforgeeks.org/get-current-date-using-python/
    task_assigned_date_raw = date.today()
    task_due_date = input('please indicate a due date (e.g. \'10 October 2021\'):')
    task_completion = 'No\n'

    # dict to help convert datetime object and method into the format used in txt
    # mapping integers to the months of the year they correspond to
    # a bit of inspiration: https://jaxenter.com/implement-switch-case-statement-python-138315.html
    month_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }

    # using f-sting format to conver date time in e.g. '12 November 2021' format
    task_assigned_date = f'{task_assigned_date_raw.day} {month_dict[task_assigned_date_raw.month]} {task_assigned_date_raw.year}'

    # writing to tasks file
    with open('tasks.txt', 'a') as register_task:
        register_task.write(
            task_assigned + ', '
            + task_title + ', '
            + task_description + ', '
            + task_assigned_date + ', '
            + task_due_date + ', '
            + task_completion
        )
        print('\nyour task has been registered')

# view all function
def view_all():
# decalre data struct to hold file contents
    task_container = []

    with open('tasks.txt', 'r') as read_tasks:

        for line in read_tasks:
            task_container.append(line)
        
    print('\nall tasks with index:')
        
    # process file contents
    for i in task_container:

        display_container = []
        display = i.split(',')

        for j in display:
            display_container.append(j.strip())
            
        display_template = f'''
        {task_container.index(i) + 1}.
        ------------------------------------------------------------------------------------------------------------------------------------
        assigned to: {display_container[0]}
        task title: {display_container[1]}
        task description: {display_container[2]}
        assignment date: {display_container[3]}
        due date: {display_container[4]}
        completed: {display_container[5]}
        ------------------------------------------------------------------------------------------------------------------------------------
        '''

        print(display_template)

# view mine funtion
def view_mine(user_name):
    # declare storage lists for password/user login authorisation
    all_users = []

    # call function
    credentials_users(all_users)

    task_container = []

    with open('tasks.txt', 'r') as read_tasks:

        for line in read_tasks:
            task_container.append(line)
        
    print('\nyour tasks with index:')
    
    task_count = 0
    for i in task_container:

        display_container = []
        display = i.split(',')

        for j in display:
            display_container.append(j.strip())
            
        display_template = f'''
        {task_container.index(i) + 1}.
        ------------------------------------------------------------------------------------------------------------------------------------
        assigned to: {display_container[0]}
        task title: {display_container[1]}
        task description: {display_container[2]}
        assignment date: {display_container[3]}
        due date: {display_container[4]}
        completed: {display_container[5]}
        ------------------------------------------------------------------------------------------------------------------------------------
        '''

        # additional condition to only display 
        # tasks with the logged in user as assigned to
        if display_container[0] == user_name:
            print(display_template)
            task_count += 1

    if task_count != 0:

        # flag to handle while loop end
        task_view = True

        # process task container to access info better
        task_components_container = []

        for i in task_container:

            task_components_container.append(i.split(','))

        while task_view:
            # vm view to select sepcific tasks
            vm_view = f'''
            ---------------------------------------
            hello {user_name}

            please enter the index of the specific 
            task you'd like to view

            '-1' - close view mine
            ---------------------------------------
            '''

            display_selection = input(vm_view)

            try:
                if user_name == task_components_container[int(display_selection) - 1][0]:
                    print(f'\nyou\'ve chosen task {display_selection}')

                    editing = True

                    while editing:

                        edit_selection = input(f'''
                        ------------------------------------------------------------------------------------------------------------------------------------
                        assigned to: {task_components_container[int(display_selection) - 1][0].strip()}
                        task title: {task_components_container[int(display_selection) - 1][1].strip()}
                        task description: {task_components_container[int(display_selection) - 1][2].strip()}
                        assignment date: {task_components_container[int(display_selection) - 1][3].strip()}
                        due date: {task_components_container[int(display_selection) - 1][4].strip()}
                        completed: {task_components_container[int(display_selection) - 1][5].strip()}

                        '1' - mark as complete
                        '2' - edit the task
                        's' - select another task
                        ------------------------------------------------------------------------------------------------------------------------------------
                        ''')

                        if edit_selection == '1':
                            if task_components_container[int(display_selection) - 1][5].strip() == 'No':
                                # read exisitng file
                                # advice on changing a particular line in a file: https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
                                with open('tasks.txt', 'r') as existing_tasks:
                                    
                                    data = existing_tasks.readlines()

                                data[int(display_selection) - 1] = (
                                        task_components_container[int(display_selection) - 1][0].strip() + ', '
                                        + task_components_container[int(display_selection) - 1][1].strip() + ', '
                                        + task_components_container[int(display_selection) - 1][2].strip() + ', '
                                        + task_components_container[int(display_selection) - 1][3].strip() + ', '
                                        + task_components_container[int(display_selection) - 1][4].strip() + ', '
                                        + 'Yes\n'
                                )
                                
                                # writing to tasks file
                                with open('tasks.txt', 'w') as register_edits:
                                    
                                    register_edits.writelines(data)
                                    print('\nyour task has been marked complete')
                                    task_view = False
                                    editing = False
                            
                            else:
                                print('task already marked complete')

                        elif edit_selection == '2':

                            if task_components_container[int(display_selection) - 1][5].strip() == 'No':
                                print('\nyou are only permitted to edit the task \'assigned to\', and \'due date\'')

                                assigned_to_replace = input('\nplease enter who this task is assigned to: ')
                                due_date_replace = input('please enter a due date in the following format (e.g. \'10 October 2021\'): ')

                                while assigned_to_replace not in all_users:
                                    assigned_to_replace = input('\nthat username is not in use. please enter a valid username: ')

                                with open('tasks.txt', 'r') as existing_tasks:
                                    
                                    data = existing_tasks.readlines()

                                data[int(display_selection) - 1] = (
                                        assigned_to_replace.strip() + ', '
                                        + task_components_container[int(display_selection) - 1][1].strip() + ', '
                                        + task_components_container[int(display_selection) - 1][2].strip() + ', '
                                        + task_components_container[int(display_selection) - 1][3].strip() + ', '
                                        + due_date_replace.strip() + ', '
                                        + task_components_container[int(display_selection) - 1][5].strip() + '\n'
                                )
                                
                                # writing to tasks file
                                with open('tasks.txt', 'w') as register_edits:
                                    
                                    register_edits.writelines(data)
                                    print('\nyour task has been edited')
                                    task_view = False
                                    editing = False


                            elif task_components_container[int(display_selection) - 1][5].strip() == 'Yes':
                                print('\nyou cannot edit a completed task')

                        elif edit_selection == 's':
                            editing = False

                        else:
                            print('\nplease make a valid selection')

                
                elif (int(display_selection) - 1) in range(len(task_container)):
                    print('\nindex does not correspond to a task assigned to you, try again')

                elif display_selection == '-1':
                    # return to main menu
                    task_view = False

                else:
                    print('\nout of task index range, try again')

            except:
                print('\nout of task index range, try again')
    
    else:
        print('\nyou have no tasks assigned to your username')

# function for admin console
def admin_con(user_name):
    # again restricting acces to admin credentials only
    if user_name == 'admin':
        # call function
        gen_report()
        print('\nhere\'s both the task overview and user overview reports')

        with open('task_overview.txt', 'r') as task_report:
            for line in task_report:
                print(line)
        
        with open('user_overview.txt', 'r') as user_report:
            for line in user_report:
                print(line)

    else:
        # message for acccess denail if not admin profile
        print(f'\n\'{user_name}\' does not possess admin rights. access denied')

# generate report function
def gen_report():
    # begin by consolidating user and task files
    # create display template for txt files
    with open('tasks.txt', 'r') as tasks_db:

        all_tasks = tasks_db.readlines()

    all_tasks_components = []

    for i in all_tasks:
        all_tasks_components.append(i.split(','))

    complete_count = 0

    for i in all_tasks_components:
        if i[5].strip() == 'Yes':
            complete_count += 1
    
    # https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
    today = date.today()
    task_overdue = 0

    month_dict_rev = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }

    # getting our task due date into format to manipulate
    # with datetime package
    for i in all_tasks_components:
        due_date_raw = i[4].split()
        due_date_processed = date(int(due_date_raw[2].strip()), month_dict_rev[due_date_raw[1].strip()], int(due_date_raw[0].strip()))

        date_delta = today - due_date_processed

        # ref for date delta conditional: https://stackoverflow.com/questions/25325882/python-time-difference-in-if-statements
        if (date_delta.days >= 0) and i[5].strip() == 'No':
            task_overdue += 1

    task_report_template = f'''
    ---------------------------------------
    tasks overview

    {len(all_tasks)} total tasks
    {complete_count} tasks marked completed
    {len(all_tasks) - complete_count} task still incomplete
    {task_overdue} tasks incomplete and overdue
    {round(100 * (len(all_tasks) - complete_count) / len(all_tasks))}% tasks incomplete
    {round(100 * task_overdue / len(all_tasks))}% tasks overdue
    ---------------------------------------
    '''

    with open('task_overview.txt', 'w') as task_report:

        task_report.write(task_report_template)


    # declare storage lists for password/user login authorisation
    all_users = []

    # open file instance to access user.txt for login
    credentials_users(all_users)

    user_report_template = f'''
    ---------------------------------------
    user overview

    {len(all_users)} total users on platform
    {len(all_tasks)} total tasks
    ---------------------------------------
    '''

    with open('user_overview.txt', 'w') as task_report:

        task_report.write(user_report_template)
    
    for i in all_users:

        task_assinged = 0
        tasks_assigned_complete = 0
        individual_task_overdue = 0

        for j in all_tasks_components:
            if i == j[0].strip():
                task_assinged += 1
            
            if i == j[0].strip() and j[5].strip() == 'Yes':
                tasks_assigned_complete += 1

            due_date_raw = j[4].split()
            due_date_processed = date(int(due_date_raw[2].strip()), month_dict_rev[due_date_raw[1].strip()], int(due_date_raw[0].strip()))

            date_delta = today - due_date_processed

            if i == j[0].strip() and j[5].strip() == 'No' and (date_delta.days >= 0):
                individual_task_overdue += 1

        # for the users with no assigned tasks
        if task_assinged == 0:

            individual_template = f'''
            ---------------------------------------
            {i}

            0 tasks assinged to user
            ---------------------------------------
            '''
            with open('user_overview.txt', 'a') as task_report:

                task_report.write(individual_template)

        # for users with assigned tasks
        else:
            individual_template = f'''
            ---------------------------------------
            {i}

            {task_assinged} tasks assinged to user
            {round(100 * task_assinged / len(all_tasks))}% of total tasks assigned to user
            {round(100 * tasks_assigned_complete / task_assinged)}% of assinged tasks completed
            {100 - round(100 * tasks_assigned_complete / task_assinged)}% of tasks assigned not completed
            {round(100 * individual_task_overdue / task_assinged)}% of tasks assigned not completed and overdue
            ---------------------------------------
            '''
            with open('user_overview.txt', 'a') as task_report:

                task_report.write(individual_template)
