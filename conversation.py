
from aiogram import types
from aiogram.dispatcher import Dispatcher

user_data = {}

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start_handler(message: types.Message):
        user_id = message.from_user.id
        user_data[user_id] = {}
        await message.answer("Привет! Я помогу вам подобрать идеальный дом. Сначала уточним несколько деталей. В каком вы регионе и где находится ваш участок?")

    @dp.message_handler(lambda message: message.from_user.id in user_data)
    async def handle_messages(message: types.Message):
        user_id = message.from_user.id
        state = user_data.get(user_id, {})
        if 'region' not in state:
            state['region'] = message.text
            await message.answer("Какая степень готовности дома вас интересует на данном этапе? (Например: только сруб, под усадку, под ключ)")
        elif 'readiness' not in state:
            state['readiness'] = message.text
            await message.answer("Какой тип дома вы рассматриваете? (бревно, профилированный брус, клеёный брус, каркасный, ручной рубки, Post&Beam и т.д.)")
        elif 'type' not in state:
            state['type'] = message.text
            await message.answer("Какие коммуникации есть на участке? (свет, вода, газ). Можно ли разместить бригаду прямо на участке?")
        elif 'comms' not in state:
            state['comms'] = message.text
            summary = f"Клиент из региона: {state['region']}
Степень готовности: {state['readiness']}
Тип дома: {state['type']}
Коммуникации: {state['comms']}"
            await message.answer(f"Спасибо! Вот ваша заявка:

{summary}

Скоро с вами свяжется менеджер!")
