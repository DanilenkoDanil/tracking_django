from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from base.models import Setting, SignalResult, Signal
from django.core.management.base import BaseCommand

import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

setting = Setting.objects.get(id=1)
bot = Bot(token=setting.channel_for_bot)
dp = Dispatcher(bot, storage=MemoryStorage())


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


@dp.message_handler(commands=['start'], state="*")
async def process_start_command(message: types.Message, state: FSMContext):
    await message.reply("Добро пожаловать!", parse_mode='Markdown')


@dp.message_handler(commands=['help'], state="*")
async def process_start_command(message: types.Message, state: FSMContext):
    await message.reply(f"Формат сообщения - /calculate balance leverage time source", parse_mode='Markdown')


@dp.message_handler(commands=['calculate'], state="*")
async def process_start_command(message: types.Message, state: FSMContext):
    command_list = message.text.split()
    balance = float(command_list[1])
    leverage = float(command_list[2])
    time = command_list[3]
    if len(command_list) >= 5:
        source = command_list[4]
    else:
        source = None
    if source is not None:
        signals = SignalResult.objects.filter(source=source)
    else:
        signals = SignalResult.objects.filter()
    for signal in signals:
        balance += ((0.25 * balance) * ((100 + (signal.price_change * leverage)) / 100) - 0.25 * balance)
    print(command_list)
    await message.reply(f"Balance - {round(balance, 2)}", parse_mode='Markdown')


class Command(BaseCommand):
    help = 'Переставка стоп лоссов'

    def handle(self, *args, **options):
        executor.start_polling(dp, on_shutdown=shutdown)
