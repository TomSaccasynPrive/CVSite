"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from CVSite2 import app
from flask_restful import Resource, Api
api = Api(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='This is the contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='This is the about page.'
    )
@app.route('/curriculumvitae')
def curriculumVitae():
    """Renders the about page."""
    return render_template(
        'CurriculumVitae.html',
        title='Curriculum Vitae',
        year=datetime.now().year,
        message='This is the curriculum vitae page.'
    )
@app.route('/schoolprojecten')
def schoolProjecten():
    """Renders the about page."""
    return render_template(
        'schoolprojecten.html',
        title='School Projecten',
        year=datetime.now().year,
        message='This is the school projects page.'
    )


class CVApiOverMij(Resource):
    def get(self):
        return{
            'Over mij': {
                'naam': 'Tom Saccasyn',
                'geboorteplaats': 'Jette',
                'woonplaats': 'Eizeringen(Sint-Kwintens-Lennik)',
                'provincie': 'Vlaams-Brabant',
                'geboortedatum': '07-10-1997',
                'School': 'Erasmushogeschool Brussel',
                'jaar in school': 'laatstejaarsstudent',
                'stage': 'SpotIt',
                'stageplaats': 'Merelbeke',
                'geslacht': 'man',
                'nationaliteit': 'Belg'
    }
  }
class CVApiHistoriekScholen(Resource):
        def get(self):
            return{
                'HistoriekScholen': {
                      'SchoolJaar 1': '2008-2010',
                      'School 1': '1 ste graad Moderne (Middenschool Sint-Angela)',
                      'SchoolJaar 2': '2011-2013',
                      'School 2': '2 de graad Handel (Don Bosco Instituut Groot-Bijgaarden)',
                      'SchoolJaar 3': '2013-2015',
                      'School 3': '3 de graad Informaticabeheer (Don Bosco Instituut Groot-Bijgaarden)',
                      'SchoolJaar 4': '2015-heden',
                      'School 4': 'Bachelor Toegepaste Informatica : Networks & Security Dig-X (Erasmus Hogeschool Brussel)'
      
    }
  }
class CVApiTalenkennis(Resource):
        def get(self):
            return{
                'Talenkennis': {
                      'Talen': {
                          'Nederlands':'moedertaal',
                          'Frans':'vloeiend begrijpen, schrijven en spreken',
                          'Engels':'vloeiend begrijpen, schrijven en spreken' }
                      
      
    }
  }
class CVApiComputerVaardigheden(Resource):
        def get(self):
            return{
                'Computervaardigheden': {
                      'Tools en Applicaties': 'HTML, Javascript, PHP,, CSS, Ajax , Adobe, Dreamweaver , Adobe Flash, MS-Office, MS-office professional, Windows 7, WordPress, Drupal, ASP.NET, Cisco apparatuur, Java, C#.NET, XML, C++',
                      'Besturingssystemen':'MS-DOS, Windows, Apple, Centos, Android, Linux',
                      'Databases':'SQL meerbepaald MySql' } 
  }

class CVApiHobbies(Resource):
        def get(self):
            return{
                'Hobbies': 'webmaster VJF (Vlaamse Judo Federatie),judo',
                'info hobby':'blauwe gordel in judo, meer informatie over de vjf zie www.vjf.be' 
  }
class CVApiAll(Resource):
        def get(self):
            return{'Over mij': {
                'naam': 'Tom Saccasyn',
                'geboorteplaats': 'Jette',
                'woonplaats': 'Eizeringen(Sint-Kwintens-Lennik)',
                'provincie': 'Vlaams-Brabant',
                'geboortedatum': '07-10-1997',
                'School': 'Erasmushogeschool Brussel',
                'jaar in school': 'laatstejaarsstudent',
                'stage': 'SpotIt',
                'stageplaats': 'Merelbeke',
                'geslacht': 'man',
                'nationaliteit': 'Belg'
    },
                   'HistoriekScholen': {
                      'SchoolJaar 1': '2008-2010',
                      'School 1': '1 ste graad Moderne (Middenschool Sint-Angela)',
                      'SchoolJaar 2': '2011-2013',
                      'School 2': '2 de graad Handel (Don Bosco Instituut Groot-Bijgaarden)',
                      'SchoolJaar 3': '2013-2015',
                      'School 3': '3 de graad Informaticabeheer (Don Bosco Instituut Groot-Bijgaarden)',
                      'SchoolJaar 4': '2015-heden',
                      'School 4': 'Bachelor Toegepaste Informatica : Networks & Security Dig-X (Erasmus Hogeschool Brussel)'
      
    },
                   'Talenkennis': {
                      'Talen': {
                          'Nederlands':'moedertaal',
                          'Frans':'vloeiend begrijpen, schrijven en spreken',
                          'Engels':'vloeiend begrijpen, schrijven en spreken' 
   },
                      'Computervaardigheden': {
                      'Tools en Applicaties': 'HTML, Javascript, PHP,, CSS, Ajax , Adobe, Dreamweaver , Adobe Flash, MS-Office, MS-office professional, Windows 7, WordPress, Drupal, ASP.NET, Cisco apparatuur, Java, C#.NET, XML, C++',
                      'Besturingssystemen':'MS-DOS, Windows, Apple, Centos, Android, Linux',
                      'Databases':'SQL meerbepaald MySql' 
   }, 
                'Hobbies': 'webmaster VJF (Vlaamse Judo Federatie),judo',
                'info hobby':'blauwe gordel in judo, meer informatie over de vjf zie www.vjf.be' 
   }
}
api.add_resource(CVApiAll,'/api/all')
api.add_resource(CVApiOverMij,'/api/overmij')
api.add_resource(CVApiHistoriekScholen,'/api/historiekscholen')
api.add_resource(CVApiTalenkennis,'/api/talenkennis')
api.add_resource(CVApiComputerVaardigheden,'/api/computervaardigheden')
api.add_resource(CVApiHobbies,'/api/hobbies')
