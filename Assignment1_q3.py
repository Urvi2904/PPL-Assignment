#Build an application that can be used to block certain websites from opening.
#RUN AS ROOT >>sudo python3 q3.py
#To view file, run cat as root.
#To unblock, run rm as root.

file_path = "/etc/hosts"
redirect_ip = "127.0.0.1"
website = str(input("Enter the website you want to block.\n"))
#context manager
with open(file_path, 'r+') as file :
	cont = file.read()
	if website in cont :
		print("Website is already blocked.\n")
		pass
	else :
		file.write(redirect_ip + " " + website + "\n")
		print("Website blocked.\n")
		
	
