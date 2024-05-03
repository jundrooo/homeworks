def katta_sonni_top(sonlar):

    eng_katta = sonlar[0] #eng birinchi indexni eng kattasi deb oladi
    for son in sonlar: # sikl yordamida sonlardagi har bir element 'son'ga yuklanadi
        if son > eng_katta: # agarda son eng_katta(sonlar ro'yxatidagi 1 chi da turgan son) nomli o'zgaruvchidan katta bo'lsa shart true ->
            eng_katta = son # hamda shart bajarilishi bilan birga endi eng_katta son nomli o'zgaruvchuning qiymati 'son' nikiga teng bo'ladi yani son nomi o'zgaruvchining qiymatini o'zlashtiradi
    return eng_katta # shu bilan birg shart yakunlanganda keyin eng_katta son nomli o'zgaruchining qiymatini qaytaradi


def textCapitalize(list1):
    capList1 = [] # bo'sh ro'yxat(list)
    for list2 in list1: # loop yordamida list1 ning ichidagi har bir element ni list2 ga yuklab olinadi
        capList1.append(list2.capitalize()) # hamda .append() metodi yordamida capList1 ga list2 ga yuklanga elentlarni .capitalize() metodi yordamida qo'shiladi
    return capList1 # hamda capList1 qiymati qaytariladi


def juft_son_top(son1):
    juft_sonlar = []
    for son3 in son1:
        if son3%2 == 0:
            juft_sonlar.append(son3)
        else:
            continue
    return juft_sonlar


def fibo(sonlar):
    a,b = 1,0 # a hamda b qiymatlarini True(10) hamda False(0) ga tenglab olinadi
    while a < sonlar: # while yordamida toki false bo'lguncha davom etadi
        if b == sonlar: # agarda b(False) Sonlar nomli parametrga teng bo'lsa (yani False bo'lsa) ->
            return True # True qaytadi
        a,b = b, a + b # fibonachi ketma ketligini topish uchun
    return False # sikldan so'ng False qiymati qaytadi