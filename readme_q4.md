# IP Allocator

A sophisticated python script to help an enterprise engineer assign IPs to a customer given a fixed Class B Network ID in hand.

## Description

- This script takes in the Network ID, the subnet mask and the number of IPs to assign to a host on a loop basis.
-  This script checks for the validity of the Network ID as well as the subnet mask.
-  It checks for the case when the engineer requests for more IPs than available.
-  The engineer has the flexibility to assign IPs to multiple customers over the same session.
-  The script ends by printing a summary containing the IPs allocated for every customer.

## Modules used
- ipaddr
- re
- time

## Usage

- Open the terminal and navigate to the directory in which the script resides.
- Run the python script using the command : python3 LAB_Q4.py
- An interactive interface where the user is prompted for details appears on the shell.

# Sample output
        Dhanrajs-MacBook-Pro:SNM draghun$ python3 LAB_Q4.py
        ***********************************************************
                             IP ALLOCATOR
        
          Takes in a class B Network and a subnet and splits it
          to your need! Multiple separate allocations can be done.
        ***********************************************************
        
        
        
        Enter a valid class B IP NETWORK address!
        172.16.1.0
        Invalid IP entered, please re-enter a network address it.
        Enter a valid class B IP NETWORK address!
        172.16.0.0
        IP Address is Valid
         Now enter the subnet mask when prompted!
        
        Enter the subnet mask for the entered class B IP address:172.16.0.0
        28
        The subnet mask is: 255.255.255.240
        Usable IPs are:
        14
        ['172.16.0.1', '172.16.0.2', '172.16.0.3', '172.16.0.4', '172.16.0.5', '172.16.0.6', '172.16.0.7', '172.16.0.8', '172.16.0.9', '172.16.0.10', '172.16.0.11', '172.16.0.12', '172.16.0.13', '172.16.0.14']
        {1: '172.16.0.1', 2: '172.16.0.2', 3: '172.16.0.3', 4: '172.16.0.4', 5: '172.16.0.5', 6: '172.16.0.6', 7: '172.16.0.7', 8: '172.16.0.8', 9: '172.16.0.9', 10: '172.16.0.10', 11: '172.16.0.11', 12: '172.16.0.12', 13: '172.16.0.13', 14: '172.16.0.14'}
        Enter the number of IPs need to be allocated:
        10
        Working on it...
        Allocating these IPs for you!:
        
        ['172.16.0.1', '172.16.0.2', '172.16.0.3', '172.16.0.4', '172.16.0.5', '172.16.0.6', '172.16.0.7', '172.16.0.8', '172.16.0.9', '172.16.0.10']
        Remaining IPs are:
        4
        ['172.16.0.11', '172.16.0.12', '172.16.0.13', '172.16.0.14']
        Do you require further IPs at this moment? (Yy/Nn)y
        Enter the number of IPs need to be allocated:
        10
        Asking for more than available!!
         Available:4
        You asked for:10
        
        Enter the number of IPs need to be allocated:
        3
        Working on it...
        Allocating these IPs for you!:
        
        ['172.16.0.11', '172.16.0.12', '172.16.0.13']
        Remaining IPs are:
        1
        ['172.16.0.14']
        Do you require further IPs at this moment? (Yy/Nn)y
        Enter the number of IPs need to be allocated:
        1
        Working on it...
        Allocating these IPs for you!:
        
        ['172.16.0.14']
        Remaining IPs are:
        0
        []
        All available IPs have been allocated!
        
        Here is a summary of the allocations:

Customer:1
IPs:['172.16.0.1', '172.16.0.2', '172.16.0.3', '172.16.0.4', '172.16.0.5', '172.16.0.6', '172.16.0.7', '172.16.0.8', '172.16.0.9', '172.16.0.10']
Customer:2
IPs:['172.16.0.11', '172.16.0.12', '172.16.0.13']
Customer:3
IPs:['172.16.0.14']

# Version
 - 1.0

Authors
----
Dhanraj Vedanth Raghunathan, Kashish Singh

# License

  - All rights reserved by the owner and NC State University.
  - Usage of the script can be done post approval from the above.