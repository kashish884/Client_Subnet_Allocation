'''
Python Version used: 3.7
Authors: Dhanraj Vedanth Raghunathan, Kashish Singh
Modules used: re, ipaddress, time
'''
import re
import ipaddress
import time

class Killersubnet:
	
	def __init__(self):
		self.ip_list_generated = []
		self.ip_list_dict = {}
		self.count = 0
		self.final_dict = {}
		self.flag = 0
		self.cust_count = 0
		print('''***********************************************************
                     IP ALLOCATOR                         
												
  Takes in a class B Network and a subnet and splits it  
  to your need! Multiple separate allocations can be done.
***********************************************************''')
		print("\n\n")

	def validity_check(self):

		ip_addr = input("Enter a valid class B IP NETWORK address!\n")

		octets = ip_addr.split('.')
		# print(octets[0])

		if ((len(octets) == 4) and (int(octets[0]) != 0 ) and (int(octets[0]) != 127) and (128 <= int(octets[0]) <= 191)
		 and ( 0 <= int(octets[1]) <= 254) and (int(octets[2]) == 0 ) and (int(octets[3]) == 0)):
			print("IP Address is Valid\n Now enter the subnet mask when prompted!\n")
			self.flag = 1
		else:
			print("Invalid IP entered, please re-enter a network address it.")
			self.validity_check()
			self.flag = 0
		if (self.flag == 1):
			cidr = input("Enter the subnet mask for the entered class B IP address:" + ip_addr + "\n")
			if (16 <= int(cidr) <= 32):
				total = ipaddress.ip_network(str(ip_addr) + '/' + str(cidr))
				print("The subnet mask is: " + str(total.netmask))
				usable_ips = total.hosts()
				print("Usable IPs are:")
				for ip in usable_ips:
					self.ip_list_generated.append(str(ip))
					self.count += 1
					self.ip_list_dict[self.count] = str(ip)
				print(self.count)
				print(self.ip_list_generated)
				print(self.ip_list_dict)

	def ask_user(self):
		ips_to_assign = input("Enter the number of IPs need to be allocated:\n")

		if (int(ips_to_assign) > int(self.count)):
			print("Asking for more than available!!\n Available:" + str(self.count)
			 + "\nYou asked for:" + str(ips_to_assign) + "\n")
			self.ask_user()
		else:
			print("Working on it...")
			time.sleep(1)

			temp_list_to_assign = self.ip_list_generated[:(int(ips_to_assign))]
			print("Allocating these IPs for you!:\n")
			print(temp_list_to_assign)
			self.cust_count += 1
			self.final_dict[self.cust_count] = temp_list_to_assign

			temp_list_remaining_ips = self.ip_list_generated[int(ips_to_assign):]
			self.ip_list_generated = temp_list_remaining_ips
			print("Remaining IPs are:")
			self.count = self.count - int(ips_to_assign)
			print(self.count)c
			print(self.ip_list_generated)
			if (self.count == 0):
				print("All available IPs have been allocated!\n")
				print("Here is a summary of the allocations:\n")
				for key,value in self.final_dict.items():
					print("Customer:" + str(key) +"\nIPs:" + str(value))
			else:
				self.ask_again()

	def ask_again(self):
		getval = input("Do you require further IPs at this moment? (Yy/Nn)")
		if ((getval == 'Y') or (getval == 'y')): 
			self.ask_user()
		elif ((getval == 'N') or (getval == 'n')):
			print("Here is a summary of the allocations:\n")
			for key,value in self.final_dict.items():
				print("Customer:" + str(key) +"\nIPs:" + str(value))
			print("Thank you, have a good one.")
			exit()
		else:
			print("Enter (Yy/Nn), nothing else")
			self.ask_again()

instance1 = Killersubnet()
instance1.validity_check()
instance1.ask_user()















