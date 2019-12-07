#!C:\Program Files (x86)\Python37-32\python.exe
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os,sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import requests
import bs4
from bs4 import BeautifulSoup
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

print('''<!doctype html>
<html>
<head>
  <title>게시판</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="food.css">
  <link rel="stylesheet" type="text/css" href="semantic/semantic.css">
  <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
  <script src="semantic/semantic.js"></script>
  <link href="https://fonts.googleapis.com/css?family=Chilanka&display=swap" rel="stylesheet">
  <script type="text/javascript" src="script2.js"></script>
  <link rel="stylesheet" href="게시판.css">
</head>
<body>
    <div class="nav">
       <div class="ui sidebar inverted vertical menu">
         <a class="item">
           1
         </a>
         <a class="item">
           2
         </a>
         <a class="item">
           3
         </a>
       </div>
       <div class="pusher">
       <!-- Site content !-->
       </div>
       <div class="pusher">
          <button id="menu" class="ui inverted primary button">Menu</button>
       </div>
       <div class="nav-right">
         <a href="LOGIN.html" class="nav_item">로그인</a>
         <a href="join.html" class="nav_item">회원가입</a>
         <div class="nav_item">검색</div>
       </div>
     </div>
    <div class="ui red five item inverted menu">
       <a href="index.py" class="item">게시판</a>
          <div class="ui pointing dropdown link item">
             <span class="text">이벤트</span>
             <i class="dropdown icon"></i>
             <div class="menu">
                <a class="item">진행중인 이벤트</a>
                <a href="join.html" class="item">종료된 이벤트</a>
             </div>
          </div>
          <div class="ui pointing dropdown link item">
             <span class="text">여행주간 프로그램</span>
             <i class="dropdown icon"></i>
             <div class="menu">
                <a class="item">테마여행</a>
                <a class="item">지역여행</a>
             </div>
          </div>
          <div class="ui pointing dropdown link item">
              <span class="text">맛집</span>
              <i class="dropdown icon"></i>
              <div class="menu">
                 <a href="백반맛집1.py" class="item">백반</a>
                 <a href="전주비빔밥맛집1.py" class="item">전주비빔밥</a>
                 <a href="콩나물국밥맛집1.py" class="item">콩나물국밥</a>
                 <a href="막걸리맛집1.py" class="item">막걸리</a>
              </div>
           </div>
           <div class="ui pointing dropdown link item">
              <span class="text">체험활동</span>
              <i class="dropdown icon"></i>
              <div class="menu">
                 <a href="문화체험.py" class="item">문화체험</a>
                 <a class="item">향토문유산</a>
                 <a class="item">지정문화재</a>
              </div>
            </div>
    </div>
  <div class="title_not">
     <a href="main.html" class="title_not">TRVEL IN JEONJU</a>
  </div>

  <div class="side">
      <h1><a href="index.py">글쓰기</a></h1>
      <form action="process_create.py" method="post">
          <p><input type="text" name="title" placeholder="title" style="width:1000px;"></p>
          <p><textarea rows="18" name="description" placeholder="description" style="width:1000px;"></textarea></p>
          <div class="create_button"><p><button type="submit" class="btn btn-primary">글쓰기</button></p></div>
      </form>
  </div>
</body>
</html>
'''.format(title=pageId, desc=description))
