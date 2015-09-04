import os
import jinja2
import webapp2
import cgi


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):         #Now don't have to write self.response.out.write every time
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
		  concept = self.request.get('concept','description')
		  lesson = self.request.get('lesson')
		  stage = self.request.get('stage')
		  template_values = self.request.get_all('concept', 'lesson', 'stage')
      self.write.template.render(template_values)
      self.render("index.html", concept=concept, lesson=lesson, stage=stage, template_values=template_values)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
