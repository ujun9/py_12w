# 32
# a = {3, 7, 9, 32, 99}
# b = {5, 7, 16, 27, 99}
# c = a|b
# d = a & b
# print(c, d)

# 33
# a = {3, 7, 9, 32, 99}
# b = {5, 7, 16, 27, 99}
# c = a - b
# d = a ^ b
# print(c, d)

# 34
# a = {3, 7, 9, 32, 99}
# a |= {100}
# print(a)

# 35
# a = {100, 200, 300, 400, 500}
# a.intersection_update( {400, 500, 600, 700, 800} )
# a.difference_update( {400, 500, 600, 700, 800} )
# a.symmetric_difference_update( {400, 500, 600, 700, 800} )
# print(a)

# 36
# a = {100, 200, 300, 400, 500}
# if (a == {100, 200, 300, 400, 500}):
#     print("동시")
# elif (a >= {100, 200, 300, 400, 500}):
#     print("상위")
# elif (a <= {100, 200, 300, 400, 500}):
#     print("부분")

# 37
# a = {3, 7, 9, 32, 99}
# a.add(1000)
# a.remove(99)
# print(a)

# 38
# multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
# print(multiples)