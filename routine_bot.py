import asyncio
from datetime import datetime
from telegram import Bot

TOKEN = "8397526678:AAFbtA3_Q1jOKCclzuVw0bLq04m92-j-33w"

bot = Bot(token=TOKEN)

isSend = False
lastSendTime = ""

class Routine:
    def __init__(self, time, message,details):
        self.time = time
        self.message = message
        self.details = details

running = Routine("08:00", "아침 유산소", "뚝방가서 30분 뛰기")
English1 = Routine("09:15", "영어 공부1", "섀도잉 집중, 모르는 표현 메모")
coding = Routine("10:45", "코딩 공부", "파이썬 OOP, 포모도로 25+5")
English2 = Routine("14:45", "영어 공부2", "혼잣말 아웃풋, 영어 일기 3~5문장 (카페)")
Reading = Routine("16:15", "독서", "책 20페이지 이상 읽기 (카페)")
Excercise = Routine("22:00", "근력 운동", "푸쉬업 3세트 x 15회 스쿼트 3세트 x 15회 런지 3세트 x 10회 (좌우) 아령 숄더프레스 3세트 x 12회 아령 컬 3세트 x 12회 플랭크 3세트 x 30초 크런치 3세트 x 15회 세트 사이 휴식 45~60초, 마지막 스트레칭 10분!")

routines = [running, English1, coding, English2, Reading, Excercise]

async def main ():
       while True:
        global isSend, lastSendTime
        nowTime = datetime.now().strftime("%H:%M")

        if nowTime != lastSendTime:
            isSend = False
            lastSendTime = nowTime

        for routine in routines:
            if routine.time == nowTime and not isSend:
                await bot.send_message(chat_id=7010307578 , text=f"{routine.message} 시간입니다! \n{routine.details}")
                isSend = True
                break
        

        await asyncio.sleep(30)
        

asyncio.run(main())

        
  