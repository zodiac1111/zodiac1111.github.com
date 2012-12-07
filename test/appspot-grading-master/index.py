import cgi
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from lispy import lis, bf
from python_grading.python import python

from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))


class lispy(webapp.RequestHandler):

    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/lispy" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="submit"></div>
              </form>
            </body>
          </html>""")
          
    def post(self):
        self.response.out.write('<html><body>Output:<pre>')
        content = self.request.get('content')
        out = str(lis.eval(lis.parse(content)))
        
        self.response.out.write(cgi.escape('> ' + str(content)) + '\n')
        self.response.out.write(cgi.escape(out))
        self.response.out.write('</pre></body></html>')
        
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/lispy', lispy),
                                      ('/python(.*)', python)],
                                      debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
