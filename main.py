import time
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

YESIL = "#00FF00"
KIRMIZI = "#FF0000"
SARI = "#FFFF00"
MAVI = "#00FFFF"
MOR = "#FF00FF"
BEYAZ = "#FFFFFF"

HAYALETLER = ["Poltergeist", "Banshee", "Demon", "Gulyabani", "Golge Ruh", "Cin Unsuru", "Ruhsal Varlik"]
MEKANLAR = ["Mutfak", "Tam Arkan", "Tavan", "Kapi Esigi", "Yatagin Alti", "Dolabin Ici", "Koridorun Sonu"]

PARANORMAL_UYARILAR = [
    "UYARI: ELEKTROMANYETIK ALAN FREKANSI DELIRDI!",
    "CIHAZ SENSORLERI ANLIK OLARAK SIFIRLANDI!",
    "DIKKAT: ODADAKI SICAKLIK HIZLA DUSUYOR!",
    "KRITIK SEVIYE: CEVREDE YUKSEK ENERJI SIKISMASI VAR!",
    "DEDEKTOR SES DALGASI ANALIZI FAIL_04",
    "SARI ALARM: ISIK SPEKTRUMUNDA GOLGE ALGILANDI!",
    "SISTEM UYARISI: PARANORMAL SIZMA ENERJISI YUKSEK!"
]

SALLANTI_SOZLUK = [
    ("Yaklasti...", MAVI),
    ("Umursamiyorsun...", SARI),
    ("Gormezden Geliyorsun...", MOR),
    ("Kavusuyorsun...", MOR),
    ("DIBINDE!!!", KIRMIZI),
    ("SINYAL KIRILIYOR ERROR_0x000", KIRMIZI)
]

class GhostDetectorApp(App):
    def build(self):
        self.title = "MEK-OS : Ghost Detector"
        self.sallanti_asama = 0
        self.baslangictan_beri_gecen = 0

        self.ana_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.baslik = Label(text="MEK-OS : Ghost Detector", font_size='24sp', color=get_color_from_hex(YESIL), size_hint_y=0.1)
        self.ana_layout.add_widget(self.baslik)

        self.sozluk_layout = BoxLayout(orientation='vertical', size_hint_y=0.4, padding=10)
        self.sozluk_label_listesi = []
        
        for i in range(len(SALLANTI_SOZLUK)):
            lbl = Label(text=" -> ?", font_size='16sp', color=get_color_from_hex(YESIL))
            self.sozluk_layout.add_widget(lbl)
            self.sozluk_label_listesi.append(lbl)
        self.ana_layout.add_widget(self.sozluk_layout)

        self.durum_label = Label(text="[*] Radar Aktif. Taraniyor...", font_size='18sp', color=get_color_from_hex(BEYAZ), size_hint_y=0.3, halign='center')
        self.ana_layout.add_widget(self.durum_label)

        self.buton = Button(text="ETRAFI TARA", font_size='20sp', size_hint_y=0.2, background_color=get_color_from_hex(YESIL), color=get_color_from_hex("#000000"))
        self.buton.bind(on_press=self.tara)
        self.ana_layout.add_widget(self.buton)

        Clock.schedule_interval(self.zamanlayici_guncelle, 1)

        return self.ana_layout

    def tara(self, instance):
        emf = round(random.uniform(0.1, 4.9), 2)
        sans = random.randint(1, 10)

        if emf > 3.5 or sans > 6:
            ruh = random.choice(HAYALETLER)
            yer = random.choice(MEKANLAR)
            uyari = random.choice(PARANORMAL_UYARILAR)
            yuksek_emf = round(random.uniform(5.0, 10.0), 2)

            metin = (f"[UYARI] YUKSEK AKTIVITE!\n\n"
                     f"[*] EMF Alani: {yuksek_emf} uT\n"
                     f"[!] Tespit Edilen: {ruh}\n"
                     f"[!] Konum: {yer}!!\n\n"
                     f"[DURUM]: {uyari}")
            self.durum_label.text = metin
            self.durum_label.color = get_color_from_hex(KIRMIZI)
        else:
            self.durum_label.text = f"[*] EMF Alani: {emf} uT\n[+] Durum: Sakin... Her sey stabil."
            self.durum_label.color = get_color_from_hex(YESIL)

    def zamanlayici_guncelle(self, dt):
        self.baslangictan_beri_gecen += 1
        
        if self.baslangictan_beri_gecen >= 600:
            self.baslangictan_beri_gecen = 0
            
            if self.sallanti_asama < len(SALLANTI_SOZLUK):
                kelime, renk = SALLANTI_SOZLUK[self.sallanti_asama]
                
                self.sozluk_label_listesi[self.sallanti_asama].text = f" -> {kelime}"
                self.sozluk_label_listesi[self.sallanti_asama].color = get_color_from_hex(renk)
                
                self.durum_label.text = f"[UYARI] CIHAZ SALLANTI ALGILADI!\n\n>>> {kelime} <<<"
                self.durum_label.color = get_color_from_hex(renk)
                
                self.sallanti_asama += 1
            else:
                self.sallanti_asama = 0
                for lbl in self.sozluk_label_listesi:
                    lbl.text = " -> ?"
                    lbl.color = get_color_from_hex(YESIL)
                self.durum_label.text = ">>> RESTART: RE-SCANNING SALS <<<"
                self.durum_label.color = get_color_from_hex(SARI)

if __name__ == "__main__":
    GhostDetectorApp().run()