#!/usr/bin/python
# Download the high-res Astronomy Picture of the Day
# and adds its title at the top of the image
#
# usage:
# ./apod.py path/to/save/image/to
# C. Ladroue

import urllib2
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re
import Image, ImageDraw, ImageFont
import sys
import os
from datetime import date

def download(url,filename):
	""" download the binary file at url """
	instream=urlopen(url)
	outfile=open(filename,'wb')
	for chunk in instream:
		outfile.write(chunk)
	instream.close()
	outfile.close()

def makeFilename(url):
	""" Turns the url into a filename by replacing possibly annoying characters by _ """	
	for c in ['/', ':', '?', '#', '&','%']:
		url=url.replace(c,'_')
	return url

def AddTitle(filename,title):
	try:
		im=Image.open(filename)
		szx,szy=im.size
		font=ImageFont.truetype("Arial.ttf", 40) # modify this to the actual location of arial.ttf 
		(tmp,bw)=font.getsize(title)
		bw=bw+5	
		im=im.transform((szx,szy+bw),Image.EXTENT,(0,-bw,szx,szy))
		draw=ImageDraw.Draw(im)	
		draw.text((5,5),title,fill="rgb(255,255,0)",font=font)
		del draw
		im.save(filename)
	finally:
		pass

if __name__=="__main__":
	try:
		dest=sys.argv[1]
	except Exception, err:
		dest='.'
	filename=dest+'/apod_'+date.today().strftime('%Y%m%d')+'.jpg'
	doc= urllib2.urlopen('http://antwrp.gsfc.nasa.gov/apod/astropix.html')
	print "Page is downloaded"
	soup = BeautifulSoup(doc)
	img=soup.find("center").findAll("a")
	url=img[1]['href']
	print ' From: http://antwrp.gsfc.nasa.gov/apod/'+url+' to '+ filename
	download('http://antwrp.gsfc.nasa.gov/apod/'+url,filename)
	title=soup.find("b").string
	AddTitle(filename,title)

