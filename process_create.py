#!C:\Program Files (x86)\Python37-32\python.exe

import cgi, os, view,sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
