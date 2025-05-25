"""
File:   the_internet.py
Author:  Sakar Ojha
Date:    12/03/2024
Section: 71
E-mail:  o66@umbc.edu
Description:
    Finds the connected path from a server from starting point to its destination.
"""
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def create_server(server_name, ipv4_address, servers):
    '''
    Function Creates a server in a dictonary
    parameter: 
    server_name is the given name of the server by the user
    ipv4_address is the given address by the user
    servers is the dictionary consisting of all the servers name as the key as its associated...
      ip address as the value
    Returns:
    the servers which contains the new key as server's name and value as its ipv4 address.
    '''
    if server_name in servers:
        servers[server_name] = ipv4_address
        print(f'New ip of {ipv4_address} has been updated to {server_name}.')
    
    elif ipv4_address in servers.values():
        print(f'{ipv4_address} ip has already been made in the internet.')

    else:
        servers[server_name] = ipv4_address
        print(f'A new server with name {server_name} was created at ip {ipv4_address}')
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def check_ipv4(ipv4_address):
    '''
    Function checks if given ipv4 is valid or not
    parameter:
    ipv4_address is the given address
    returns: 
    True or False based on if there is any values of ip that exceed the range
    '''
    list_ipv4 = ipv4_address.split('.')

    for bit in list_ipv4:
        if not (int(bit) >= 0 and int(bit) <= 255):
            return False
    return True
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def create_connection(server_1, server_2, connect_time, network, servers):
    '''
    Function creates connection given two unique servers with their associated connect_time
    Parameters:
    server_1 is name of the server_1
    server_2 is name of the server 2
    connect_time is time between those servers in milliseconds
    network is 2d dictionary containing server connections and time in milliseconds
    servers is a dictionary with all the server names and ips
    Returns: 
    Updated Network with the two servers connected
    '''
    if not ((server_1 in servers) and (server_2 in servers)):
        print('Error, No Such Server Found!')
    else:
        # server_2 will automatically be connected to server_1 since connections are bidirectional
        if (server_1 in network) and (server_2 in network[server_1]):
            print('This server connection already exists.')
        else:
            if (server_1 in network):
                network[server_1].update({server_2: int(connect_time)})
                if (server_2 in network):
                    network[server_2].update({server_1: int(connect_time)})
                else:
                    network[server_2] = {server_1: int(connect_time)}
            else:
                network[server_1] = {server_2: int(connect_time)}
                if (server_2 in network):
                    network[server_2].update({server_1: int(connect_time)})
                else:
                    network[server_2] = {server_1: int(connect_time)}
            print(f'Connection between {server_1} and {server_2} has been created.')
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def set_server(server_or_ip_choice, prev_server, servers):
    '''
    Function sers the server
    parameter: 
    server_choice is the choice of the server the user wants to be in
    prev_server which is the previous server 
    servers is the dictionary with all server names and ip's 
    Returns: 
    prev_server if the new server choice is not valid
    current_server if the choice is valid
    '''
    #values() will get all of the ip's (values) and check if the server_or_ip_choice if given ip, is in any of the dictionary values.
    
    if (server_or_ip_choice in servers):
        current_server = server_or_ip_choice #setting current_server equal to the choice
        print(f'Server {server_or_ip_choice} selected.')
    
    elif (server_or_ip_choice in servers.values()): 
        for key in servers:
            if servers[key] == server_or_ip_choice:
                current_server = key
                print(f'Server {current_server}  ip: {server_or_ip_choice} selected.')
      
    else:
        print(f'{server_or_ip_choice} is not connected to the Internet')
        return prev_server # THIS RETURNS THE PREVIOUS SERVER IF CHOICE WANST VALID
    
    return current_server
#print(set_server('porfavor.com', 'amazon.com', {'amazon.com':'10.8', 'porfavor.com': '20.2'}))
#------------------------------------------------------------------------------------------------------

def ip_to_name(ip, servers):
    '''
    Function converts ip to server's name
    parameter: 
    ip is the ip address
    servers is  a dictionary containing server name as the key and ip as its value'''
    for key in servers:
        if servers[key] == ip:
            server_name = key
            return server_name


#------------------------------------------------------------------------------------------------------
def ip_config(current_server, servers):
    '''
    Function displays the current position in the internet
    Parameter:
    current_server is the current server in the internet
    servers is a dictionary containing server name as the key and ip as its value
    No Returns
    '''
    print(f'Currently in the server {current_server}, IP: {servers[current_server]}.')
#------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------
def display_servers(servers, network):
    '''
    Function displays all the servers
    Parameters:
    servers is dictionary containing server name and IP
    network is dictionary containing server connections and time in milliseconds
    No Returns
    '''

    for server in servers:
        print(server, '\t', servers[server]) #server[server] is the IP
        #This is a double loop with network[server] having all of the server's nodes/connections 
        if server in network:
            for connection in network[server]: #Accesssing the connections on the server
                print('\t', connection, '\t' , servers[connection], '\t' , network[server][connection])

##display_servers({'amazon.com': '10.8', 'facebook.com': 'ip provided'} , {'amazon.com': {'facebook.com': 34, 'XO- Tatted': '20'}})
# #------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def traceroute(current_server, destination_server, network):
    '''
    Function creates a visited dictionary and calls the traceroute_rec() function. 
    Parameter: 
    current_server is the present server/ starting point
    destination_server is the endpoint
    network is dictionary containing server connections and time in milliseconds
  
    Returns: 
    output of the function traceroute_rec()
    '''
    visited = {}
    for server in network:
        visited[server] = False
    
    return traceroute_rec(current_server, destination_server, network, visited)

#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def traceroute_rec(current_server, destination_server, network, visited):
    '''
    Function Traces the route to the destination server based on where the current server is located
    Parameter: 
    current_server is the present server/ starting point
    destination_server is the endpoint
    network is dictionary containing server connections and time in milliseconds
    visited_list is a dictionary with the server_names all set to False in the very beginning
    Returns: 
    path if there is any
    '''
    path = [] # This list will contain our path if any was found
    if current_server == destination_server: #Base case if we reach the destination we start unfolding the recursions
        return [[current_server, None]] # We return destination_server as a 2D list to match our path data type 
    
    visited[current_server] = True #Setting the current_server as visited/ True

    for connection in network[current_server]:
        if not(visited[connection]):
            path = traceroute_rec(connection, destination_server, network, visited)
            if path: #If path list wasn't empty when the recursion returns then we create the path
                #network[current_server][connection] will return us the time in milliseconds for that server when unfolding
                return [[current_server, network[current_server][connection]]] + path #concateneting 2D lists
            
    return path #Returens empty if no path was found

#path = (traceroute('Node 1', 'Node 5',({'Node 1': {'Node 4': 10, 'Node 5': 22}, 'Node 2': {'Node 5': 90, 'Node 4' : 66}, 'Node 3': 0, 'Node 4': {'Node 1' : 7, 'Node 2': 66}, 'Node 5': {'Node 1': 2, 'Node 2':90 }})))
#print(path)

#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def print_traceroute(destination, path, servers):
    '''
    Function prints the route to users destination from current position
    Parameter:
    path is the 2d list containing the server's name in 0th index of each column and time to another server containing in 1th index of each column 
    No Returns
    '''
    if len(path) == 0:
        print(f'Path was not found for {destination}')
    else:
        print(f'Tracing route to {destination}') #Could be implemented on main function that runs the function***
        #### MAY NEED TO PUT A CASE FOR EMPTY PATH#####
        for i in range(len(path)):
            if i == 0:
                print(f'0 \t 0 \t {path[i][0]} \t [{servers[path[i][0]]}]') #servers[path[i]][0] gives the ip #Likewise path[i][1] has the ping value in milliseconds
            else:
                print(f'{i} \t {path[i-1][1]} \t {path[i][0]} \t [{servers[path[i][0]]}]') #servers[path[i]][0] gives the ip #Likewise path[i][1] has the ping value

# #print_traceroute('Home', path, ({'Node 1': 10.9, 'Node 4': 20, 'Node 2': 0, 'Node 5': 202}))   
#------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------
def ping(current_server, destination_server, network):
    '''
    Function creates a visited dictionary and calls the ping_rec() function. 
    Parameter: 
    current_server is the present server/ starting point
    destination_server is the endpoint
    network is dictionary containing server connections and time in milliseconds
  
    Returns: 
    output of the function ping_rec()
    '''
    visited = {}
    for server in network:
        visited[server] = False
    
    return ping_rec(current_server, destination_server, network, visited)

# #------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------
def ping_rec(current_server, destination_server, network, visited):
    '''
    Function Traces the route to the destination server and gets its ping
    Parameter: 
    current_server is the present server/ starting point
    destination_server is the endpoint
    network is dictionary containing server connections and time in milliseconds
    visited_list is a dictionary with the server_names all set to False in the very beginning
    Returns: 
    path if there is any 
    '''
    ping = [] # This list will contain oall our ping times as a list
    if current_server == destination_server: #Base case if we reach the destination we start unfolding the recursions
        return [0] # We return destination_server as a list to match our ping data type 
    
    visited[current_server] = True #Setting the current_server as visited/ True

    for connection in network[current_server]:
        if not(visited[connection]):
            ping = ping_rec(connection, destination_server, network, visited)
            if ping: #If path list wasn't empty when the recursion returns then we create the path
                #network[current_server][connection] will return us the time in milliseconds for that server when unfolding
                return [network[current_server][connection]] + ping #concateneting 2D lists
            
    return ping #Returens empty if no path was found
# #------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------
def print_ping(ping_list, destination):
  '''
  Function prints the route to users destination from current position
  Parameter:
  ping is the list containing the server's ping 
  No Returns
  '''
  if not ping_list: #if ping list is empty
      print(f'Path was not found for {destination}, we were unable to ping it.')
  
  else: # Adding the ping numbers from the list and then we print
      total_ping = 0
      for ping in ping_list:
          total_ping += ping
      print(f'Reply from {destination} time = {total_ping} ms') #Could be implemented on main function that runs the function***
    

# #ping = (ping('Node 1', 'Node 5',({'Node 1': {'Node 4': 10, 'Node 5': 22}, 'Node 2': {'Node 5': 90, 'Node 4' : 66}, 'Node 3': 0, 'Node 4': {'Node 1' : 7, 'Node 2': 66}, 'Node 5': {'Node 1': 2, 'Node 2':90 }})))
# #print(ping)
# #print_ping('Node 1', ping)
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
def internet_runner(): #Runner function
    
    servers = {}
    network = {}
    current_server = None

    user_input = input('Input Here: ').lower()
    

    while user_input != 'quit':
        user_input_elements = user_input.strip().split() #stripping the whitespaces and splitting each element(separated by whitespaces) into an array

        if user_input_elements[0] == 'create-server': #If user wants to create a serer
            ipv4 = user_input_elements[-1] #ip address is the last element of the list
            
            if check_ipv4(ipv4): # checks the ipv4 with the function, enters 'if' condition it is True , 'else' if it's false
                create_server(user_input_elements[1], user_input_elements[2], servers)
            else:
                print('That is not a valid IP address, range for each box must be from 0-255 inclusive')
        

        elif user_input_elements[0] == 'create-connection':
            #If user bychance forgets to enter somethings, we throw this before index error arises
            if len(user_input_elements) < 4: 
                print('Error not enough elements to continue.')
            else:
                server_1 = user_input_elements [1]
                server_2 = user_input_elements[2]
                connect_time = int(user_input_elements[3])

                create_connection(server_1, server_2, connect_time, network, servers) #Function call
        

        elif user_input_elements[0] == 'set-server':
            server_or_ip_choice = user_input_elements[1]
            current_server = set_server(server_or_ip_choice, current_server, servers) #Function call


        elif (user_input_elements[0] == 'traceroute') or user_input_elements[0] == 'tracert':
            destination_server = user_input_elements[1]
            
            if current_server == None: #If there is no starting point
                print('You have not set a server starting point, use: "set-server (starting server)"')

            elif (destination_server in servers.values()): #if the input is an ip address
                destination_server = ip_to_name(destination_server, servers)
                path = traceroute(current_server, destination_server, network) #Function call
                print_traceroute(destination_server, path, servers)  #Function call 
            else: #If input is server name
                path = traceroute(current_server, destination_server, network) #Function call
                print_traceroute(destination_server, path, servers)  #Function call 
  

        elif user_input_elements[0] == 'ping':
            destination_server = user_input_elements[1]
            
            if current_server == None: #If there is no starting point
                print('You have not set a server starting point, use: "set-server (starting server)"')

            elif (destination_server in servers.values()): #if the input is an ip address
                destination_server = ip_to_name(destination_server, servers)
                ping_list = ping(current_server, destination_server, network) #Function call
                print_ping(ping_list, destination_server) #Function call
            else:
                ping_list = ping(current_server, destination_server, network) #Function call
                print_ping(ping_list, destination_server) #Function call


        elif user_input_elements[0] == 'ip-config':
            ip_config(current_server, servers)


        elif user_input_elements[0] == 'display-servers':
            display_servers(servers, network)
            

        else:
            print('Not a valid input, Try again')

        # We let the user input again
        user_input = input('>>> ').lower()
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
     internet_runner()