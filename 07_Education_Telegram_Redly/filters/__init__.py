from aiogram import Dispatcher

from .private_chat import IsPrivate

# Add filter attribute to Dispatcher
def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)