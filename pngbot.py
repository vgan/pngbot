#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from subprocess import Popen,PIPE,STDOUT
import time
import os
from shutil import copyfile
import random
import re
from random import randint
from time import sleep
import urllib
import mmap
import hashlib
# TODO: get wand working for converting and compositing
#from wand.image import Image
#from wand.image import COMPOSITE_OPERATORS
#from wand.color import Color
import pytumblr
from pngbot_keys import *

client = pytumblr.TumblrRestClient(tumblr_consumer_key, tumblr_consumer_secret, tumblr_token, tumblr_token_secret)
auth = tweepy.OAuthHandler(twitter_consumer_key,twitter_consumer_secret)
auth.set_access_token(twitter_token,twitter_token_secret)
api = tweepy.API(auth)
image_bots_list = api.list_members('vgan', 'image-bots', -1) # whitelist for image bots

basedir = "/home/vgan/pngbot/" # set your base dir here
png0 = "png0.png"
png1 = "png1.png"
default = "default.png"
me = "pngbot"
emoji_padlock = unicode('\xF0\x9F\x94\x92', 'utf-8')
prefix = "@"
suffix = " " 
thementions = " "
images = [ png0, png1]
combined = "combined.png"
process = [ basedir + "imagemagicks.sh" ,png0,png1 ]
now = time.strftime("%c")

mentions = api.mentions_timeline(count=5)

if not os.path.isfile(basedir + "mentions.txt"): # create the mentios.txt file if it doesnt exist  
        makethelog = open(basedir + "mentions.txt","w")
        makethelog.write('MENTIONS_LOG\n') # write a header and close file
        makethelog.close()
mentionlog = open(basedir + "mentions.txt","a+")
mentionmap = mmap.mmap(mentionlog.fileno(), 0, access=mmap.ACCESS_READ)

def dotweet():
	try:
		status = api.update_with_media(combined,status=prefix + username + "\n expand image to reveal secret." + emoji_padlock + "\n" + thementions + suffix ,in_reply_to_status_id=mention.id,file=outobj)
	except:
		print now + " unexpected error tweeting. :/"

def dotumblr():
	try:
		tumblrcaption= "expand image to reveal secret." + emoji_padlock + "\n" + "submitted by http://twitter.com/" + username
        	client.create_photo('pngbot', state="published", tags=[me,"png hack","transparency","image bot", "illusion","optical illusion", username], caption=tumblrcaption , data=combined)
        	print now + ' tumblrd photo for ' + username
	except:
        	print now + " tumblr photo post failed for some reason :/ " + username

for mention in mentions:
	mentionid = str(mention.id)
	if mentionmap.find(mentionid) == -1 and mention.user.screen_name !=me: # mention not found in log and not from us
		if 'media' in mention.entities:
        		if 'media' in mention.extended_entities:
        			for idx, media in enumerate(mention.extended_entities['media']):
					if media.get("type",None) == "photo":
						image="png" + str(idx) + ".png"
						print now + " download and save: " + image
						image_url = media['media_url']
        		        		urllib.urlretrieve (image_url, image ) # download each image
						#with Image(filename=image) as img:
        		                        	#img.format = 'png'
        		                        	#img.save(filename=image)
        	       		                 	#print now + (' w: ', img.width)  # TODO: use later if I can ever get wand compositing to work
        	        	                	#print now + (' h: ', img.height)
        	        	text = mention.text
				text = text.strip("\@" + me)
				mentionusers = re.findall( r"@\w+", text )
				username = mention.user.screen_name
				for bot in image_bots_list: # allow ONLY whitelisted image bots to pass mentions through to prevent abuse (props to @ronallo for heads up)
					if username.lower() == bot.screen_name.lower():
						for user in mentionusers:
							thementions = thementions + user + " "
						suffix = " #bot2bot"
				prefix = "@"
               	 		sensitive = mention.possibly_sensitive
                	if sensitive == False: # ok - tweet isnt sensitive
				if not os.path.isfile(png1):
					print now + " only one file, using default.png as first image..."
					copyfile (basedir + png0, basedir + png1)
					copyfile (basedir + default, basedir + png0)
                		p = Popen(process, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                		output = p.stdout.read()
                	        sleep(3)
				print now + " shell script output is: " + output
                	        if os.path.isfile(combined): # ok - file exists
                	        	print now + " file exists - tweet and delete"
                        		outobj=open(combined)
					dotweet()	
					dotumblr()
                        		os.remove(combined)
                        		mentionlog.write(mentionid + " " + username + "\n") # writing mention ID to log
                        	else:
	 				print now + " no " + combined + " file found, writing to mention log!"
                        		mentionlog.write(mentionid + " " + username + " no " + combined + " file found! \n") # writing mention ID, but there was no file
                	else:
                		status = api.update_status(status="@"+ username + " sorry, image is marked sensitive.",in_reply_to_status_id=mention.id)
                		print now + " tweet marked sensitive, replied."
				mentionlog.write(mentionid + " " + username + "\n") # writing mention ID to file since we replied"
	#else:
               	#print "already replied!"
mentionlog.close()                                                                                                              
			
