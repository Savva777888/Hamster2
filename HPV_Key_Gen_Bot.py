from telebot import TeleBot, types
from colorama import Fore
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

from Core.Tools.Generation.HPV_My_Clone_Army import _HPV_My_Clone_Army
from Core.Tools.Generation.HPV_Chain_Cube_2048 import _HPV_Chain_Cube_2048
from Core.Tools.Generation.HPV_Train_Miner import _HPV_Train_Miner
from Core.Tools.Generation.HPV_Bike_Ride_3D import _HPV_Bike_Ride_3D

from Core.Config.HPV_Config import TG_TOKEN
from Core.Tools.HPV_Proxy import HPV_Proxy_Checker
from Core.Tools.HPV_Banner import HPV_Banner




HPV = TeleBot(TG_TOKEN, parse_mode='HTML')



def HPV_Button(Key_Gen=True) -> types.InlineKeyboardMarkup:
    Button = types.InlineKeyboardMarkup()
    if Key_Gen:
        Button.add(types.InlineKeyboardButton('😶‍🌫️ Сгенерировать ключи 😶‍🌫️', callback_data='HPV_Key_Gen'))
    Button.add(types.InlineKeyboardButton('😎 Владелец: САНТИЗ НАХУ', url='https://t.me/santiz52cr'))

    return Button

def HPV_Text() -> str:
    return f'''👋🏻<b> Здарова мираславик и кириешка228</b>\n\n\n<b>МОЙ БОТ СУКА позволяет генерировать по 1 ключу для каждой игры за раз без ограничений нахуй</b>'''



######################## START #########################
@HPV.message_handler(commands=['start'])  
def HPV_START(info: types.Message):
    HPV_User = info.from_user.id # ID
    HPV.send_message(HPV_User, HPV_Text(), reply_markup=HPV_Button())
########################################################



################### ИНЛАЙН ОБРАБОТКА ###################
@HPV.callback_query_handler(func=lambda Call: True)
def HPV_INLINE(info: types.CallbackQuery):
    HPV_User = info.from_user.id # ID
    HPV_Message_ID = info.message.message_id # ID сообщения
    HPV_Command = info.data # Команда

    if HPV_Command == 'HPV_Key_Gen':
        HPV.answer_callback_query(info.id, '☑️ ЖДИ СУКА, идёт генерация...')
        HPV.edit_message_text('☑️ <b>ЖДИ СУКА, идёт генерация...</b>\n\n<blockquote><i>📌 В среднем генерация ключей занимает несколько минут, ЖДИ!</i></blockquote>', HPV_User, HPV_Message_ID, reply_markup=HPV_Button(False))

        Console_Lock = Lock()
        Proxy = HPV_Proxy_Checker()
        KEYS_TEXT = HPV_Text() + '\n'

        Games = [_HPV_My_Clone_Army, _HPV_Chain_Cube_2048, _HPV_Train_Miner, _HPV_Bike_Ride_3D]

        HPV_Keys = []
        with ThreadPoolExecutor() as _HPV:
            Futures = [_HPV.submit(Game, Console_Lock, 1, Proxy) for Game in Games]
            for Future in Futures:
                Keys, Status = Future.result()
                HPV_Keys.append(Keys) if Status else None

        if HPV_Keys:
            for KEYS in HPV_Keys:
                for Game, Keys in KEYS.items():
                    print(Fore.MAGENTA + '\n[SANTIZ ИИИУУУ]' + Fore.GREEN + f' — бери ключ писят два `{Game}`:\n')
                    KEYS_TEXT += f'\n✅ <b>Ваши ключи для <i>{Game}</i>:</b>\n'
                    for Key in Keys:
                        print(Fore.MAGENTA + '[SANTIZ ИИИУУУ]' + Fore.GREEN + ' — `' + Fore.WHITE + Key + Fore.GREEN + '` ///' + Fore.MAGENTA + ' t.me/santiz52cr')
                        KEYS_TEXT += f'<b>—</b> <code>{Key}</code>\n'
        else:
            KEYS_TEXT += '\n❌ <b>Не получилось ёпта. повтори позже!</b>'

        HPV.edit_message_text(KEYS_TEXT, HPV_User, HPV_Message_ID, reply_markup=HPV_Button())
########################################################



if __name__ == '__main__':
    while True:
        try:
            HPV_Banner()
            HPV.polling(none_stop=True) # Запуск бота
        except:
            continue