#!C:\Program Files (x86)\Python37-32\python.exe

import cgi, os, view,sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()
