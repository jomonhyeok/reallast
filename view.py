import cgi, os, view,sys

def getlist():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr +'''<div class="게시판리스트"><table class="table">
           <tbody><td><a href="게시판내용.py?id={name}">{name}</a></td></tbody></table></div>'''.format(name=item)
    return listStr
