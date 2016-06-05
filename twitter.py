import twitter
from twitter import *

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