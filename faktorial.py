# def faktorial(N):
#     i = 1
#     fakt = 1
#     while i != N +1:
#         fakt = fakt * i
#         i += 1
#     return fakt
# if __name__ == '__main__':
    # print(faktorial(3))
# print(faktorial(4))


# N = int(float(input('N: ')))
# def faktorial(N):
#     fakt = 1
#     for i in range(1, N + 1):
#         fakt *= i
#     return fakt
# print(faktorial(N))


# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# def addNums(a,b):
#     summa = a + b
#     return summa
# print(addNums(a,b))

# def getLargest(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>c:
#             return b
#         else:
#             return c
# print(getLargest(a,b,c))

# def faktorial(N):
#     i=1
#     fakt=1
#     while i!=N+1:
#         fakt = fakt * i
#         i += 1
#     return fakt
# print(faktorial(c))

def findNum(N:15):
    for n in range(1, N):
        ans = input(f"Siz {n}-o'yladingiz? (y/n)")
        if ans == 'y':
            print("Yutding!")
            return n 
        else:
            print("Yutqazding!")
findNum(15)