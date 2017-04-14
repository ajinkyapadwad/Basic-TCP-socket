"""
	Python Server 
	AJINKYA PADWAD
	APRIL 2017
"""

import socket	#library
import struct
import time
import sys

host = 'localhost'	# IPv4 address
#port = 4000	# port number	
#port = 6000

port = sys.argv[1]
print sys.argv[0], sys.argv[1]
server_address = (sys.argv[0], int(sys.argv[1]))

if len(sys.argv) < 1:
	print ">>Please set a port"
	sys.exit()


print '------------------------ SERVER SIDE ----------------------'

T = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# socket creation
T.bind(server_address)				# associate the port with socket

print '		SERVER LISTENING ON ', host
print '		Waiting for Client...'

T.listen(10)							# act as server, connection sniffing
conn, addr = T.accept()					# connection address, wait for incoming connection

if not addr:
	print 'Connection Failed !'
	T.close()
else:
	print ' 	Connectd to Client @', host, ': ', port

print "-----------------------------------------------------------"

print ""

def get(variable):
	#try:
		if variable in ("testfile"):
			infile = open("testfile.txt")
			print "	Verifying file name ..."
		
			print " Reading file content..."
			text = infile.read()
			print " Sending file content..."
			infile.close()
			time.sleep(2)
			conn.sendall(text)
		elif variable in ("newintro"):
			newfile = open("newintro.txt")
			print "	Verifying file name ..."
		
			print " Reading file content..."
			text = newfile.read()
			print " Sending file content..."
			time.sleep(2)
			conn.sendall(text)
		else:
			text = "File not found !"
			print " File not found !"
			conn.sendall(text)
			# conn.close()
			# sys.exit()

	# except IOError:
	# 	print "Could not open file! "
	

def bounce(variable):
	print" Bouncing back to client !"
	conn.sendall(variable)
	conn.close()

def end(variable):
	print " Exit : ", variable
	T.close()
	sys.exit()

while 1:
	print ""
	print" -------------------------------------  "
	command = conn.recv(6)

	print " GOT COMMAND : ", command

	variable = conn.recv(8)

	print " GOT var : ", variable 

	if command in ("get", "GET"):
		get(variable)	
	elif command in ("BOUNCE", "bounce"):
		bounce(variable)
	elif command in ("EXIT", "exit"):
		if not variable:
			print "NORMAL EXIT"
			T.close()
			sys.exit()
		else:
			end(variable)	
	else:
		print " Invalid command ! Try again at client !"
T.close()

sys.exit()
