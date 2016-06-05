# Made by Tim Lupo and Neel Patel-Shah (c) 2016
# AP Computer Science Final Project
# Warning: prototype and not perfect verification techniques - not production ready
# Don't steal our credentials we have like 3 followers and its for a school project
# I don't have money for private repos, especially not for this

import twitter
from six.moves import urllib
from bs4 import BeautifulSoup
from twitter import *

# Twitter verification
t = Twitter(
    auth=OAuth(
        consumer_key='rxk2uZazCTE9nC0JVXoqs5aqM',
        consumer_secret='wIj6KffXIGncGIQs0rayZodb4RFBTW8U2RRXghRlC1ZV7bd4Zq',
        token='730015918831632385-YynAbmdnGdpdGh20XQJYdIk9yfkSb49',
        token_secret='w9mUfVxCIFlu0J0FX7P08ORvhRWDbeM1v3IrWQcPDSxwJ'
    )
)
auth = twitter.OAuth(
    consumer_key='rxk2uZazCTE9nC0JVXoqs5aqM',
    consumer_secret='wIj6KffXIGncGIQs0rayZodb4RFBTW8U2RRXghRlC1ZV7bd4Zq',
    token='730015918831632385-YynAbmdnGdpdGh20XQJYdIk9yfkSb49',
    token_secret='w9mUfVxCIFlu0J0FX7P08ORvhRWDbeM1v3IrWQcPDSxwJ'
)

# Verify submission is a valid SoundCloud link
def verifySubmission(text):
	try: # Verifies link is valid
		page = urllib.request.urlopen(text)
		html = BeautifulSoup(page.read(), "html.parser")
		links = html.find_all('meta')
		ID = links[7].get('content')
		if (ID == 'SoundCloud'): # Verifies link is from SoundCloud
			return True;
		else:
			return False;
	except:
		print("Could not connect to link, likely not valid")

def formatTweet(text):
	page = urllib.request.urlopen(text)
	html = BeautifulSoup(page.read(), "html.parser")
	links = html.find_all('meta')
	track = links[22].get('content') #get track title
	artist = links[62].get('content') #get artist title
	tweet = "Listen to '" + track + "' by " + artist + " - " + text + " #carjams"
	return tweet

# Search DMs
stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')
for msg in stream.user():
    if 'direct_message' in msg:
    	text = msg['direct_message']['text']
    	if verifySubmission(text):
    		try:
    			t.statuses.update(status=formatTweet(text))
    			print("Tweeted: %s" % formatTweet(text))
    		except:
    			print("Error tweeting: %s" % text)
    	else:
    		print("Not a valid SoundCloud link")