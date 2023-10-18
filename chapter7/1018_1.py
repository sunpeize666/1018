'''
    적성일 : 2023년 10월 18일
    작성자 : 202195057 손패택
    설면: 
'''

fruits = ['달기','사과','바나나']
print("과일 목록 :",fruits)


fruits ("과일 목록(속바 추가) :", fruits)
fruits.append('망고')
print("과일 목록(망고 추가) :", fruits)



fruits = fruits + ['포도']
print("과일 목록(포도 추가)")

num - [1,2,3] + [4,5,6]
print("숫자 리스트 : ", num)

print("과일 목록에 망고가 있나요? ", '망고' in fruits)

for i in range(5) :
    fruit_name = input(str(i=1)) + ". 좋아하는 과일의 이름 입력하시오 : ")
    fruits.append(fruit_name)
    
print("압력한 과입 리스트 : ", fruits)