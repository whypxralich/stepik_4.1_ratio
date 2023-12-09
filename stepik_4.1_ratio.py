#stepik_4.1_ratio
num = int(input())

n1 = num // 1000
n2 = (num //100)%10
n3 = ((num//10)%100)%10
n4 = ((num%1000)%100)%10

if n1 + n4 == n2 - n3:
    print ("ДА")
else:
    print("НЕТ")