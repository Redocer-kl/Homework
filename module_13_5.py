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

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info = types.KeyboardButton("Информация")
    calc = types.KeyboardButton("Рассчитать")
    kb.add(info, calc)
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text = "Рассчитать")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст")
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
