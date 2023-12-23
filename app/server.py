import cherrypy
import os

from main import app

if __name__ == '__main__':

	# Mount the application
	cherrypy.tree.graft(app, "/")

	# Unsubscribe the default server
	cherrypy.server.unsubscribe()

	# Instantiate a new server object
	server = cherrypy._cpserver.Server()

	# Configure the server object
	server.socket_host = "0.0.0.0"
	server.socket_port = int(os.getenv("FLASKPORT", 5000))
	server.thread_pool = 30

	# SSL Support
	# server.ssl_module            = 'builtin'
	# server.ssl_certificate       = '../ssl/certificate.crt'
	# server.ssl_private_key       = '../ssl/privatekey.key'
	# server.ssl_certificate_chain = '../ssl/certificate_chain.pem'

	# "Cannot use tools without cherrypy Application"

	# cherrypy.tools.staticdir.dir = f"{os.getcwd()}/static"
	# cherrypy.tools.staticdir.on = True
	# cherrypy.config.update({"tools.staticdir.on": True})

	# # cherrypy.tree.mount(None, "/", config=cfg)

	# Subscribe this server
	server.subscribe()

	print(f"Starting cherrypy...")

	cherrypy.engine.start()
	cherrypy.engine.block()