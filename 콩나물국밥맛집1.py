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

url = 'http://openapi.jeonju.go.kr/rest/jeonjufood/getGongBapList'
queryParams = '?'+'&startPage='+'1' +'&serviceKey=' + 'oQ6t%2FFFMlyvY4TJNfkC36yv2zMwEMFIqNc8324oyaZZ1mg5LhqJBswxl6GfcSzHVPgM30GGbtzNf4HiKpVobsA%3D%3D'
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
parkingdetail=bs_obj.find_all("parkingdetail")
tablecnt=bs_obj.find_all("tablecnt")

img0=mainimgurl[0].text
img1=mainimgurl[1].text
img2=mainimgurl[2].text
img3=mainimgurl[3].text
img4=mainimgurl[4].text
img5=mainimgurl[5].text
img6=mainimgurl[6].text
img7=mainimgurl[7].text
img8=mainimgurl[8].text
img9=mainimgurl[9].text

print('''<!doctype html>
<html>
<head>
  <title>콩나물국밥</title>
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

        <div class="list">
            <div class="list_title">
                ■ 콩나물국밥 맛집 LIST
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl0} width= "200px">
                <div class="info">
                    <div class="storenm">{storenm0}</div>
                    <div class="mainmenu">{mainmenu0}</div>
                    <div class="tel0">전북 전주시 완산구 온고을로 30-30</div>
                    <div class="open_close_time">운영시간 | {opentime0} ~ {closetime0}</div>
                    <div class="holiday">휴무일 | {holiday0}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl1} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm1}</div>
                    <div class="mainmenu">{mainmenu1}</div>
                    <div class="parkingdetail1">주차 가능 대수 | {parkingdetail1}</div>
                    <div class="open_close_time">운영시간 | {opentime1} ~ {closetime1}</div>
                    <div class="holiday">휴무일 | {holiday1}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl2} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm2}</div>
                    <div class="mainmenu">{mainmenu2}</div>
                    <div class="parkingdetail2">주차 가능 대수 | {parkingdetail2}</div>
                    <div class="open_close_time">운영시간 | {opentime2} ~ {closetime2}</div>
                    <div id="holiday">휴무일 | 매주 일요일, 마지막주는 월요일</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl3} height="130px" >
                <div class="info">
                    <div class="storenm">{storenm3}</div>
                    <div class="mainmenu">{mainmenu3}</div>
                    <div class="parkingdetail3">주차 가능 대수 | {parkingdetail3}</div>
                    <div class="open_close_time">운영시간 | {opentime3} ~ {closetime3}</div>
                    <div class="holiday">휴무일 | {holiday3}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl4} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm4}</div>
                    <div class="tablecnt4">테이블좌적수 | {tablecnt4}</div>
                    <div class="newaddr4">{newaddr4}</div>
                    <div class="open_close_time">운영시간 | {opentime4} ~ {closetime4}</div>
                    <div class="holiday">휴무일 | {holiday4}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl5} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm5}</div>
                    <div class="mainmenu">{mainmenu5}</div>
                    <div class="newaddr">{newaddr5}</div>
                    <div class="open_close_time">운영시간 | {opentime5} ~ {closetime5}</div>
                    <div class="holiday">휴무일 | {holiday5}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl6} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm6}</div>
                    <div class="mainmenu">콩나물국밥, 굴매생이해장국, 떡국</div>
                    <div class="newaddr">{newaddr6}</div>
                    <div class="open_close_time">운영시간 | {opentime6} ~ {closetime6}</div>
                    <div class="holiday">휴무일 | {holiday6}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl7} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm7}</div>
                    <div class="mainmenu">전주콩나물국밥, 얼큰돼지국밥, 전주비빔밥</div>
                    <div class="newaddr">{newaddr7}</div>
                    <div class="open_close_time">운영시간 | {opentime7} ~ {closetime7}</div>
                    <div class="holiday">휴무일 : {holiday7}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl8} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm8}</div>
                    <div class="mainmenu">순대국밥, 콩나물국밥, 순두부찌개</div>
                    <div class="newaddr">{newaddr8}</div>
                    <div class="open_close_time">운영시간 | {opentime8} ~ {closetime8}</div>
                    <div class="holiday">휴무일 | {holiday8}</div>
                </div>
            </div>
            <div class="foodlist">
                <img class="foodimg" src={mainimgurl9} width= "210px">
                <div class="info">
                    <div class="storenm">{storenm9}</div>
                    <div class="mainmenu">콩오름 콩나물국밥, 묵은지 갈비전골</div>
                    <div class="newaddr">{newaddr9}</div>
                    <div class="open_close_time">운영시간 | {opentime9} ~ {closetime9}</div>
                    <div class="holiday">휴무일 | {holiday9}</div>
                </div>
            </div>
        </div>
        <div class="page_button">
            <a href="콩나물국밥맛집1.py"><button class="ui brown button">1</button></a>
            <a href="콩나물국밥맛집2.py"><button  class="ui brown  basic button">2</button></a>
            <a href="콩나물국밥맛집3.py"><button class="ui brown  basic button">3</button></a>
        </div>
    </body>
    </html>
'''.format(mainimgurl0=img0,mainmenu0=mainmenu[0],newaddr0=newaddr[0],storenm0=storenm[0],holiday0=holiday[0],opentime0=opentime[0],closetime0=closetime[0],tel0=tel[0],parkingdetail1=parkingdetail[1],mainimgurl1=img1,mainmenu1=mainmenu[1],newaddr1=newaddr[1],storenm1=storenm[1],holiday1=holiday[1],opentime1=opentime[1],closetime1=closetime[1],tel1=tel[1],parkingdetail2=parkingdetail[2],mainimgurl2=img2,mainmenu2=mainmenu[2],newaddr2=newaddr[2],storenm2=storenm[2],holiday2=holiday[2],opentime2=opentime[2],closetime2=closetime[2],tel2=tel[2],parkingdetail3=parkingdetail[3],mainimgurl3=img3,mainmenu3=mainmenu[3],newaddr3=newaddr[3],storenm3=storenm[3],holiday3=holiday[3],opentime3=opentime[3],closetime3=closetime[3],tel3=tel[3],tablecnt4=tablecnt[4],mainimgurl4=img4,mainmenu4=mainmenu[4],newaddr4=newaddr[4],storenm4=storenm[4],holiday4=holiday[4],opentime4=opentime[4],closetime4=closetime[4],tel4=tel[4],mainimgurl5=img5,mainmenu5=mainmenu[5],newaddr5=newaddr[5],storenm5=storenm[5],holiday5=holiday[5],opentime5=opentime[5],closetime5=closetime[5],tel5=tel[5],mainimgurl6=img6,mainmenu6=mainmenu[6],newaddr6=newaddr[6],storenm6=storenm[6],holiday6=holiday[6],opentime6=opentime[6],closetime6=closetime[6],tel6=tel[6],mainimgurl7=img7,mainmenu7=mainmenu[7],newaddr7=newaddr[7],storenm7=storenm[7],holiday7=holiday[7],opentime7=opentime[7],closetime7=closetime[7],tel7=tel[7],mainimgurl8=img8,mainmenu8=mainmenu[8],newaddr8=newaddr[8],storenm8=storenm[8],holiday8=holiday[8],opentime8=opentime[8],closetime8=closetime[8],tel8=tel[8],mainimgurl9=img9,mainmenu9=mainmenu[9],newaddr9=newaddr[9],storenm9=storenm[9],holiday9=holiday[9],opentime9=opentime[9],closetime9=closetime[9],tel9=tel[9]))
