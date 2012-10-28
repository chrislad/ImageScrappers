#!/usr/bin/python
# Download today's picture from bing.com
# usage:
# ./bing.py path/to/save/image/to
# C. Ladroue

import urllib2
from urllib import urlopen
from datetime import date
import re
import sys

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
	doc=urllib2.urlopen('http://www.bing.com')
	content=doc.read()

	result=re.search(r"g_img={url:'([^']*)",content)
	if result is None:
		print "Didn't find the image url"
	else:
		result=result.groups(0)[0]
		result=result.replace('\\','')
		filename=dest+'/bing_'+date.today().strftime('%Y%m%d')+'.jpg'
		download('http://www.bing.com'+result,filename)

