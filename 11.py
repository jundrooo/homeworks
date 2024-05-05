#1

import re
from datetime import datetime, timedelta

bugun = datetime.today()
for i in range(11):
    sana = bugun + timedelta(weeks=2*i)
    print(sana.strftime("%Y-%m-%d"))

#2
ramazan25 = datetime(2025,3,1)
hayit = datetime(2025,3,31)
ramazan25_2 = bugun-ramazan25
hayit2 = bugun-hayit
print("Ramazangacha:", (ramazan25_2).days, "Hayitgacha", (hayit2).days)

#3
input_num =  input('Enter Phone Num : ')
checker = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

if re.match(checker,input_num):
    print('✅')
else:
    print('Raqamni to\'liq kiriting')

print(re.match(checker,input_num))

#4
import re

def find_url(text):
    result = re.search("(?P<url>https?://[^\s]+)", text)

    if result:
        return result.group("url")
    else:
        return None

myString = "This is my tweet check it out http://example.com/blah"

url = find_url(myString)
if url:
    print("Bulunan URL:", url)
else:
    print("URL bulunamadı")
