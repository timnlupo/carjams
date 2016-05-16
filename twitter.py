import twitter
from twitter import *

t = Twitter(
    auth=OAuth(
        consumer_key='Hie6B2gTK7DxZ7NkV4GZPsWMd',
        consumer_secret='gdvQgSMH7weKm7mtWLTOggVMn3wFe5WaMgbRFAQFmIN3sJ5s2V',
        token='4049670291-kEklQ68NeyfjV6TLEeKl0HgO0FcGMBKUVUdrDyF',
        token_secret='AH2T7EhChEU8gp6EP4gYZVbVATYyi3IwZs7bkUyofPp7X'
    )
)

auth = twitter.OAuth(
    consumer_key='Hie6B2gTK7DxZ7NkV4GZPsWMd',
    consumer_secret='gdvQgSMH7weKm7mtWLTOggVMn3wFe5WaMgbRFAQFmIN3sJ5s2V',
    token='4049670291-kEklQ68NeyfjV6TLEeKl0HgO0FcGMBKUVUdrDyF',
    token_secret='AH2T7EhChEU8gp6EP4gYZVbVATYyi3IwZs7bkUyofPp7X'
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