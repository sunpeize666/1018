'''
    적성일 : 2023년 10월 18일
    작성자 : 202195057 손패택
    설면: 
'''

fruits = []


for i in range(5) :
    fruit_name = input(str(i+1) + ". 좋아하는 과일의 이름을 입력하시오 : ")
    fruits.append(fruit_name)  

print("입력한 과일 리스트 : ", fruits)


favo_fruit = input("좋아하는 과일 하나를 입력하세요. : ")

if favo_fruit in fruits :
    print(f'{favo_fruit}은(는) 당신이 좋아하는 과일입니다.')
else :
    print(f'{favo_fruit}은(는) 당신이 좋아하는 과일이 아닙니다.')






