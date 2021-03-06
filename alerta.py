# 1° importar as bibliotecas necessárias
from datetime import datetime
import PySimpleGUI
import pywhatkit
import keyboard
import time

# 2° saber em que dia da semana esta
class Alerta:
    def __init__(self):
        self.dia_da_semana = datetime.now().strftime("%A").lower()
        self.semana = self.dia_da_semana
        self.contatos = ['+5521964956804', '+5521991818284', '+5521972841620', '+5521987747103', '+5521985336340']
        self.mensagem = self.dia_da_semana
# 3° relacionar o dia da semana com um anime
        if self.dia_da_semana == 'monday':
            self.dia_da_semana = '''
● Uma Musume: Pretty Derby (2ª Temporada)
● Wave Surfing Yappe!
● Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi
● Mushoku Tensei: Isekai Ittara Honki Dasu
● EX-ARM
● Maoujou de Oyasumi
● Ura Sekai Picnic
● Non Non Biyori (3ª Temporada)
● Alice in Deadly School
● Ochikobore Fruit Tart'''
            self.Iniciar()
        elif self.dia_da_semana == 'tuesday':
            self.dia_da_semana = '''
● Gekidol
● Shin Chuuka Ichiban! (2ª Temporada)
● Tensei Shitara Slime Datta Ken (2ª Temporada)
● Beastars (2ª Temporada)
● Maesetsu!
● Magatsu Wahrheit: Zuerst
● Black Clover'''
            self.Iniciar()

        elif self.dia_da_semana == 'wednesday':
            self.dia_da_semana = '''
● Hortensia Saga
● Soukou Musume Senki
● Log Horizon: Entaku Houkai (3ª Temporada)
● Kaifuku Jutsushi no Yarinaoshi
● Wonder Egg Priority
● Nanatsu no Taizai: Fundo no Shinpan
● Re:Zero kara Hajimeru Isekai Seikatsu ( 2ª Temporada – Parte 2)'''
            self.Iniciar()
        
        elif self.dia_da_semana == 'thursday':
            self.dia_da_semana = '''
● Go-toubun no Hanayome ∬
● Yuru Camp△ (2ª Temporada)
● Tenchi Souzou Design-bu
● 2.43: Seiin Koukou Danshi Volley-bu
● Yakusoku no Neverland – The Promised Neverland (2ª Temporada)
● Dr. Stone: Stone Wars (2ª Temporada)
'''
            self.Iniciar()

        elif self.dia_da_semana == 'friday':
            self.dia_da_semana = '''
● Kumo desu ga, Nani ka?
● Ore dake Haireru Kakushi Dungeon: Kossori Kitaete Sekai Saikyou
● Jaku-Chara Tomozaki-kun
● Back Arrow
● WIXOSS Diva(A)Live
● Azur Lane: Bisoku Zenshin
● Otona no Bouguya-san (2ª Temporada)
● Jujutsu Kaisen
● Dragon Quest: Dai no Daibouken (2020)
● King’s Raid: Ishi wo Tsugumono-tachi)
'''
            self.Iniciar()

        elif self.dia_da_semana == 'saturday':
            self.dia_da_semana = '''
● Hataraku Saibou (2ª Temporada)
● Hataraku Saibou Black
● Horimiya
● SK∞
● Kai Byoui Ramune
● Hanyou no Yashahime: Sengoku Otogizoushi
● Digimon Adventure (2020)
● One Piece
'''
            self.Iniciar()

        elif self.dia_da_semana == 'sunday':
            self.dia_da_semana = '''
● Shingeki no Kyojin Final Season
● Kemono Jihen
● Pokemon (2019)
● Boruto: Naruto Next Generations
        
'''
            self.Iniciar()
# 4° Enviar a mensagem no wpp para os contatos específicos

    def Iniciar(self):

        while len(self.contatos) >= 1:
            pywhatkit.sendwhatmsg(self.contatos[0], 
            f'Hoje tem: {self.dia_da_semana}', datetime.now().hour, datetime.now().minute + 1)
            del self.contatos[0]
            time.sleep(2)
            keyboard.press_and_release('alt + f4')

alerta = Alerta()
alerta.Iniciar()
