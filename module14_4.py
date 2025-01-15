from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from telethon.tl.types import ReplyKeyboardMarkup
import crud_functions


API_TOKEN = "8065000752:AAGhRz8GgcNHLbWqsW_QwwqIhtYKjGZc9l8"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

kb = types.InlineKeyboardMarkup(resize_keyboard=True)

b1 = types.InlineKeyboardButton("Рассчитать норму калорий", callback_data="calc")
b2 = types.InlineKeyboardButton("Формулы расчета", callback_data="formula")

kb.add(b1, b2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info = types.KeyboardButton("Информация")
    calc = types.KeyboardButton("Рассчитать")
    buy = types.KeyboardButton("Купить")
    kb_start.add(info, calc, buy)
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb_start)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup = kb)

@dp.message_handler(text = "Купить")
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for product in products:
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        with open("image.jpg", 'rb') as photo:
            await bot.send_photo(message.chat.id, photo)

    kb_buy = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
    buy1 = types.InlineKeyboardButton("Продукт 1", callback_data="product_buying")
    buy2 = types.InlineKeyboardButton("Продукт 2", callback_data="product_buying")
    buy3 = types.InlineKeyboardButton("Продукт 3", callback_data="product_buying")
    buy4 = types.InlineKeyboardButton("Продукт 4", callback_data="product_buying")
    kb_buy.add(buy1, buy2, buy3, buy4)

    await message.answer("Выберите продукт для покупки", reply_markup=kb_buy)

@dp.callback_query_handler(text = 'product_buying')
async def buy(call):
    await call.message.answer("Вы успешно купили товар!")


@dp.callback_query_handler(text = 'formula')
async def get_formula(call):
    await call.message.answer("Формула вычисления: 10 * вес + 6.25 * рост - 5 * возраст")

@dp.callback_query_handler(text = 'calc')
async def set_age(call):
    await call.message.answer("Введите вес")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async  def set_growth(message:types.Message, state):
    await state.update_data(age = int(message.text))
    await message.answer("Введите свой рост")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async  def set_weight(message:types.Message, state):
    await state.update_data(growth = int(message.text))
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    result = 10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"]
    await message.answer(f"Ваша норма калорий {result}")
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
