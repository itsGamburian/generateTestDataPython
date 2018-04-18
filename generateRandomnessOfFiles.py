#######################
# Hambartzum Gamburian
# randomfilegenerator.py
# Generate random test data for C# unit testing
#######################

import md5
import os

fileSize_kBytes = input("Enter file size in kilobytes: ")
filesize_bytes 	= 1024 * fileSize_kBytes 										# Thousands of random data
outdir 		= "./output" 														# Ouput directory
numFiles_input = input("Enter number of files to generate in thousands: ")
numfiles 	= 1024 * numFiles_input												# Number of files to generate

m = md5.new()

DirHash_L1 = {}  	
DirHash_L2 = {}  	

for x in range(0, numfiles):
     randomdata = os.urandom(filesize_bytes)
     m.update(randomdata) 
     																			# Generate md5 digest of random bytes
     hash = m.hexdigest()

     																			# Get the first 2 chars of the hex digest as 1st level
     first_level = hash[:2]

     																			# Secondlevel 
     second_level = hash[2:4]

     path = outdir + "/" + first_level + "/" + second_level
     if not os.path.exists(path):
          os.makedirs(path)

     with open(os.path.join(path, hash), 'wb') as temp_file:
          temp_file.write(randomdata)

     DirHash_L1[first_level] = 1
     DirHash_L2[first_level + second_level] = 1

     if (x % 1000) == 999:
	print "Generated " + str(x+1) + " files so far"

print "============================="
print "Total Files: " + str(numfiles)
print " Total Dirs: " + str(len(DirHash_L1.keys()) + len(DirHash_L2.keys()))
