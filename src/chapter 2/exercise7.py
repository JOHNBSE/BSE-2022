#in the US dollar denominations, there is paper money and coins. The paper money has the following dollar notes:
#100 dollars
#50 dollars
#20 dollars
#10 dollars
#5 dollars
#1 dollar
#The coins have are in the following forms:
#Quarter 25 cents (0.25 of a dollar)
#Dime 10 cents ( 0.1 of a dollar)
#Nickel 5 cents (0.05 of a dollar)
#Penny 1 cent (0.01 of a dollar)
#write a program that lets a user input an amount of money that they need to make change for ,
#and dispenses the correct amount of change( in US currency). assume dollar bill 20 is the largest denomination.

a=float(input('please put the money u want to be changed: '))
twenties=a//20
print(twenties,'twenties')
r_1=a%20
tens=r_1//10
print(tens,'tens')
r_2=r_1%10
fives=r_2//5
print(fives,'fives')
r_3=r_2%5
ones=r_3//1
print(ones,'ones')
r_4=r_3%1
qrts=r_4//0.25
print(qrts,'quarters')
r_5=r_4%0.25
dims=r_5//0.1
print(dims,'dimes')
r_6=r_5%0.1
nickels=r_6//0.05
print(nickels,'nickels')
r_7=r_6%0.05
pennies=r_7//0.01
print(pennies,'pennies')