"""
	Python Client 
	AJINKYA PADWAD
	APRIL 2017
"""

import socket
import struct
import time
import sys

# ------------------- SETUP ------------------------------------- 

#host = '127.0.0.2'
#host = 'localhost'
#port = 4000
#port = 6000

host = sys.argv[1]
port = sys.argv[2]

if len(sys.argv) < 2:
    print "Please set a hostname / port"
    sys.exit()

time.sleep(1)


NewSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

NewSocket.connect((host,port))

print '---------------------- CLIENT SIDE ----------------------'

print "		Connected to Server @ ", host, ': ', port

print "---------------------------------------------------------"

print "	List of commands : "
print "> GET filename"
print "> BOUNCE message"
print "> EXIT exitcode"
print "> EXIT "

print "---------------------------------------------------------"

print " Available files : "
print " 1. intro.txt"
print " 2. testfile.txt"
print ""

while(1):
		variable = 1
		command = 1
		print ""
		command, variable = raw_input("\n	Enter command >> ").split(" ") 
		#print ">>",command,",",variable
		if command in ("get", "GET"):
		 	wrapper = struct.Struct('!' + '3s')		
		elif command in ("BOUNCE", "bounce"):
			wrapper = struct.Struct('!' + '6s')
		elif command in ("EXIT", "exit"):
			wrapper = struct.Struct('!' + '4s')
		# elif command is 1:
		# 	print '>>Invalid command, try again !'
		# 	continue	
		else :
			print '>>Invalid command, try again !'
			continue

		packet = wrapper.pack(command)
		NewSocket.sendall(packet)

		time.sleep(1)

		wrapper = struct.Struct('!' + '8s')
		packet = wrapper.pack(variable)
		NewSocket.sendall(packet)


		if command in ("get", "GET"):
			text = NewSocket.recv(1024)
			print""
			print ">>RECEIVED : "
			print text

		elif command in ("BOUNCE", "bounce"):
			back = NewSocket.recv(20)
			print ">>RECEIVED : ", back

		elif command in ("EXIT", "exit"):
			time.sleep(2)
			if variable is 1:
				print "NORMAL EXIT"
			else:
				print " EXIT ", variable
			T.close()
			sys.exit()	

	# except:
	# 	print '>Invalid input(s), try again !'

socket.close()
sys.exit()



