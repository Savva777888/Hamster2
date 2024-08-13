from requests import post
from time import sleep, time
from random import randint
from uuid import uuid4
from colorama import Fore
from threading import Lock, Thread
from typing import Literal
from datetime import datetime
from itertools import cycle







class HPV_Chain_Cube_2048:
    '''
    Генерация ключей для игры Chain Cube 2048 в Hamster Kombat
    ----------------------------------------------------------
    [1] - `Генерация уникального ID`
    
    [2] - `Аутентификация для получения токена`
    
    [3] - `Эмуляция человека`
    
    [4] - `Получение ключа`
    '''



    def __init__(self, Console_Lock: Lock, _Thread: int, Proxy: dict = None) -> None:
        self.APP_TOKEN = 'd1690a07-3780-4068-810f-9b5bbf2931b2'
        self.PROMO_ID = 'b4170868-cef0-424f-8eb9-be0622e8e8e3'
        self.Console_Lock = Console_Lock

        self.THREAD = f'Поток №{_Thread}' # Нумерация потока
        self.PROXY = Proxy # Прокси (при наличии)
        self.ID = self.HPV_ID() # Генерация уникального ID
        self.TOKEN = self.HPV_Login() # Получение токена по ID



    def Current_Time(self) -> str:
        '''Текущее время'''

        return Fore.BLUE + f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'



    def Logging(self, Type: Literal['Success', 'Warning', 'Error'], Smile: str, Text: str) -> None:
        '''Логирование'''

        with self.Console_Lock:
            COLOR = Fore.GREEN if Type == 'Success' else Fore.YELLOW if Type == 'Warning' else Fore.RED # Цвет текста
            DIVIDER = Fore.BLACK + ' | '   # Разделитель

            Time = self.Current_Time()             # Текущее время
            _Thread = Fore.MAGENTA + self.THREAD   # Нумерация потока
            Smile = COLOR + str(Smile)             # Смайлик
            Text = COLOR + Text                    # Текст лога

            print(Time + DIVIDER + Smile + DIVIDER + _Thread + DIVIDER + Text)



    def HPV_ID(self) -> str:
        '''Генерация уникального ID'''

        return f'{int(time() * 1000)}-{"".join(str(randint(0, 9)) for _ in range(19))}'



    def HPV_Login(self) -> str:
        '''Аутентификация для получения токена'''

        URL = 'https://api.gamepromo.io/promo/login-client'
        JSON = {'appToken': self.APP_TOKEN, 'clientId': self.ID, 'clientOrigin': 'deviceid'}

        try:
            return post(URL, json=JSON, proxies=self.PROXY).json()['clientToken']
        except:
            return ''



    def HPV_Emulation(self) -> bool:
        '''Эмуляция человека'''

        URL = 'https://api.gamepromo.io/promo/register-event'
        HEADERS = {'Authorization': f'Bearer {self.TOKEN}', 'Content-Type': 'application/json'}
        JSON = {'promoId': self.PROMO_ID, 'eventId': str(uuid4()), 'eventOrigin': 'undefined'}

        try:
            sleep(25)
            return post(URL, json=JSON, headers=HEADERS, proxies=self.PROXY).json()['hasCode']
        except:
            return False



    def HPV_Generate_Key(self) -> str:
        '''Получение ключа'''

        URL = 'https://api.gamepromo.io/promo/create-code'
        HEADERS = {'Authorization': f'Bearer {self.TOKEN}', 'Content-Type': 'application/json'}
        JSON = {'promoId': self.PROMO_ID}

        try:
            return post(URL, json=JSON, headers=HEADERS, proxies=self.PROXY).json()['promoCode']
        except:
            return ''



    def Run(self) -> str:
        '''Автоматическое получение ключа'''

        if self.TOKEN: # Если токен получен
            self.Logging('Success', '🟢', 'Аутентификация успешна!')

            # Эмуляция человека
            for _ in range(15):
                if self.HPV_Emulation():
                    self.Logging('Success', '🟢', 'Ключ готов!')
                    break
                else:
                    self.Logging('Warning', '🟡', 'Ключи ещё не готов!')

            # Получение токена
            KEY = self.HPV_Generate_Key()
            if self.HPV_Generate_Key():
                self.Logging('Success', '🟣', 'Ключ успешно получен!')
            return KEY
        else: # Если токен не получен
            self.Logging('Error', '🔴', 'Аутентификация не успешна!')
            return None







def _HPV_Chain_Cube_2048(Console_Lock, Retry, Proxy) -> dict:
    '''Генерация ключей для игры Chain Cube 2048'''

    HPV_Keys = [] # Список хранящий ключи для Chain Cube 2048
    Threads = [] # Список потоков

    def HPV_Key_Gen(_Thread, Proxy=None):
        HPV = HPV_Chain_Cube_2048(Console_Lock, f'{_Thread} Cube', Proxy)
        KEY = HPV.Run()
        HPV_Keys.append(KEY) if KEY else None

    for retry in range(Retry):
        if Proxy:
            Proxy = cycle(Proxy)
            TH = Thread(target=HPV_Key_Gen, args=(retry, next(Proxy)))
        else:
            TH = Thread(target=HPV_Key_Gen, args=(retry,))
        TH.start()
        Threads.append(TH)

    for thread in Threads:
        thread.join()

    return {'Chain Cube 2048': HPV_Keys}, True if HPV_Keys else False