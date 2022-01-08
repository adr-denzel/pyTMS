# really cleaed up the structre of the program following
# the initial iteration and the addidtional features
# requested in this task. really helped me figure out
# a method to better structure my work to be easily modified,
# totally reworked, or heavily added onto. best task yet!

# importing all my functions
from functions import reg_user, add_task, view_all, view_mine, admin_con, gen_report, credentials

# login procedure start
# declare lists for password/user login authorisation tests
user_list = []
password_list = []

# call function to process users and passwords in textfile
# returns user_list and password_list
credentials(user_list, password_list)

# initial message to user
intro_prompt = '''
before we begin, please login with
your unique username & password
'''

# output login prompt
print(intro_prompt)

# request user inputs to test login credentials
session_name = input('username: ')
session_password = input('password: ')

# declare initial state of user verification flag
session_verified = False

# initiate while loop to run until login is successful
while not session_verified:

    # first to ensure a valid username is entered
    if session_name in user_list:

        # if password and username match for the same index 
        for i in range(len(user_list)):
            if session_name == user_list[i] and session_password == password_list[i]:
                # flag changes, while will break
                session_verified = True
                
        if session_verified:
            # user verrification message
            print('\nlogin successful')

        else:
            # login failure for incorrect password, loop re-runs
            print('\npassword invalid. please try again\n')
            session_name = input('username: ')
            session_password = input('password: ')
    
    else:
        # as soon as a username is not valid, re-run loop
        print('\nusername invalid. please try again\n')
        session_name = input('username: ')
        session_password = input('password: ')

# while our user session is live
while session_verified:
    # menu template
    selection_prompt = '''
    ---------------------------------------
    please select one of the following:

    'r' (admin only) - register user
    'ds' (admin only) - admin console
    'gr' - generate reports
    'a' - add task
    'va' - view all tasks
    'vm' - view my tasks
    'e' - exit
    ---------------------------------------
    : '''
    
    # request user selection
    selection = input(selection_prompt).lower()

    # register new users
    if selection == 'r':
        reg_user(session_name)

    # display user and task reports
    elif selection == 'ds':
        admin_con(session_name)

    # add tasks
    elif selection == 'a':
        add_task()

    # view all tasks
    elif selection == 'va':
        view_all()
            
    # view session_name tasks
    elif selection == 'vm':
        view_mine(session_name)
    
    # generate reports
    elif selection =='gr':
        gen_report()
        print('\nyou generated reports!')

    # terminate session
    elif selection == 'e':
        print(f'\nsession end. \'{session_name}\' logged out\n')
        # hot tip: https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481
        exit()
    
    # handling non-menu inputs
    else:
        print('\nplease make a valid selection')
