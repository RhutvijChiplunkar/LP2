import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
	     self.response.write("Bindi")

app = webapp2.WSGIApplication([('/',MainPage),
			       ],
                               debug=True)