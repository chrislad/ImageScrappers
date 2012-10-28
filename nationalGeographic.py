#!/usr/bin/python
# Download today's picture from http://photography.nationalgeographic.com/photography/photo-of-the-day/
#
# usage:
# ./nationalGeographic.py path/to/save/image/to
# C. Ladroue

import urllib2
from urllib import urlopen
import re
from datetime import date
import sys
import os


def download(url,filename):
	""" download the binary file at url """
	instream=urlopen(url)
	outfile=open(filename,'wb')
	for chunk in instream:
		outfile.write(chunk)
	instream.close()
	outfile.close()

if __name__=="__main__":
	try:
		dest=sys.argv[1]
	except Exception, err:
		dest='.'
	filename=dest+'/natgeo_'+date.today().strftime('%Y%m%d')+'.jpg'

	doc=urllib2.urlopen('http://photography.nationalgeographic.com/photography/photo-of-the-day')
	content=doc.read()

	# search for wallpaper link
	result=re.search("<div class=\"download_link\">.*?<a href=\"(.*?)\".*?<\/div>",content,re.DOTALL)
	if result is None:
		result=re.search("<div class=\"primary_photo\">.*?<img src=\"(.*?)\".*?<\/div>",content,re.DOTALL)  # search for main link
	if result is None:
		print "Didn't find the image, sorry."
	else:
		imageURL=result.group(1)
		print imageURL
		print "to"
		print filename
		download(imageURL,filename)
