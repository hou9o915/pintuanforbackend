#!/usr/bin/env python
#-*-coding:UTF-8-*-
from controller import app

app.run(host='0.0.0.0', port=8080,debug=True,reloader=True)