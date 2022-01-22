#write a program which prompts the user for a celsius temperature, convert the temperature to fahrenheit and prints out the converted temperature
celcius=float(input('please write your temperature: '))
fahrenheit=round(((celcius*1.8)+32),2)
print(fahrenheit)