#1

import re
from datetime import datetime, timedelta

bugun = datetime.today() #date time kutubxonsi yordamida bugungi sanani 'bugun' nomli o'zgaruvchiga yukladik
for i in range(11): # loop yordamida 10 ta raqamni 'i' ga yukladik
    sana = bugun + timedelta(weeks=2*i) # bu yerda esa timedelta muduliga murojat qilib weeks ni esa 'i' ni 2ga ko'paytmasiga tenglab oldik hamda ushbu yig'indini bugun bilan qo'shdik
    print(sana.strftime("%Y-%m-%d")) # strftime yordamida sana standartini o'zimizga moslab chiqarib olamiz

#2
ramazan25 = datetime(2025,3,1) # ramazon vaqtini huddi konstantadek aniq bir sanaga to'g'irlab olamiz
hayit = datetime(2025,3,31) # qurbon haitini ham tepadakidek usulda yozib olamiz
ramazan25_2 = bugun-ramazan25 # va bugungi sanadan ramazon25 ni ayiramiz
hayit2 = bugun-hayit # bu yerdaham shunday
print("Ramazangacha:", (ramazan25_2).days, "Hayitgacha", (hayit2).days) #print() orqali ekrangachiqaramiz , hamda bu yerda .days() ham ishlatilgan bu bizga qaytgan javobdan faqat kunlarni olib beradi

#3
input_num =  input('Enter Phone Num : ') # input() yordamida foydalanuvchidan tel raqamini kiritishi so'raldi
checker = "^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$" # andoza

if re.match(checker,input_num): # if yordamida re kutubxonasi ichidagi match orqai andoza yordamida user kiritgan tel raqam standartlari tekshiriladi
    print('✅') # agarda shart to'g'ri bo'lsa done emojisi qaytadi
else:
    print('Raqamni to\'liq kiriting') # agarda hato bo'lsa manashi text qaytadi

#4


def find_url(text):
    result = re.search("(?P<url>https?://[^\\s]+)", text) # RE.SEARCH yordamida berilgan andoza orqali text dan url ni izlaydi

    if result: # agarda shart to'g'ri bo'la
        return result.group("url") # bu joyda .group yordamida birlashtirib qiymat qaytaradi
    else:
        return None # aks holda None qiyamatqaytaradi

myString = "shfuhiufgdusihttps://github.com" # example text

url = find_url(myString) # bu joyda fin url funksiyasiga murojat qilib unga parametr sifatida myStringni uzatamiz
if url: # agarda shart to'g'ri bo'lsa
    print("URl:", url) # url output
else:
    print("URL not found") # aks holda Url not found
