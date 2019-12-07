#!C:\Program Files (x86)\Python37-32\python.exe
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os, sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    update_link = '<a href="update.py?id={}"><button type="submit" class="btn btn-primary">수정하기</button></a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <button type="submit" class="btn btn-primary">삭제하기</button>
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
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
        <h1><a href="index.py">WEB</a></h1>
        <div class="create_button">
            <a href="index.py"><button type="submit" class="btn btn-primary">목록</button></a>
        </div>
        <div class="본문">
            <h2 class="제목">{title}</h2>
            <p class="내용">{desc}</p>
        </div>
        <div class="create_button">
            <p>{update_link}</p>
            <p>{delete_action}</p>
        </div>
    </div>
</body>
</html>
'''.format(title=pageId, desc=description, update_link=update_link, delete_action=delete_action))
