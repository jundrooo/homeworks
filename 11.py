from datetime import datetime
def yosh_hisobla(tugilgan_sana):
    tugilgan_sana = datetime.strptime(tugilgan_sana, '%Y-%m-%d')
    hozirgi_sana = datetime.now()
    farq = hozirgi_sana - tugilgan_sana
    kunlar = farq.days
    yillar = kunlar // 365
    oy = (kunlar % 365) // 30
    kun = (kunlar % 365) % 30
    return f"Siz {yillar} yil, {oy} oy va {kun} kun yashadingiz."

# Foydalanish misoli:
print(yosh_hisobla('2009-01-09'))