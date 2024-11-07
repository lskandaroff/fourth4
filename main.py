# Vazifa_____________________________________________

# 1

# count = 0
# def function():
#     def inner():
#         global count
#         count += 1
#         return count
#     return inner
#
# function()()
# function()()
# print(function()())

# 2
#
# def function(factor):
#     def inner():
#         return factor * factor
#     return inner
#
# print(function(5)())
# print(function(6)())

# 3

# def number():
#     total = 0
#     def inner(num):
#         nonlocal total
#         total += num
#         return total
#     return inner
#
# add_to_sum = number()
# print(add_to_sum(5))
# print(add_to_sum(6))

# 4

# def function():
#     total = 0
#     def qoshish(b):
#         nonlocal total
#         total += b
#         return total
#     def ayruv(b):
#         nonlocal total
#         total -= total
#         return total
#     return qoshish, ayruv
#
# qoshish_, ayrish_ = function()
#
# print(qoshish_(10))
# print(ayrish_(3))
# print(qoshish_(20))

# 5

# maxsulotlar = {"olma": 3000, "nok": 2000}
#
# def function():
#     def inner(maxsulot, new_count):
#         for i in maxsulotlar:
#             if i == maxsulot:
#                 chegirma = (maxsulotlar[maxsulot] // 100) * new_count
#                 return maxsulotlar[maxsulot] - chegirma
#
#     return inner
#
# print(function()("olma", 25))
# print(function()("nok", 15))

# 7

# parol = 123456
#
# def function():
#     def inner(add_parol):
#         global parol
#
#         if add_parol != parol:
#             return ("Parol notogri")
#         else:
#             return "Xush kelibsiz"
#
#     return inner
#
# print(function()(123456))







































