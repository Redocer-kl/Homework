from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from telethon.tl.types import ReplyKeyboardMarkup

API_TOKEN = ""
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
    kb_start.add(info, calc)
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb_start)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup = kb)

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
