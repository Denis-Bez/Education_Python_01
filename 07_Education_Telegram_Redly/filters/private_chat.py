from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

# Create castom filter to handler (message)
class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE # Check type of chat

# Filter for callback button in an inline keyboard
# class IsPrivate_Query(BoundFilter):
#     async def check(self, call: types.CallbackQuery):
#         return call.message.chat.type == types.ChatType.PRIVATE