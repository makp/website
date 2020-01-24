import os
import datetime
import time
import webapp2
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'pages/')
jinja_env = jinja2.Environment(autoescape=True,
                               loader=jinja2.FileSystemLoader(template_dir))


date_today = datetime.datetime.now() # .strftime('%Y, %m, %d')
week_today = date_today.isocalendar()[1]
week_first = datetime.date(2019, 8, 26).isocalendar()[1]
week_jump = (week_today - week_first) + 1
# week_jump = 2
id_jump = 'Week' + str(week_jump)



class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        # takes the name of a template file and returns a template object
        template_values = {
            'verb': "blah"
        }
        self.response.write(template.render(template_values))

        # q = self.request.get("q")
        # if q == "1":
        #     self.response.headers['Content-Type'] = 'text/plain'
        #     self.response.out.write(self.request)
        # elif q == "2":
        #     self.redirect("/research")
        
        # def post(self):
        #     r = self.request.get("r")
        #     self.response.out.write(r)

        
class PublicationHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'verb': "blah"
        }
        template = jinja_env.get_template('publications.html')
        self.response.write(template.render(template_values))

class ResearchHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'verb': "blah"
        }
        template = jinja_env.get_template('research.html')
        self.response.write(template.render(template_values))


class TeachingHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'verb': "blah"
        }
        template = jinja_env.get_template('teaching.html')
        self.response.write(template.render(template_values))

class TeachingSched1(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': "Environmental Ethics",
            'number': "PHIL255",
            'semester': "Fall 2019",
            'source': 'includes/schedule_f19_phil255.html',
            'id_jump': id_jump,
            'week_jump': week_jump
        }
        template = jinja_env.get_template('schedule.html')
        self.response.write(template.render(template_values))

class TeachingSched2(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': "What Makes Us Moral",
            'number': "PHIL342",
            'semester': "Fall 2018",
            'source': 'includes/schedule_f18_phil342.html',
            'id_jump': id_jump,
            'week_jump': week_jump
        }
        template = jinja_env.get_template('schedule.html')
        self.response.write(template.render(template_values))

class TeachingSched3(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': "Sex, Death, & Outlaws",
            'number': "PHIL212",
            'semester': "Spring 2020",
            'source': 'includes/schedule_s20_phil212.html',
            'id_jump': id_jump,
            'week_jump': week_jump
        }
        template = jinja_env.get_template('schedule.html')
        self.response.write(template.render(template_values))

class TeachingSched4(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': "The Evolution of Complexity",
            'number': "PHIL460",
            'semester': "Spring 2019",
            'source': 'includes/schedule_s19_phil460.html',
            'id_jump': id_jump,
            'week_jump': week_jump
        }
        template = jinja_env.get_template('schedule.html')
        self.response.write(template.render(template_values))

class TeachingSched5(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': "Environmental Ethics",
            'number': "PHIL255",
            'semester': "Spring 2020",
            'source': 'includes/schedule_s20_phil255.html',
            'id_jump': id_jump,
            'week_jump': week_jump
        }
        template = jinja_env.get_template('schedule.html')
        self.response.write(template.render(template_values))

# URL mapping section
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/pubs', PublicationHandler),
    ('/research', ResearchHandler),
    ('/teaching', TeachingHandler),
    ('/schedule1', TeachingSched1),
    ('/schedule2', TeachingSched2),
    ('/schedule3', TeachingSched3),
    ('/schedule4', TeachingSched4),
    ('/schedule5', TeachingSched5),
], debug=True)
