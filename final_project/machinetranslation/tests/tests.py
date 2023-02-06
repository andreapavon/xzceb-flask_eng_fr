import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def TestNull(self):
        self.assertEqual(frenchToEnglish(''),'')
        self.assertEqual(englishToFrench(''),'')

    def TestHello(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def TestYes(self):
        self.assertEqual(frenchToEnglish('Oui'),'Yes')
        self.assertEqual(englishToFrench('Yes'),'Oui')

unittest.main()