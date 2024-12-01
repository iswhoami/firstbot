from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

import config


class IsAdmin(BaseFilter):
    async def __call__(self, obj: TelegramObject) -> bool:
        return obj.from_user.id in config.admins