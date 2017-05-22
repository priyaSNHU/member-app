import webapp2
import logging

from authentication import *
from add import GuildMember

class RemoveApp(webapp2.RequestHandler):
  def post(self):
    logging.info(self.request)

    if Authentication.CanUserSeeData(self.request) is False:
      self.response.status_int = 403
      return

    if GuildMember.remove(self.request.body) is True:
      self.response.write("Removed")
    else:
      # TODO: Return some better message.
      self.response.write("Error removing")

app = webapp2.WSGIApplication([
  ('/remove', RemoveApp),
], debug=True)
