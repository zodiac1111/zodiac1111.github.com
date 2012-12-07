import cgi
import os
from django.utils import simplejson

from google.appengine.api import users
from google.appengine.ext import webapp
from python_problems import get_problems_in_pset

from google.appengine.ext.webapp import template

form = """
              <form action="/python/%s/%s" method="post">
                <div><textarea name="exec" rows="10" cols="60">%s</textarea></div>
                <div><input type="submit" value="submit"></div>
              </form>
"""

class python(webapp.RequestHandler):


    def show_home(self):
        from python_problems import pset_list
        
        template_values = {
            'pset_list': pset_list
        }
        
        path = os.path.join(os.path.dirname(__file__), 'python.html')
        self.response.out.write(template.render(path, template_values))

    def show_pset(self, pset_name):
        
        template_values = {
            'pset_name':pset_name,
            'problems':get_problems_in_pset(pset_name)
        }

        path = os.path.join(os.path.dirname(__file__), 'pset.html')
        self.response.out.write(template.render(path, template_values))

    def get(self, problem_id):
        
        if problem_id == '':
            return self.show_home()
        if (problem_id[-1] == '/'):
            return self.redirect('/python' + problem_id[:-1])
                
        parsed_id = problem_id[1:].split('/')

        pset_name = parsed_id[0]
                
        if len(parsed_id) == 1:
            return self.show_pset(pset_name)
        
        problem_id = int(parsed_id[1])
        
        template_values = {
            'intro': get_problems_in_pset(pset_name)[problem_id].intro.replace('\n', '<br>\n'),
            'id': problem_id,
            'pset_name': pset_name,
            'code': get_problems_in_pset(pset_name)[problem_id].init
        }
        path = os.path.join(os.path.dirname(__file__), 'problem.html')
        self.response.out.write(template.render(path, template_values))
          
    def post(self, problem_id):
    
        problem_id = problem_id[1:]
            
        parsed_id = problem_id.split('/')
        
        pset_name = parsed_id[0]
        problem_id = int(parsed_id[1])
        
        passed = True
        
        exec_stmt = self.request.get('exec')
        exec_stmt = exec_stmt.replace('\r\n', '\n')
                
        import sys
        out = sys.stdout

        class WriteLog:
            def __init__(self):
                self.content = ""
            def write(self, string):
                self.content += string

        wo = WriteLog()

        try:
            sys.stdout = wo
            closure = {}
            exec exec_stmt in closure
            get_problems_in_pset(pset_name)[problem_id].test(closure)
        except AssertionError:
            passed = False 
        except:
            passed = "Error"
        finally:
            sys.stdout = out
        
        if wo.content:
            self.response.out.write("<pre style='color:lightblue'>")
            self.response.out.write(wo.content)
            self.response.out.write("</p>")
            
        if passed == "Error":
            self.response.out.write("<pre style='color:red'>error</p>")      
        elif passed:
            self.response.out.write("<pre style='color:lightgreen'>passed</p>")
        else:
            self.response.out.write("<pre style='color:red'>failed</p>")


