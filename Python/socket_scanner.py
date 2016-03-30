# coding: utf-8

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)

# Set time-out to get the scanning fast
socket.setdefaulttimeout(0.5)

# Ask for input
remote_server = raw_input("Enter a remote host to scan:")
remote_server_ip = socket.gethostbyname(remote_server)

# Print a nice banner with info on which host we are about to scan
print '-' * 60
print 'Please wait, scanning remote host ', remote_server_ip
print '-' * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports(1 - 1024)
# We also put in some error handling for catching errors
try:
    for port in range(1,1025):
        sock = socket.socket(2,1) # 2:socket.AF_INET 1:socket.SOCK_STREAM
        res = sock.connect_ex((remote_server_ip,port))
        if res == 0:
            print 'Port {}: OPEN'.format(port)
        sock.close()

except KeyboardInterrupt:
    print 'You pressed Ctrl+C !'
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved.Exiting'
    sys.exit()

except socket.error:
    print "Could't connect to the server"
    sys.exit()

# Check the time now
t2 = datetime.now()

# Calculates the difference of time
total = t2 - t1

# Print the info to screen
print 'Scanning Completed in: ', total

