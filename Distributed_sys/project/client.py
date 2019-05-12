import xmlrpc.client
import select
import sys
import time


# This function check whether user input something or not.
def user_input_message():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

# When user type quit_msg, user will exit from chat.
quit_msg = 'quit'

#Set server
server = xmlrpc.client.ServerProxy('http://localhost:8000')

#Rigster self as a new client
print('Input your name:')
user_name = sys.stdin.readline().strip()
try:
    user_id = server.regist_new_user(user_name)
except:
    print('Server Closed.')
    sys.exit()

print('User id:', user_id, 'User Name:', user_name)
print('You can start chatting now!')

while True:

    time.sleep(1)
    try:
        message_list = server.display_message(user_id)
    
        for message in message_list:
            print(message)
        #TODO : add info when new user enter the chatting room
        # server.notify_new_user_enter()
    except:
        print('Server Closed.')
        sys.exit()



    # If user input some message and press <Enter> Key.
    if user_input_message():

        user_message = sys.stdin.readline().strip()

        if user_message == quit_msg:         
            print('Exit chat room')
            server.user_leave(user_id)
            sys.exit()
        else:
            print('<You>:', user_message)
            server.send_message(user_id, user_message)
