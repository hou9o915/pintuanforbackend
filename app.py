#!/usr/bin/env python
#-*-coding:UTF-8-*-
from controller import app
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000,debug=True,reloader=True)
else:
	#os.chdir(os.path.dirname(__file__))
	application = app