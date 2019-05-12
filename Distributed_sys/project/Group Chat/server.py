from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import queue
# Restrict to a particular path.

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# This class defines the variables stored on server:
class ServerDataContainer:
    user_id = 1
    user_list = []


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler,
                        allow_none=True,
                        logRequests=False) as server:

    server_data_container = ServerDataContainer()

    # Score : public
    # regist_new_user:
    # create a new user with name 'user_name', id number 'user_id', 
    # and store it into user_list.

    def regist_new_user(user_name):
        # Every user_id is unique
        user_id = server_data_container.user_id

        #Regist:
        info_container = {'user_id': user_id, 'user_name': user_name, 'message_queue':queue.Queue()}

        #Add to user_list
        server_data_container.user_list.append(info_container)
        server_data_container.user_id += 1
        
        #For Debug
        print('New User : User id:', user_id, 'User Name:', user_name)

        return user_id
    
    # Score : public
    # user_leave:
    def user_leave(user_id):
        #remove user from user_list
        for user in server_data_container.user_list:
            if user['user_id'] == user_id:
                message = user['user_name'] + ' left group chat.'

                print(message)

                # Send message to other user
                inform_user_leave(user_id, message)

                # User leave
                server_data_container.user_list.remove(user)
                display_remaining_user()
                break

        

    # Score : public
    # send_message:
    def send_message(user_id, user_message):
        #for all user(except user_id), add the message into their message_queue;
        for user in server_data_container.user_list:
            if user['user_id'] == user_id:
                user_name = user['user_name']
                break

        format_msg = format_user_message(user_name, user_message)

        for user in server_data_container.user_list:
            if user['user_id'] != user_id:
                user['message_queue'].put(format_msg)

    # Score : public
    # display_message:
    def display_message(user_id):
        for user in server_data_container.user_list:
            if user['user_id'] == user_id:
                message_list = []
                while not user['message_queue'].empty():
                    message_list.append(user['message_queue'].get())
        return message_list

    server.register_function(user_leave, 'user_leave')    
    server.register_function(regist_new_user, 'regist_new_user')
    server.register_function(send_message, 'send_message')
    server.register_function(display_message, 'display_message')

    # Score : private 
    # format_user_message
    def format_user_message(user_name, user_message):
        return '<' + user_name + '>: ' + user_message

    # Score : private 
    # format_leave_message
    def format_leave_message(leave_message):
        return '<System>: ' + leave_message

    # Score : private
    # inform_user_leave
    def inform_user_leave(user_id, user_message):

        format_msg = format_leave_message(user_message)

        for user in server_data_container.user_list:
            if user['user_id'] != user_id:
                user['message_queue'].put(format_msg)

    # Score : private
    # display_remaining_user
    def display_remaining_user() :
        for user in server_data_container.user_list:
            print("Remaining user: User id:", user['user_id'], "User Name:", user["user_name"])

    # Run the server's main loop
    server.serve_forever()