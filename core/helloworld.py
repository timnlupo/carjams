import webapp2
from tweepy import *

class MainPage(webapp2.RequestHandler):
    def get(self):
		auth = tweepy.OAuthHandler('Hie6B2gTK7DxZ7NkV4GZPsWMd', 'gdvQgSMH7weKm7mtWLTOggVMn3wFe5WaMgbRFAQFmIN3sJ5s2V')
		auth.set_access_token('4049670291-kEklQ68NeyfjV6TLEeKl0HgO0FcGMBKUVUdrDyF', 'AH2T7EhChEU8gp6EP4gYZVbVATYyi3IwZs7bkUyofPp7X')

		api = tweepy.API(auth)

		public_tweets = api.home_timeline()
		for tweet in public_tweets:
		    print tweet.text

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
