import math

x = float(input("введіть x: "))
y = (math.sin(x ** 2) - math.tan(x - 8)) / math.log(math.fabs(x ** 3 - math.sin(x)))
print("Відповідь:", y )
