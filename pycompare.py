#!/usr/bin/python
import os
from bs4 import BeautifulSoup

def getfiles(path1, path2):
	
	#Load files on root of path1 on files1
	for root, dir, names in os.walk(path1):
		files1 = names
		break #Will break the for to read just the root folder

	#Load files on root of path2 on files2
	for root, dir, names in os.walk(path2):
		files2 = names
		break #Will break the for to read just the root folder


	#Compares the two list of files and select files with the same name on both paths
	interfiles = set(files1).intersection(files2)

	#Select just HTML files on mylist
	mylist = [ fi for fi in interfiles if fi.endswith('.html')]


	print '\nI will check:', len(mylist), 'files in total... HOLD ON!\n'
	return mylist


def checkcontent(path1, path2):
	
	#Get files from both paths
	mylist = getfiles(path1, path2)

	difcontent = 0
	diftitles = 0
	titles = []
	notitles = []

	print '='*50
	print 'Files With Different Content'
	print '='*50

	
	for files in mylist:

		#Select files on path1 and add them to the sooup
		htmlDoc = open (path1+files, 'r+')
		soup1 = BeautifulSoup(htmlDoc.read())

		#Select div class description inside div class bodytext
		find1 = soup1.select('.bodytext .description')

		#Select H3 tags
		header1 = soup1.h3

		#Select files on path2 and add them to the sopu
		htmlDoc = open (path2+files, 'r+')
		soup2 = BeautifulSoup(htmlDoc.read())
		
		#Select div class description inside div class bodytext
		find2 = soup2.select('.bodytext .description')

		#Select H1 tag
		header2 = soup2.h1

		#Check if the are H1 and H3 tags
		if (header2 == None or header1 == None):
			notitles.append(files)

		#Compares headers
		else:
			for headers in header1:
				h1 = headers
			for headers2 in header2:
				h3 = headers2
			if not h1 == h3:
				titles.append(files)
				diftitles += 1

		#Read lines on HTML files
		for lines1 in find1:
			l = lines1
		for lines2 in find2:
			n = lines2

		#Compares content
		if not l == n:
			print files
			difcontent += 1

	#Print results
	print '\n'
	print '='*50
	print 'Files With No Title'
	print '='*50

	for lines in notitles:
		print lines

	print '\n'
	print '='*50
	print 'Files With Different Titles'
	print '='*50

	for lines in titles:
		print lines

	print "\nI've found", difcontent, 'files with different content'
	print "I've found", diftitles, 'different titles'




def main():
	
	mypath = "PATH_TO_FOLDER1"
	mypath2 = "PATH_TO_FOLDER2"

	checkcontent(mypath, mypath2)


if __name__ == "__main__":
    main()

