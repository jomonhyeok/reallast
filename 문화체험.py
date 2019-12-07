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

url = 'http://openapi.jeonju.go.kr/rest/experience/getExperienceList'
queryParams = '?'+'&startPage='+'1' +'&serviceKey=' + 'oQ6t%2FFFMlyvY4TJNfkC36yv2zMwEMFIqNc8324oyaZZ1mg5LhqJBswxl6GfcSzHVPgM30GGbtzNf4HiKpVobsA%3D%3D'
url=url+queryParams
result =requests.get(url)
bs_obj=BeautifulSoup(result.content,"html.parser")

datatitle=bs_obj.find_all("datatitle")
addr=bs_obj.find_all("addr")
addrdtl=bs_obj.find_all("addrdtl")
img0=bs_obj.find_all("homepage")

homepage0=img0[0].text
homepage1=img0[1].text
homepage2=img0[2].text
homepage3=img0[3].text
homepage4=img0[4].text
homepage5=img0[5].text
homepage6=img0[6].text
homepage7=img0[7].text

print('''<!doctype html>
<html>
<head>
  <title>문화체험</title>
  <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="semantic/semantic.css">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
    <script src="semantic/semantic.js"></script>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="food.css">
    <link rel="stylesheet" href="문화체험.css">
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
            <div class="culturl_title">
                ■ 문화체험 LIST
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle0}</div>
                <div class="addr">{addr0} {addrdtl0}</div>
                <a href="{homepage0}"><div class="homepage">{homepage0}</div></a>
                <div class="content">
                    <div>■ 체험정보</div>
                    <div class="step1">○ 한지뜨기 : 모든연령 / 30분 / 500~2,000원</div>
                    <div class="step1">○ 한지공예 : 모든연령 / 60분 / 5,000원 - 연필꽂이, 악세사리함, 휴대폰고리, 칼라믹스악세사리, 아로마테라피함, 명함케이스(10,000원)</div>
                    <div class="step1">○ 한지창의 : 모든연령 / 60분 / 5,000원 - 민화퍼포먼스, 줌치를 이용한 생활소품, 한지를 이용한 만화경 만들기</div>
                    <div class="step1">○ 상시체험 : 어린이,청소년 / 30분 / 2,000원</div>
                    <div class="step1">○ 무료체험 : 한지퍼즐 맞추기, 한지과학탐험, 투호놀이</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle1}</div>
                <div class="addr">{addr1} {addrdtl1}</div>
                <a href="{homepage1}"><div class="homepage">{homepage1}</div></a>
                <div class="content">
                    <div>■ 저희 예다원은 2010년 6월에 전주한옥마을 향교길에 둥지를 틀었습니다.</div>
                    <div class="step1">○ 천연염색체험, 전통 차 체험과 함께 전주한옥마을에서 잊지 못할 추억을 만들어 드립니다.</div>
                    <div class="step1">○ 바쁘고 복잡한 일상을 잠시 내려놓고 저희 예다원에서 친구와 애인 그리고 가족들과 함께 바쁜 일상에서 못다한 이야기들을 나눠보세요.</div>
                    <div>■ 체험정보</div>
                    <div class="step1">1) 소요시간 - 40~60분</div>
                    <div class="step1">2) 인원/비용 - 4인 이상 / 20명 이상 단체 30%할인(사전에 문의해주세요)</div>
                    <div class="step1">3) 기타 - 천연염색 자연에서 채취한 나무껍질·풀·꽃·열매·흙 등의 자연 염료로 옷감에 물을 들이는 체험입니다. 체험 시에는 주로 손수건이나 티셔츠 등을 사용하여 진행합니다.</div>
                    <div class="step2">비용 : 1인당 10,000원, 20인 이상 단체할인(사전문의) - 다례체험 전통 차를 직접 우려내고 대접해 봄으로써 우리 전통예절을 배울 수 있는 체험입니다.</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle2}</div>
                <div class="addr">{addr2} {addrdtl2}</div>
                <a href="{homepage2}"><div class="homepage">{homepage2}</div></a>
                <div class="content">
                    <div>■ 한지로 만나는 놀라운 세상 이지원 </div>
                    <div class="step1">○ 전통한지공예가 김혜미자 선생의 자택이자 작업실인 이지원은 다양한 한지공예를 만날 수 있는 곳으로 거의 모든 가재도구가 한지 작품으로 꾸며져 있으며 한지공예 체험도 가능하다.</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle3}</div>
                <div class="addr">{addr3} {addrdtl3}</div>
                <a href="{homepage3}"><div class="homepage">{homepage3}</div></a>
                <div class="content">
                    <div>■ 체험정보</div>
                    <div class="step1">○ 코일링과 도자기페인팅을 이용한 나만의 생활도자기만들기, 도자기 시계 만들기, 내방문패 만들기</div>
                    <div class="step1">○ 체험문의:홈페이지 참고</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle4}</div>
                <div class="addr">{addr4} {addrdtl4}</div>
                <a href="{homepage4}"><div class="homepage">{homepage4}</div></a>
                <div class="content">
                    <div>■ 체험정보</div>
                    <div>○ 서각, 전통기러기, 문패만들기 등의 체험을 즐기실 수 있습니다.</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle5}</div>
                <div class="addr">{addr5} {addrdtl5}</div>
                <a href="{homepage5}"><div class="homepage">{homepage5}</div></a>
                <div class="content">
                    <div>■ 전주시 제1호 3대 김치 명가의 집 단체체험, 숙박, 전통 음식도 배우는 김명옥 김치 전통요리체험관입니다.</div>
                    <div class="step1">○ 전주음식에 정을 담아 숙박도 하고 외갓집처럼 집 밥 요리 배우서 먹고 반찬 꾸러미도 싸가지고 갈수 있습니다.</div>
                    <div>■ 체험정보</div>
                    <div class="step1">○ 김치담그기</div>
                    <div class="step2">1)비용 및 인원 : 15,000원~ (식사포함시 5,000~8,000원 추가) 10인이상 (소수인원 가격조정)</div>
                    <div class="step2">2)기타 : 김치체험 후 1kg 포장</div>
                    <div class="step1">○ 화합의비빔밥 - 전통방식의 비빔밥 만들기 체험</div>
                    <div class="step2">1)비용 및 인원 : 10,000~15,000원 ※5인1조와 1인 놋그릇 가격 다름) 10인이상 (소수인원 가격조정)</div>
                    <div class="step1">○ 인절미 - 떡 매치기</div>
                    <div class="step2">1)비용 및 인원 : 8,000~10,000원 (인원수에 따름) 10인이상</div>
                    <div class="step2">2)기타 : 전통식 인절미 매치고 포장해가기</div>
                    <div class="step1">○ 전통 유과 만들기 및 한과체험</div>
                    <div class="step2">1)비용 및 인원 : 10,000원~ 10인이상</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle6}</div>
                <div class="addr">{addr6} {addrdtl6}</div>
                <a href="{homepage6}"><div class="homepage">{homepage6}</div></a>
                <div class="content">
                    <div>■ 전주시 서쪽에 위치한 원동은 인근에 전주수목원이 자리하고 있어 봄에는 배꽃과 복숭아꽃이 만발하는 아름다운 마을이다. </div>
                    <div class="step1">마을특산물 - 한과, 두부, 청국장, 조청 등</div>
                    <div>■ 체험정보</div>
                    <div class="step1">○ 배꽃인공수분</div>
                    <div class="step2">1) 운영기간 : 4월 배꽃필시기</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 10명 100명 3,000원</div>
                    <div class="step1">○ 감자캐기</div>
                    <div class="step2">1) 운영기간 : 6월 하지</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 10명 100명 6,000원</div>
                    <div class="step2">3) 기타 : 감자 1㎏ 증정</div>
                    <div class="step1">○ 배따기</div>
                    <div class="step2">1) 운영기간 : 10월</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 10명 100명 10,000원</div>
                    <div class="step2">3) 기타 : 배 3개</div>
                    <div class="step1">○ 단감따기</div>
                    <div class="step2">1) 운영기간 : 10월</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 10명 100명 6,000원</div>
                    <div class="step2">3) 기타 : 단감 15개</div>
                </div>
            </div>
            <div class="info_culturl">
                <div class="datatitle">{datatitle7}</div>
                <div class="addr">{addr7} {addrdtl7}</div>
                <a href="{homepage7}"><div class="homepage">{homepage7}</div></a>
                <div class="content">
                    <div>■ 모악산 자락에 위치하여 공기가 좋고 마을 인심이 풍성하며 도심에서 가까워 체험을 하기에는 더욱 좋고, 근교에 완산체련공원과 인접해 문화적 해택을 접할 수 있는 마을이다. </div>
                    <div class="step1">○ 마을특산물 - 두부, 한과, 조청, 청국장 등</div>
                    <div>■ 체험정보</div>
                    <div class="step1">○ 두부만들기</div>
                    <div class="step2">1) 운영기간 : 1~2, 7~8월 제외</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 20명 70명 7,000원</div>
                    <div class="step2">3) 기타 : 두부 1모 증정, ※준비물:두부통 다육심기 상시 1시간 20명 60명 6,000원 다육화분 증정</div>
                    <div class="step1">○ 딸기따기</div>
                    <div class="step2">1) 운영기간 : 4월 중순~5월</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 20명 유치부 8,000원 초등생 10,000원</div>
                    <div class="step2">3) 기타 : 딸기 1㎏ 증정</div>
                    <div class="step1">○ 감자캐기</div>
                    <div class="step2">1) 운영기간 : 6월 하지</div>
                    <div class="step2">2) 비용 및 인원 : 40분 10명 7,000원</div>
                    <div class="step2">3) 기타 : 감자 2㎏ 증정, ※준비물:장갑 수영장 7~8월 10:00~18:00 300명 8,000원 평상무료 대여, 상담요함</div>
                    <div class="step1">○ 고구마캐기</div>
                    <div class="step2">1) 운영기간 : 10월</div>
                    <div class="step2">2) 비용 및 인원 : 1시간 10명 7,000원</div>
                    <div class="step2">3) 기타 : 고구마 2㎏ 증정, ※준비물:장갑 김장담기 11월 1시간 20명 70명 13,000원 김장 1㎏ 증정, ※준비물:앞치마, 토시</div>
                </div>
            </div>
        </div>
    </body>
    </html>
'''.format(datatitle0=datatitle[0],addr0=addr[0],addrdtl0=addrdtl[0],homepage0=homepage0,datatitle1=datatitle[1],addr1=addr[1],addrdtl1=addrdtl[1],homepage1=homepage1,datatitle2=datatitle[2],addr2=addr[2],addrdtl2=addrdtl[2],homepage2=homepage2,datatitle3=datatitle[3],addr3=addr[3],addrdtl3=addrdtl[3],homepage3=homepage3,datatitle4=datatitle[4],addr4=addr[4],addrdtl4=addrdtl[4],homepage4=homepage4,datatitle5=datatitle[5],addr5=addr[5],addrdtl5=addrdtl[5],homepage5=homepage5,datatitle6=datatitle[6],addr6=addr[6],addrdtl6=addrdtl[6],homepage6=homepage6,datatitle7=datatitle[7],addr7=addr[7],addrdtl7=addrdtl[7],homepage7=homepage7))
