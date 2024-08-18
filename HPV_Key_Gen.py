from os import system as sys
from platform import system as s_name
from colorama import Fore
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

from Core.Tools.Generation.HPV_My_Clone_Army import _HPV_My_Clone_Army
from Core.Tools.Generation.HPV_Chain_Cube_2048 import _HPV_Chain_Cube_2048
from Core.Tools.Generation.HPV_Train_Miner import _HPV_Train_Miner
from Core.Tools.Generation.HPV_Bike_Ride_3D import _HPV_Bike_Ride_3D
from Core.Tools.Generation.HPV_Twerk_Race import _HPV_Twerk_Race
from Core.Tools.Generation.HPV_Merge_Away import _HPV_Merge_Away

from Core.Tools.HPV_Proxy import HPV_Proxy_Checker
from Core.Tools.HPV_Banner import HPV_Banner







if __name__ == '__main__':

    sys('cls' if s_name() == 'Windows' else 'clear') # Очистка терминала
    HPV_Banner()
    Console_Lock = Lock()
    Proxy = HPV_Proxy_Checker()
    Retry = 1 if len(Proxy) == 0 else len(Proxy) if len(Proxy) > 0 and len(Proxy) <= 50 else 50

    try:
        Amount = int(input(Fore.MAGENTA + '\n[SANTIZ ИИИУУУ]' + Fore.GREEN + f' - Введи количество ключей писят два (не более {Retry}): '))
        KEY_COUNT = Amount if Amount <= Retry else Retry
        print('\n')
    except:
        print(Fore.MAGENTA + '[SANTIZ ИИИУУУ]' + Fore.GREEN + ' — Введено некорректное значение!')
        exit()

    Games = [_HPV_Twerk_Race, _HPV_Merge_Away, _HPV_My_Clone_Army, _HPV_Chain_Cube_2048, _HPV_Train_Miner, _HPV_Bike_Ride_3D]

    HPV_Keys = []
    with ThreadPoolExecutor() as HPV:
        Futures = [HPV.submit(Game, Console_Lock, KEY_COUNT, Proxy) for Game in Games]
        for Future in Futures:
            Keys, Status = Future.result()
            HPV_Keys.append(Keys) if Status else None

    if HPV_Keys:
        with open('[SANTIZ ИИИУУУ] Keys.txt', 'w', encoding='utf-8') as HPV_TEAM:
            for KEYS in HPV_Keys:
                for Game, Keys in KEYS.items():
                    print(Fore.MAGENTA + '\n[SANTIZ ИИИУУУ]' + Fore.GREEN + f' — бери ключ писят два `{Game}`:')
                    HPV_TEAM.write(f'\n[SANTIZ ИИИУУУ]  — Ваши ключи для {Game}:\n')
                    for Key in Keys:
                        print(Fore.MAGENTA + '[SANTIZ ИИИУУУ]' + Fore.GREEN + ' — `' + Fore.WHITE + Key + Fore.GREEN + '` ///' + Fore.MAGENTA + ' t.me/santiz52cr')
                        HPV_TEAM.write(f'   `{Key}` /// @santiz52cr\n')
    else:
        print(Fore.MAGENTA + '\n[SANTIZ ИИИУУУ]' + Fore.RED + ' НЕ ПОЛУЧИЛОСЬ, ДУРАК БЛЕН')


