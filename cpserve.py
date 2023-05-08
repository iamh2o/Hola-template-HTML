import cherrypy

class Website:
    @cherrypy.expose
    def index(self):
        return open('index.html')

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8081})
    cherrypy.quickstart(Website(), '/', {'/': {'tools.staticdir.on': True, 'tools.staticdir.dir': '/home/centos/projects/daylily-web-mobile/'}})
