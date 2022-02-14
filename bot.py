import discord

client = discord.Client()

@client.event
async def on_ready():
    print('로그인성공')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content =="명령어":
        embed = discord.Embed(title="명령어List",color=0x0000ff,description = "수정사항있으면 알려주세요~")
        embed.add_field(name="\r\t v 발탄 v \r\t",value="발탄1\r\n발탄2\r\n노말=하드")
        embed.add_field(name="\t v 비아키스 v \t",value="비아1\r\n비아2\r\n비아3\r\n하드미제작")
        embed.add_field(name="\t v 쿠크세이튼 v\t",value="쿠크1\r\n쿠크2\r\n쿠크3")
        embed.add_field(name="\t v 아브렐슈드 v\t",value="아브1\r\n아브2\r\n아브3\r\n아브4\r\n아브5\r\n아브6\r\n하드 미제작")
        await message.channel.send(embed=embed)

    if message.content =="발탄1":
        embed = discord.Embed(title="발탄 1관문 루가루",color=0x0000ff,description = "준비물 : 회오리수류탄, 만능물약")
        embed.add_field(name="v 45줄 v\t\t",value="보스 채널링/7시 대기후 진입")
        embed.add_field(name="v 40줄 v\t\t",value="파란색난입 / 빨12 - 파 6\r\n(금구슬은파랑)")
        embed.add_field(name="v 33줄 v\t\t",value="어글자 바뀔때마다 암흑디버프+1 \r\n 5스택중첩시 감금")
        embed.add_field(name="v 30줄 v\t\t",value="구슬먹기 후 무력\r\n 보스 체력바 아래 구슬갯수확인")
        embed.add_field(name="v 25줄 v\t\t",value="빨간색난입 / 빨12 - 파6\r\n(금구슬은빨강)")
        embed.add_field(name="v 15줄 v\t\t",value="구슬먹기 후 무력\r\n 보스 체력바 아래 구슬갯수확인")
        embed.add_field(name="v 15~0줄 v\t\t",value="검은안개 > 가장먼사람 공포>무력화\r\n공포 걸린사람은 핑!!")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i13464248708.jpg')
        await message.channel.send(embed=embed)


    if message.content =="발탄2":
        embed = discord.Embed(title="발탄 2관문 발탄",color=0x0000ff,description = "준비물 : 파괴폭탄(7명)or부식폭탄(1명)\r\n시간정지물약")
        embed.add_field(name="\t v 160줄 v\t",value="갑옷파괴3-1-11-9\r\n부식폭탄: 박치기전\r\n파괴폭탄:박치기후")
        embed.add_field(name="\t v 130줄 v\t<",value="전멸기 - 피자패턴후 전멸 \r\n 바훈투르장판,로아운의 기운으로 생존")
        embed.add_field(name="\t v 110줄 v\t",value="임포스터패턴 \r\n 빨간장판 고정후 노란장판에서 or 안전지대이동")
        embed.add_field(name="\t v 88줄 v\t",value="지형파괴\r\n 좌or우 사이즈 지형파괴 안전지대로이동")
        embed.add_field(name="\t v 65줄 v\t",value="버러지카운터\r\n모여서 카운터")
        embed.add_field(name="\t v 30줄 v\t",value="지형파괴\r\n나머지 지형파괴")
        embed.add_field(name="\t v 16줄 v\t",value="4방향찍기+연환파신권\r\n바훈투르생존or\r\n연환파신권3번찍은후 시간정지물약")
        embed.add_field(name="\t v 15줄 유령 v\t",value="피40줄회복\r\n 카운터후 발탄에게 붙기\r\n잡기39/27/14줄")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i13464248708.jpg')
        await message.channel.send(embed=embed)


    if message.content =="비아1":
        embed = discord.Embed(title="비아키스1관문 모르페",color=0x0000ff,description = "준비물 : 회오리수류탄/시간정지물약/신속로브")
        embed.add_field(name="\t v 49줄 v\t",value="구슬넣기\r\n빨-파-초-흰-검 순서")
        embed.add_field(name="\t v 36줄 v\t",value="구슬먹기-무력\r\n파랑-11 / 5 \r\n 검정-1 / 7")
        embed.add_field(name="\t v 30줄 v\t",value="파티교체 쾌락-욕망")
        embed.add_field(name="\t v 25줄 v\t",value="안전장판 브리핑\r\n12 / 3 / 6 / 9")
        embed.add_field(name="\t v 12줄 v\t",value="구슬먹기-무력\r\n파랑-11 / 5 \r\n 검정-1 / 7")
        embed.add_field(name="\t v 5줄 v\t",value="광폭화-별거없음")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i16216326567.jpg')
        await message.channel.send(embed=embed)    


    if message.content =="비아2":
        embed = discord.Embed(title="비아키스2관문 비아키스",color=0x0000ff,description = "준비물 : 시간정지물약/신속로브")
        embed.add_field(name="\t v 144줄 v\r\t",value="거리두기 - 겹치지않게 선뒤\r\n시계방향 회전")
        embed.add_field(name="\t v 120줄 v\t",value="환영날개-보-접/빨-핀")
        embed.add_field(name="\t v 90줄 v\t",value="거리두기 - 겹치지않게 선뒤\r\n시계방향 회전")
        embed.add_field(name="\t v 65줄 v\t",value="검 구슬먹기- 각 자리로가서 검정구슬 먹기\r\n3은 스페가 처리")
        embed.add_field(name="\t v 50줄 v\t",value="욕망주입 - 피격시 디버프+1\r\n 3중첩시 똥장판 활성화(정화로 관리)")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i16216326567.jpg')
        await message.channel.send(embed=embed)  


    if message.content =="비아3":
        embed = discord.Embed(title="비아키스3관문 비아눈나",color=0x0000ff,description = "준비물 : 시간정지물약/회오리수류탄/수면폭탄")
        embed.add_field(name="\t v 175줄 v\t",value="늪(9시 설치)\r\n신속-멀리서 배치\r\n절망-9시 간격을두고 배치")
        embed.add_field(name="\t v 155줄 v\t",value="칼/석상패턴\r\n매혹게이지 70%이상 칼핑\r\n 매혹게이지 70%이하 핑찍힌곳에 석상이있으면 이동")
        embed.add_field(name="\t v 138줄 v\t",value="아재절단기\r\n 12시로 이동 매혹게이지 0으로 만들기\r\n똥장판 뭉쳐서 빼기")
        embed.add_field(name="\t v 120줄 v\t",value="왕좌폭발 - 카운터X \r\n 다같이 매혹걸리기")
        embed.add_field(name="\t v 105줄 v\t",value="무력후 시간정지물약사용")
        embed.add_field(name="\t v 75줄 v\t",value="늪(9시 설치)\r\n신속-멀리서 배치\r\n절망-9시 간격을두고 배치")
        embed.add_field(name="\t v 52줄 v\t",value="촉수제거 - 매혹게이지 70%이상시 데미지 들어감")
        embed.add_field(name="\t v 10줄 v\t",value="매혹게이지 제거")
        embed.add_field(name="\t v 0줄 v\t",value="본체찾기+무력화 - 미니맵에 보스 위치확인\r\n중앙-캐릭터-미니맵보스 일자로 선후\r\n미니맵보스를 바라보며서있다가\r\n중앙에서 생성되는 장판을 밟으며\r\n미니맵 보스 뒤로 이동후 무력")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i16216326567.jpg')
        await message.channel.send(embed=embed)      

  
    if message.content =="쿠크1":
        embed = discord.Embed(title="쿠크1",color=0x0000ff,description = "준비물 : 회오리수류탄, 성스러운 부적,시간 정지물약")
        embed.add_field(name="\t v 128줄 v\t",value="반격 무력화\r\n보라색 방패가 없는곳에서 무력화 ")
        embed.add_field(name="\t v 100줄 v\t",value="세이튼 찾기\r\n1-5-7-11 하트핑")
        embed.add_field(name="\t v 88줄 v\t",value="댄스 타임- 세이튼동작 따라하기")
        embed.add_field(name="\t v 60줄 v\t",value="반격 무력화\r\n보라색 방패가 없는곳에서 무력화")
        embed.add_field(name="\t v 48줄 v\t",value="주사위(스페이드-하트 / 클로버-다이아)\r\n 6시 검검빨빨 거리두고 서기\r\n3인 감금 처음나오는 카드먹기\r\n1인 감금3번째카드")
        embed.add_field(name="\t v 22줄 v\t",value="세이튼 찾기\r\n1-5-7-11 하트핑")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i13411451557.jpg')
        await message.channel.send(embed=embed)

    if message.content =="쿠크2":
        embed = discord.Embed(title="쿠크1",color=0x0000ff,description = "준비물 : 성스러운 부적,시간 정지물약")
        embed.add_field(name="\t v 125줄 v\t",value="거대세이튼등장\r\n폭탄/공튀기기 피하기 ")
        embed.add_field(name="\t v 110줄 v\t",value="광기장판\r\n빨간장판-2인\r\n파란장판-1인\r\n뒤돌기")
        embed.add_field(name="\t v 95줄 v\t",value="쿠크 찾기\r\n표식자 카드위로")
        embed.add_field(name="\t v 80줄 v\t",value="카드미로")
        embed.add_field(name="\t v 55줄 v\t",value="벨가패턴\r\n12시 시작\r\n별 회전방향 2.5회  이동\r\n2.5회 이동후 밖으로 탈출")
        embed.add_field(name="\t v 25줄 v\t",value="쿠크 찾기\r\n표식자 카드위로")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i13411451557.jpg')
        await message.channel.send(embed=embed)

    if message.content =="쿠크3":
        embed = discord.Embed(title="쿠크1",color=0x0000ff,description = "준비물 : 성스러운 부적,시간 정지물약")
        embed.add_field(name="\t v 155줄 v\t",value="1마리오\r\n칼날피해서 무력화 ")
        embed.add_field(name="\t v 125줄 v\t",value="2마리오\r\n갈고리 피해서 무력화")
        embed.add_field(name="\t v 90줄 v\t",value="쇼타임\r\n6시뭉쳐서 이동\r\n폭탄지우기\r\n노란구슬 피하기")
        embed.add_field(name="\t v 80줄 v\t",value="3마리오\r\n칼날+갈고리 피해서 무력화")
        embed.add_field(name="\t v 55줄 v\t",value="4마리오\r\n칼날+갈고리 피해서\r\n7시/11시 아재패턴>래버당기기후\r\n무력화가능")
        embed.add_field(name="\t v 0줄 v\t",value="빙고\r\n3번째 폭탄마다 1줄완성")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/01/05/bbs/i13411451557.jpg')
        await message.channel.send(embed=embed)        
    
    if message.content =="아브1":
        embed = discord.Embed(title="아브1",color=0x0000ff,description = "준비물 : 2파티 수폭or회폭\r\n1파티\r\n슬픔-투견(부파),석상(검은구슬 드리블)\r\n절망-투견(쫄마리제거),석상(일정시간마다 무력)\r\n2파티\r\분노-투견(타수),석상(피증디버프3~4무력)\r\n침식-투견(무력),석상(디버프시전시-상태이상기)")
        embed.add_field(name="\t v 85줄 v\t",value="장판밟기/1파티 곱3 - 2파티 곱3+1")
        embed.add_field(name="\t v 45줄 v\t",value="카운터 6회\r\n망치가 헤드\r\n망치들어 올릴때")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2021/11/10/bbs/i14597737939.jpg')
        await message.channel.send(embed=embed)

    if message.content =="아브2":
        embed = discord.Embed(title="아브2",color=0x0000ff,description = "준비물 : 수폭,회폭,시정")
        embed.add_field(name="\t v 130줄 <\t",value="주황구슬\r\n구체 먹은 3명이 다이아장판 밟기")
        embed.add_field(name="\t v 110줄 v\t",value="파&빨-구슬\r\n파&빨표식자 구슬x\r\n표식없는 사람 구슬1개 먹기")
        embed.add_field(name="\t v 80줄 v\t",value="무력화+구슬파괴\r\n표식자 검은구슬뒤로이동후 표식이사라지면 이동기로 회피\r\n흰구슬-타수\r\n보라구슬-무력")
        embed.add_field(name="\t v 45줄 v\t",value="빨간구슬 생존\r\n3,6,9,12 구슬 부순뒤  입장\r\n구슬위 표시로 입장가능  인원확인")
        embed.add_field(name="\t v 40줄 v\t",value="몽환의 기사\r\n빠르게 제거")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2021/11/10/bbs/i14542768509.jpg')
        await message.channel.send(embed=embed)

    if message.content =="아브3":
        embed = discord.Embed(title="아브3",color=0x0000ff,description = "준비물 : 수폭,회폭,시정")
        embed.add_field(name="\t v 140줄 v\t",value="운석+무력화\r\n1팟 곱3\r\n2팟 곱3+1")
        embed.add_field(name="\t v 100줄 v\t",value="무력화\r\n고양이눈=보면안됨\r\n둥근눈=보기")
        embed.add_field(name="\t v 40줄 v\t",value="창/낫\r\n처음 밟은 장판과 동일한 장판 지우기")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2021/11/10/bbs/i14528776276.jpg')
        await message.channel.send(embed=embed)        

    if message.content =="아브4":
        embed = discord.Embed(title="아브4",color=0x0000ff,description = "준비물 : 회폭,시정,화폭\r\n노란규브 = 구슬파괴후 구슬먹고 장판위 무력\r\n(구슬파괴자,노란구슬먹은사람은 장판밖에서 구체막기)\r\n파란큐브 = 전우조무력\r\n빨간큐브=오브획득후 마법진이동 나머지 무력\r\n파란큐브 = 변안전\r\n빨간큐브=모서리안전")
        embed.add_field(name="\t v 170줄 <\t",value="전멸기\r\n 첫 입장 색상")
        embed.add_field(name="\t v 160줄 v\t",value="형상변환")
        embed.add_field(name="\t v 135줄 v\t",value="형상변환\r\n120줄 전멸기 색상")
        embed.add_field(name="\t v 120줄 v\t",value="전멸기\r\n135줄 색상패턴")
        embed.add_field(name="\t v 95줄 v\t",value="무력화\r\n별모양")
        embed.add_field(name="\t v 65줄 v\t",value="형상변환")
        embed.add_field(name="\t v 55줄 v\t",value="전멸기\r\n65줄 색상패턴")
        embed.add_field(name="\t v 40줄 v\t",value="형상변환")
        embed.add_field(name="\t v 20줄 v\t",value="무력화\r\n별모양")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2021/11/10/bbs/i14589905148.jpg')
        await message.channel.send(embed=embed)   

    if message.content =="아브5":
        embed = discord.Embed(title="아브5",color=0x0000ff,description = "준비물 : 회수/신속/시정")
        embed.add_field(name="\t v 180줄 v\t",value="낙인\r\n 번호 곱하기2")
        embed.add_field(name="\t v 144줄 v\t",value="딜컷(문양사라질때까지)\r\n140줄 곱3자리이동\r\n즉사기=가로-세로-가로-세로")
        embed.add_field(name="\t v 110줄 v\t",value="무력-포탈-능지\r\n불들어온순서대로 무력\r\n1팟 인당3개\r\n2팟1인 12개\r\n껍질까기+무력+순서기억")
        embed.add_field(name="\t v 85줄 v\t",value="낙인\r\n 번호 곱하기2")
        embed.add_field(name="\t v 54줄 v\t",value="딜컷(문양사라질때까지)\r\n50줄 곱3+1자리이동\r\n즉사기=9-3-12-6")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/02/02/bbs/i14210105413.png')
        await message.channel.send(embed=embed)         

    if message.content =="아브6":
        embed = discord.Embed(title="아브6",color=0x0000ff,description = "준비물 : 회수or암수/신속/시정")
        embed.add_field(name="\t v 220줄 <\t",value="몽환혼란\r\n추방디버프 - 모래폭풍비벼해제")
        embed.add_field(name="\t v 210줄 v\t",value="문양\r\n반전-정상-반전")
        embed.add_field(name="\t v 188줄 v\t",value="노메\r\n12 or 6\r\n12추천")
        embed.add_field(name="\t v 137줄 v\t",value="노메\r\n6 or 12\r\n6추천")
        embed.add_field(name="\t v 112줄 v\t",value="찬미\r\n중앙7시 대기후 이동\r\n1팟-곱3 / 2팟-곱3+1자리로이동\r\n노갈구슬2개 먹고 흰구슬 떨리면 들어가기\r\n 내부: 외부 브리핑대로 카운터or무력\r\n외부: 시계-무력 / 반시계-카운터")
        embed.add_field(name="\t v 87줄 v\t",value="노메\r\n12 or 6")
        embed.add_field(name="\t v 62줄 v\t",value="몽환혼란\r\n추방디버프 - 모래폭풍비벼해제")
        embed.add_field(name="\t v 37줄 v\t",value="노메\r\n6 or 12")
        embed.add_field(name="\t v 32줄 V\t",value="문양\r\n이난나추천")
        embed.add_field(name="\t v 25줄 V\t",value="타일파괴\r\n 파메 중앙 금지")
        embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/02/02/bbs/i15252768436.png')
        await message.channel.send(embed=embed)         

client.run('OTQxOTM3NjM3ODgxNjk2Mjc2.YgdNyQ.PDd8IRxovjyl7jBXJZ8fSsTYdqU')