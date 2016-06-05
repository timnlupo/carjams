import fix_path
import webapp2
import tweepy
from tweepy import *

class MainPage(webapp2.RequestHandler):
    def get(self):

		auth = tweepy.OAuthHandler('rxk2uZazCTE9nC0JVXoqs5aqM', 'wIj6KffXIGncGIQs0rayZodb4RFBTW8U2RRXghRlC1ZV7bd4Zq')
		auth.set_access_token('730015918831632385-YynAbmdnGdpdGh20XQJYdIk9yfkSb49', 'w9mUfVxCIFlu0J0FX7P08ORvhRWDbeM1v3IrWQcPDSxwJ')
		api = tweepy.API(auth)
		print(api.me().name)
		stream = Stream(auth, StdOutListener())
		stream.userstream()
		time.sleep(600)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)



class StdOutListener( StreamListener ):

	def __init__( self ):
		self.tweetCount = 0

	def on_connect( self ):
		print("Connection established!!")

	def on_disconnect( self, notice ):
		print("Connection lost!! : ", notice)

	def on_data( self, status ):
		print("Entered on_data()")
		print("DATA: ", status)
		return True

	def on_data( self, status ):
		print("Entered on_direct_message()")
		try:
			print("DATA: ", status)
			return True
		except BaseException as e:
			print("Failed on_direct_message()", str(e))

	def on_error( self, status ):
		print("StdOutListener Error: ", status)


