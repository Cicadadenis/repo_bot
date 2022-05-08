
from PIL import Image,  ImageDraw, ImageFont
import secrets
from aiogram import types, Bot, Dispatcher
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
import random, time
from aiogram.dispatcher.filters import ChatTypeFilter
from datetime import datetime, timedelta
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from klava import  klv
import webbrowser

class cicada(StatesGroup):
    sms = State()
    size = State()
    jaloba = State()
    ppp = State()
    tex = State()
    delit = State()

adm = []
with open("admins.txt", "r") as f:
    adm_add = f.readlines()
    for x in adm_add:
        adm.append(x)
#1144785510






token = "5352078889:AAHJFCUQvo1DvDviWozx3-F-OzJQZg9najE"
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text='adm', state='*')
async def adm(message: types.Message, state: FSMContext):
    chat_id = int(message.chat.id)
    imya = message.chat.first_name
    await message.answer("<b>Введи Пароль Администратора:   </b>")
    await cicada.ppp.set()


@dp.message_handler(state=cicada.ppp)
async def adm_pass(message: Message, state):
    imya = message.chat.first_name
    xx = message.text
    await state.finish()
    if xx == 'xxx':
        await message.answer(f"Добро пожаловать \n{imya}", reply_markup=klv)
    else:
        await message.answer("<b>В Доступе Отказано!</b>")

@dp.callback_query_handler(text='/cicada', state='*')
async def otcet(call: CallbackQuery, state: FSMContext):
    ch = call.message.chat.id
    webbrowser.open("otchet.html", new=2)
    time.sleep(3)
    with open(f"otchet.html", "rb") as doc:
       await bot.send_document(ch, doc)


ps = []
@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    ps.clear()
    chat_id = message.chat.id
    imya = message.chat.first_name
    password = secrets.token_urlsafe(3)
    ps.append(password)
    im = Image.open('dropbox-logo@2x.jpg')
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype('Carnivale.ttf', size=170)
    draw_text.text(
        (220,120),
        password,
        font=font,
        fill=('green'),
        colors='green'
        )
    im.save('new_pic.jpg')
    pp = open("new_pic.jpg", 'rb').read()
    text = (f"<b>Введите код с картинки 👆</b>\n"
           f" ➖➖➖➖➖➖➖➖➖\n"
           f"<b>Чтобы вернуться в меню и начать</b>\n"
           f"<b>Oтправьте 👉 /start</b>")
    await bot.send_photo(chat_id, photo=pp, caption=text)
    await cicada.sms.set()

@dp.message_handler(state=cicada.sms)
async def bot2(message: Message, state):

    chat_id = message.chat.id
    imya = message.chat.first_name
    pas = message.text
    if pas == ps[0]:
        ps.clear()
        await message.answer(f"<b>Привет ! {imya} \nОпишете суть вашего обращения</b>\n"
                             f"<b>И мы Отправим Ваше Обращение</b>\n"
                             f"<b>Первому свободному Оператору</b>\n"
                             f"<b>В течении 3-х минут С Вами Свяжеться Тех-Подержка</b>")
        await cicada.jaloba.set()
    else:
        ps.clear()
        await message.answer("<b>Неверно Введена Капча\nПопробуйте Снова</b>")
        await start_command(message, state="*")


@dp.message_handler(state=cicada.jaloba)
async def bot2(message: Message, state):
    fafa = message.chat.id
    imya = message.chat.first_name
    user = message.chat.username
    jb = message.text


    date_when_expires = datetime.now() 
    date_to_db = str(date_when_expires).split(".")[0]
    text = (
        f"<b>Зафиксированно обращение</b>\n"
        f"<b>В {date_to_db}</b>\n"
        f"<b>От пользователя:</b>\n"
        f"<b>{imya}</b>\n"
        f"<b>🆔 {fafa}</b>\n"
        f"<b>Юзик @{user}</b>\n"
        f"<b>Суть Обращения:</b>\n\n"
        f"<code>{jb}</code>"
    )
    text2 = (
        f"<b>Зафиксированно обращение</b><p>\n"
        f"<b>В {date_to_db}</b><p>\n"
        f"<b>От пользователя:</b><p>\n"
        f"<b>{imya}</b><p>\n"
        f"<b>🆔 {fafa}</b><p>\n"
        f"<b>Юзик @{user}</b><p>\n"
        f"<b>Суть Обращения:</b><p>\n\n"
        f"<code>{jb}</code><p>"
    )
    add_tex = open("tex.txt", "r").readlines()
    nn = random.choice(add_tex)
    oper_tex = nn.split("\n")[0]
    hth = f"Обращение отправленно Тех потдержке <p>{oper_tex}<p>\n\n{text2}\n\n\n"
    with open("otchet.html", "a", encoding="utf-8") as f:
        f.write(hth)
    
    await bot.send_message(chat_id=oper_tex, text=text)
    await message.answer(f"<b>Тех Подержка Уведомлена Об вашем Обращени</b>\n"
                         f"<b>{imya} Вам Ответят В Ближайшее Время </b>")
    await state.finish()
ff = []
     
@dp.callback_query_handler(text="list_tex", state="*")
async def list_tex(call: CallbackQuery, state: FSMContext):
    add_tex = open("tex.txt", "r").readlines()

    for x in add_tex:
        ff.append(x.split("\n")[0])
    s = "\n".join(ff)
    await call.message.answer(f"<b>Введи ID Пользователя которого нужно удалить</b>\n"
                              f"<code>{s}</code>")
    await cicada.delit.set()

def rm(d):
    add_tex = open("tex.txt", "r").readlines()
    ff.clear()
    for x in add_tex:
        ff.append(x.split("\n")[0])
    ff.remove(d)
    with open("tex.txt", "w") as r:
        for x in ff:
            r.write(f"{x}\n")

@dp.message_handler(state=cicada.delit)
async def delit(message: Message, state):
    d = message.text
    rm(d)
    add_tex = open("tex.txt", "r").readlines()
    ff.clear()
    for x in add_tex:
        ff.append(x.split("\n")[0])
    s = "\n".join(ff)
    await message.answer(f"<b>Текуший Список ID Пользователей</b>\n"
                              f"<code>{s}</code>")
    await state.finish()

@dp.callback_query_handler(text="add_tex", state="*")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    await call.message.answer("<b>Введи ID Пользователя для Добавления Его В Тех Подержку</b>")
    await cicada.tex.set()

@dp.message_handler(state=cicada.tex)
async def tex(message: Message, state):
    tex_add = message.text
    with open("tex.txt", "a") as f:
        f.write(f"{tex_add}\n")
    add_tex = open("tex.txt", "r").readlines()
    ff.clear()
    for x in add_tex:
        ff.append(x.split("\n")[0])
    s = "\n".join(ff)
    await message.answer(f"<b>Текуший Список ID Пользователей</b>\n"
                              f"<code>{s}</code>")
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp)