import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luotu_kortin_saldo_oikein_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein_kun_rahat_riittaa(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 0.0)

    def test_saldo_ei_muutu_jos_rahat_ei_riita(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_metodi_palauttaa_true_jos_rahat_riittavat_ottoon(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)

    def test_metodi_palauttaa_false_jos_rahat_ei_riita_ottoon(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)
