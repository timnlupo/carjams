import twitter
from twitter import *

t = Twitter(
	auth=OAuth(
	    consumer_key='',
        consumer_secret='',
        token='',
        token_secret=''
	)
)

auth = twitter.OAuth(
    consumer_key='',
    consumer_secret='',
    token='',
    token_secret=''
)

stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in stream.user():
    if 'direct_message' in msg:
    	text = msg['direct_message']['text']
    	print "Message received..."
    	try:
    		t.statuses.update(status=text)
        	print "Tweeted: %s" % text
        except:
        	print "Error tweeting: %s" % text