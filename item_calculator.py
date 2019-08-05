#설명
'''어떤 캐릭터의 별을 올려주려면 메모리 피스(피스)라는 조각이 필요하다.

조각을 얻으려면 이벤트 지역을 돌아야 한다.
이벤트는 '하드', '하드(보스)', '베리하드(보스)', '상자열기' 이렇게 4가지가 있다.

하드는 지역당 3번을 돌 수 있고 1-1 1-3 1-5 총 세가지 지역이 있고 피스의 드랍 확률은 30퍼센트다. # 리스트 kokkoro
(하드, 베하)보스를 잡으면 토벌증은 주어서 상자를 열 수 있다.
베리하드(보스)는 잡으면 조각을 1개 준다. # very_hard = 1
상자열기는 토벌증을 모아서 열 수 있으며 매일 3조각 정도를 얻는다. #box = 3'''

#조건 very_hard = 1 box = 3 매일 매일 얻는 개수

import random

def count(area, pieces): # 이벤트 기간동안 특정 지역에서 캔 개수
        result = 0
        for p in pieces:
                result += p
        return print(area, result,'개')

kokkoro = [1,1,1,0,0,0,0,0,0,0] # 30퍼센트 1 = 당첨 0 = 꽝

piece_1 = [] # 1-1
piece_2 = [] # 1-3
piece_3 = [] # 1-5

total = 0 # 결과값 초기화
time_out = 14 # 이벤트 종료까지 남은 일 수
box = 3 # 상자에서 얻는 조각
very_hard = 1 # 베리하드 클리어 보상 조각

for i in range(time_out): #매일매일이니 for문으로

        a,b,c=0,0,0 # 3지역(1-1 1-3 1-5)개수 초기화

        for j in range(3):

                x = random.choice(kokkoro) # kokkoro에서 하나를 픽
                y = random.choice(kokkoro)
                z = random.choice(kokkoro)
                
                a += x # x의 값을 더함 (개수)
                b += y
                c += z
        
        piece_1.append(a) # 3번 돌려서 나온 결과값을 리스트에 추가
        piece_2.append(b)
        piece_3.append(c)

        hard = a + b + c
        total += hard + very_hard + box

print('남은 이벤트 기간:',time_out,'일')
count('EH 1-1',piece_1)     # 이벤트 하드 1-1
count('EH 1-3',piece_2)     # 이벤트 하드 1-3
count('EH 1-5',piece_3)     # 이벤트 하드 1-5
print('베리하드, 상자에서 획득:',(very_hard + box) * time_out,'개')
print('총합:',total,"개")   # 예상 총합 개수

#print(piece_1)
#print(piece_3)
#print(piece_5) #리스트
