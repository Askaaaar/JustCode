# def square(a):
#     P = a*4
#     S = a ** 2
#     D = a ** 0.5
#     return P, S, D
#
#
# print(square(5))

# A = int(input())
#
#
# def season(A):
#     if A == 12 or A == 1 or A == 2:
#         return ("this is winter")
#     if A == 3 or A == 4 or A == 5:
#         return ("this is spring")
#     if A == 6 or A == 7 or A == 8:
#         return ("this is summer")
#     if A == 9 or A == 10 or A == 11:
#         return ("this is autumn")
#     else:
#         print("fuck off")
#
#
# print(season(A))


deposit = int(input())
years = int(input())
procent = int(input())


def bank():
    for i in range(0, years):
        money = (deposit/100)*procent
        total = money + procent
        return total


print(bank())
