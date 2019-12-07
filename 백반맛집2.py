#!C:\Program Files (x86)\Python37-32\python.exe
print("content-type: text/html; charset=utf-8\n")
print()
import cgi,os, sys
import codecs
import requests
import bs4
from bs4 import BeautifulSoup
import io
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())#한글출력

url = 'http://openapi.jeonju.go.kr/rest/jeonjufood/getWhiteRiceList'
queryParams = '?'+'&startPage='+'2' +'&serviceKey=' + 'oQ6t%2FFFMlyvY4TJNfkC36yv2zMwEMFIqNc8324oyaZZ1mg5LhqJBswxl6GfcSzHVPgM30GGbtzNf4HiKpVobsA%3D%3D'
url=url+queryParams
result =requests.get(url)
bs_obj=BeautifulSoup(result.content,"html.parser")

mainmenu=bs_obj.find_all("mainmenu")
newaddr=bs_obj.find_all("newaddr")
opentime=bs_obj.find_all("opentime")
closetime=bs_obj.find_all("closetime")
holiday=bs_obj.find_all("holiday")
storenm=bs_obj.find_all("storenm")
tel=bs_obj.find_all("tel")
mainimgurl=bs_obj.find_all("mainimgurl")

img0=mainimgurl[0].text
img1=mainimgurl[1].text
img2=mainimgurl[2].text

print('''<!doctype html>
<html>
<head>
  <title>백반</title>
  <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="semantic/semantic.css">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
    <script src="semantic/semantic.js"></script>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="food.css">
    <link href="https://fonts.googleapis.com/css?family=Chilanka&display=swap" rel="stylesheet">
    <script type="text/javascript" src="script2.js"></script>
</head>
<body>
  <div class="backgroud">
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
           <span class="text">여행 정보</span>
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

        <div class="list">
            <div class="list_title">
                ■ 백반 맛집 LIST
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl0} width= "200px">
                <div class="info">
                    <div class="storenm">{storenm0}</div>
                    <div class="mainmenu">{mainmenu0}</div>
                    <div class="newaddr">{newaddr0}</div>
                    <div class="open_close_time">운영시간 | {opentime0} ~ {closetime0}</div>
                    <div class="holiday">휴무일 | {holiday0}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl1} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm1}</div>
                    <div class="mainmenu">{mainmenu1}</div>
                    <div class="newaddr">{newaddr1}</div>
                    <div class="open_close_time">운영시간 | {opentime1} ~ {closetime1}</div>
                    <div class="holiday">휴무일 | {holiday1}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl2} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm2}</div>
                    <div class="mainmenu">{mainmenu2}</div>
                    <div class="newaddr">{newaddr2}</div>
                    <div class="open_close_time">운영시간 | {opentime2} ~ {closetime2}</div>
                    <div class="holiday">휴무일 | {holiday2}</div>
                </div>
            </div>
        </div>
        <div class="page_button">
            <a href="백반맛집1.py"><button class="ui brown basic button">1</button></a>
            <a href="백반맛집2.py"><button class="ui brown button">2</button></a>
        </div>
    </body>
    </html>
'''.format(mainimgurl0=img0,mainmenu0=mainmenu[0],newaddr0=newaddr[0],storenm0=storenm[0],holiday0=holiday[0],opentime0=opentime[0],closetime0=closetime[0],tel0=tel[0],mainimgurl1=img1,mainmenu1=mainmenu[1],newaddr1=newaddr[1],storenm1=storenm[1],holiday1=holiday[1],opentime1=opentime[1],closetime1=closetime[1],tel1=tel[1],mainimgurl2=img2,mainmenu2=mainmenu[2],newaddr2=newaddr[2],storenm2=storenm[2],holiday2=holiday[2],opentime2=opentime[2],closetime2=closetime[2],tel2=tel[2]))
