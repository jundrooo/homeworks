import unittest
from modul import katta_sonni_top, textCapitalize, juft_son_top, fibo



class Check1:
    def tekshir(self):
        assert katta_sonni_top([1,23,5,6]) == 23 
        assert katta_sonni_top([12,43,12,23]) == 43

    def tekshir2(self):
        assert textCapitalize("hello world") == "Hello world"
        assert textCapitalize('salom py') == 'Salom py'

    def tekshir3(self):
        assert juft_son_top([12,43,3,5]) == 12
        assert juft_son_top([55,44,22,31]) == 44,22

    def tekshir3(self):
        class check2:
            def tekshir_true(self):
                assert fibo(8) == True
                assert fibo(2) == True
                assert fibo(1) == True
            def tekshir_False(self):
                assert fibo(10) == False
                assert fibo(11) == False


unittest.main()
