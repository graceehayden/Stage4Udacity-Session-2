import os
import jinja2
import webapp2
import cgi

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, content, **kw):         #Now don't have to write self.response.out.write every time
		self.response.write(content)
    
	def render_str(self, template, **kw):
		t = jinja_env.get_template(template)
		return t.render(kw)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		name = 'Stage 1'
		lessons = [
					['Lesson 1 Important Concepts',[
						['HTML', 'HTML is the text we read online, known as hypertext markup language.'],
						['Tags and Elements', 'Tags are used to distinguish elements, or parts contained within the tags. The em tag, for instance, places emphasis on text by italicizing it. The p tag I used separates the text within it into paragraphs.'],
						['Why Computers Are Stupid', 'Computers need to be told what to do very literally. They will misread all unedited typos and ruin code.'],
						['Inline and Block Elements', 'Block elements put themselves in blocks and inlines do not. Block elements are good for styling and inline elements are not.']
					]
				],
					['Lesson 2: Creating a Structured Document with HTML',[
						['Developer Tools','Everything designed on a website is in blocks. Within the blocks are trees of elements that may be designed separately based on their tags. CSS is commonly used for that design.'],
						['HTML is Structured Like a Family Tree','HTML elements are tiered within one another, which allows for visual ease in styling. Each new element within another is indented and the indentations get deeper the more elements that get nested within others.'],
						['Text Editors','HTML is written with text editors, which are like word processors for code. Some automatically close tags and autoindent.']
					]
				],
					['Lesson 3: Adding Style to HTML Using CSS',[
						['Avoiding Repetition','If programmers repeat the same code over and over in different places, any future changes will be harder to make, as they will have to go back and find each place it was used.'],
						['CSS','CSS, or cascading style sheets, is styling done in a separate document that is linked to on the index page. It allows for non-redundancies by the assignment of classes, etcetera.']
					]
				]	
			]	
		stage = [name, lessons]		
		self.render("index.html", name=name, lessons=lessons)
		
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
