# 문자열 https://www.acmicpc.net/step/7

# Q_11654 아스키 코드
'''print(ord(input()))'''

# Q_11720 숫자의 합
'''n = int(input())
n = list(input())
sum = 0
for i in n:
    i = int(i)
    sum += i
print(sum)'''

# Q_10809 알파벳 찾기
'''import string as s
S=list(input())
a=list(s.ascii_lowercase)
R=[]
for i in a:
    try:
        r=S.index(i)
    except ValueError:
        print(-1,end=' ')
    else:
        print(r,end=' ')'''

# Q_2675 문자열 반복
'''T=int(input())
for i in range(T):
    r=''
    R,S=input().split()
    R=int(R)
    S=list(S)
    for j in S:
        r+=j*R
    print(r)'''

# Q_1157 단어 공부
'''import string as s
r=[]
S=input().lower()
S=list(S)
a=list(s.ascii_lowercase)
for i in a:
    s=S.count(i)
    r.append(s)
x=max(r)
y=r.count(x)
x=r.index(x)
if y==1:
    print(a[x].upper())
else:
    print('?')'''

# Q_1152 단어의 개수
'''print(len(list(input().split())))'''

# Q_2908 상수
'''a,b=input().split()
a=''.join(reversed(a))
b=''.join(reversed(b))
a=int(a)
b=int(b)
print(max(a,b))'''

# Q_5622 다이얼
# 못 품
# 사용 리스트 for문
'''w=input()
s=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
r=0
for j in range(len(w)):
    for i in s:
        if w[j] in i:
            r += s.index(i)+3
print(r)'''

# Q_2941 크로아티아 알파벳
# 못 품
# 사용 replace
'''w=input()
s=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in s:
    w=w.replace(i,' ')
print(len(w))'''

# Q_1316 그룹 단어 체커
#  
n=int(input())
for i in range(n):
    w=input()