# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))

# if a <= b <= c:
#     print("Shart qanoatlantiriladi.")
# else:
#     print("Shart qanoatlantirilmaydi.")

# Foydalanuvchidan ballni olish
# ball = int(input("Talaba to'plagan ballni kiriting: "))

# # Ballga qarab bahoni aniqlash
# if 90 <= ball <= 100:
#     baho = 5
# elif 70 <= ball < 90:
#     baho = 4
# elif 60 <= ball < 70:
#     baho = 3
# elif 0 <= ball < 60:
#     baho = 2
# else:
#     baho = "Noto'g'ri ball"

# # Natijani chiqarish
# print("Talaba bahosi:", baho)




# # Haroratni foydalanuvchidan so'raymiz
# harorat = float(input("Haroratni kiriting: "))

# if harorat > 45:
#     print("O'ta issiq")
# elif 38 <= harorat <= 45:
#     print("Issiq")
# elif 28 <= harorat < 38:
#     print("O'rtacha issiq")
# elif 18 <= harorat < 28:
#     print("Iliq")
# elif 11 <= harorat < 18:
#     print("Salqin")
# elif 0 <= harorat < 11:
#     print("Sovuq")
# else:
#     print("O'ta sovuq")



def check_color(color):
    match color:
        case 'qizil':
            return "Bu qizil rang."
        case 'yashil':
            return "Bu yashil rang."
        case 'kok':
            return "Bu ko'k rang."
        case _:
            return "Bu boshqa rang."

# Misol
print(check_color('qizil')) 
print(check_color('sariq'))
