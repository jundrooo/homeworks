import unittest
from modul import katta_sonni_top, textCapitalize, juft_son_top, fibo #unnitest hamda modul ni chqirib olamiz



class Check1:
    def tekshir(self):
        assert katta_sonni_top([1,23,5,6]) == 23  # assert medodi yordamida ushbu berilgan listdagi elementlarning orasidagi katta son 23 ga tengmi yo'qmi tekshiriladi
        assert katta_sonni_top([12,43,12,23]) == 43 # bu yerda ham huddi tepadakidek holat

    def tekshir2(self):
        assert textCapitalize("hello world") == "Hello world" # bu joyda ''hello world'' ushbu funksiya orqali ekranga chiqarilganda Birinchi harf katta ekanligi tekshiriladi
        assert textCapitalize('salom py') == 'Salom py' # ^

    def tekshir3(self):
        assert juft_son_top([12,43,3,5]) == 12 # bunda listdagi element faqat 12 juft ekanligi tekchiriladi
        assert juft_son_top([55,44,22,31]) == 44,22 # ^

    def tekshir3(self):
        class check2: # bu joyda funksiya ichida klass yaratib birinchi funksiyada True qiymatlar tekshiriladi ikkinchisida esa False qiymatlar
            def tekshir_true(self):
                assert fibo(8) == True # 8 fibonaci ro'yxatida bormi
                assert fibo(2) == True # ^
                assert fibo(1) == True # ^
            def tekshir_False(self):
                assert fibo(10) == False # 10 fibonaci ro'yxatida yo'qmi
                assert fibo(11) == False # ^
                assert fibo(12) == False # ^


unittest.main()
