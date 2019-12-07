#!C:\Program Files (x86)\Python37-32\python.exe

import cgi, os, view,sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#Redirection
print("Location: 게시판내용.py?id="+title)
print()
