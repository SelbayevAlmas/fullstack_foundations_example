import http.server  

class webserverHandler(baseHTTPrequestHandler):
	def do_GET(self):
		try:
			if self.path.endwith("/hello"):
				self.send_response(200)
				self.send_header('content-type','text/html')
				self.end_header()

				output=""
				output+="<html><body><h1>Hello!</h1></body></html>"
				
				self.wfile.write(output)
				print(output)
				return

		except IOError:	
			self.send_error(404,"FILE NOT FOUND %s" % self.path)

def main():
	try:
		port = 8080
		server = HTTPserver(('',port),webserverHandler)
		print(("web server running on port %s" % port))
		server.serve_forever()

	except KeyboardInterrupt:
		print("^C entered, stopping web server...")
		server.socket.close()

if __name__=='__main__':
	main()