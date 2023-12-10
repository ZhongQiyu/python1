# 11/18

# group class

cache = dict()

def f(n): 
    if n < 1:
        return 0
    if n in [1,2]: 
        return n
        
    if cache.get(n) is not None:
        return cache[n]
    else:
        result = f(n-1) + f(n-2)
        cache[n] = result 
        return result
        
print(f(100))



# 12/2

a = 10
print((a))
print((a, 20))

# 浮点数 (float)
# 10.0
# 10.100; 10.010; 10.001
a = 10.001 # 0.00099...
b = 20
print(a + b) # 30.001想让他输出
print(float(1/7)+1)
# 1/7=0.(142857)* ~ 0.(1428); 逼近/近似

type(b)

"""
m = 10 # 10kg
a = 4.9 # 4.9m/s^2

f=ma
print(f)
"""

ph1 = 6.0
ph2 = 9.0
m1 = 0.4
m2 = 0.6

# 12/9

# 2.1 布尔值 (Boolean)

# 0: False
# 1: True

if 1:
    print("We have a correct Boolean value.")

if "abc" != "def":
    print("'abc' is not equal to 'def'.")

# 2.2

"""
10 == 10
11 != 13
"Katy" == "Katy"
20 < 45
15 >= 15
"Bob" == 32
30 <= 30
55 > 20
200 < 2000
"Jerry" == "jerry"
"""

# 2.3

"""
"Bob" == 32
print(ord("B")) # ord: ordinary (number) 原数; chr: character 字符
"""

l = "4"
m = '4'
n = 4
print(l == m == n) # AND: l == m AND m == n
print(l == m)

# 
1, 13
# dictionary 词典
# 关联两种数据 以建立规则
poker_rules = {1:'A', 11:'J', 12:'Q', 13:'K'} # 常量
print(l == m != n)

print(1 == 2 and 1 == 1) # short-circuiting 短路
print(1 == 1 or 1 == 2) # short-circuiting 短路
print((1 != 1) == (not (1 == 1)))
