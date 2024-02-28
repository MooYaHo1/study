import sys

input = sys.stdin.readline # 로우레벨의 입력 함수(기존 input 보다 빠름) 
printf = sys.stdout.write # 프린트보다 빠르고 기능이 적다!
#---------------------------------------------------------------------------------
if i & 1: # 비트 연산자 and 연산을 통해 짝수면 맨뒤가 0 홀수면 맨 뒤가 1이다 그래서 i&1은 홀수
    i=0
#-------------
enumerate # 인덱스와 요소를 같이 반환시킴
my_list = ['apple', 'banana', 'cherry']

for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")
#----------------
abs() #정수표기

#--------------
