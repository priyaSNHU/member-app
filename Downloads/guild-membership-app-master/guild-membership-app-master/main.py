import logging
import webapp2

from authentication import *

class MainPage(webapp2.RequestHandler):
    def get(self):
      # We don't authenticate the user here.
      # The endpoints responsible for querying
      # the database are responsible for this.
      # This allows the UI to handle the
      # authentication flow more seamlessly.
      template = open('index.html').read()
      self.response.write(template)

class Authenticate(webapp2.RequestHandler):
  def get(self):
      self.response.write(open('authentication.html').read())
    
class GoogleLogin(webapp2.RequestHandler):
  def get(self):
    # This page has login: required, which forces to
    # authenticate using the user API.
    # TODO: We are missing the original page URL here
    # and always redirect to the homepage. Propagate
    # this information here if it makes sense.
    self.redirect('/')

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/authenticate', Authenticate),
  ('/glogin', GoogleLogin),
], debug=True)
