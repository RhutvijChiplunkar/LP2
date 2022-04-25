import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        a = 1 
        for i in range(5):
            self.response.write(str(5)+" x " + str(a) + " = " + str(int(a)*5) + "<br>")
            a+=1 

app = webapp2.WSGIApplication([('/', MainPage),],debug=True)