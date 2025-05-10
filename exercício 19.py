print('Fahrenheit', '|  Celsius')

for fahrenheit in range(45,80+1,1):
    celsius = 5/9 * (fahrenheit - 32)
    print(fahrenheit,'º       |  f"{celsius:.3f}"','º')