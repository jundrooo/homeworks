#1
def arifmetik_amal(n1, n2, amal):
  while True:
    if amal == '+':
        natija = n1 + n2
    elif amal == '-':
        natija = n1 - n2
    elif amal == '*':
        natija = n1 * n2
    elif amal == '/':
        if n2 != 0:
            natija = n1 / n2
        else:
            natija = "Nolga bo'lib bo'lmaydi"
    else:
        natija = "Noto'g'ri amal"
    return natija


n1 = float(input("Birinchi sonni kiriting: "))
n2 = float(input("Ikkinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal in ['+', '-', '*', '/']:
    print("Natija:", arifmetik_amal(n1, n2, amal))
else:
    print("Noto'g'ri amal kiritildi!")



#2
a_list = [1,2,3,4,5]
b_list = ['text1' , 'text2']
relist = [*a_list, *b_list]
print(relist)
