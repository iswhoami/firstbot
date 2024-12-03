import aiosqlite
from config import DB_PATH
from errors import DBQueryException


class Connection:

    async def init_connection(self, *args, **kwargs):
        self._conn = await aiosqlite.connect(DB_PATH)

    async def execute(self, sql, *args):
        try:
            async with self._conn.execute(sql, *args) as cursor:
                rows = await cursor.fetchall()
                if rows:
                    column_names = [description[0] for description in cursor.description]
                    result = [dict(zip(column_names, row)) for row in rows]
                    await self._conn.commit()
                    return result
                await self._conn.commit()
        except aiosqlite.Error as e:
            raise DBQueryException(str(e))

    async def execute_single_value(self, sql, *args):
        try:
            async with self._conn.execute(sql, *args) as cursor:
                result = await cursor.fetchone()
                if result is not None:
                    return result[0]
        except aiosqlite.Error as e:
            raise DBQueryException(str(e))

    async def execute_one_row(self, sql, *args):
        try:
            async with self._conn.execute(sql, *args) as cursor:
                rows = await cursor.fetchall()
                if rows:
                    column_names = [description[0] for description in cursor.description]
                    result = dict(zip(column_names, rows[0]))
                    await self._conn.commit()
                    return result
        except aiosqlite.Error as e:
            raise DBQueryException(str(e))

    async def execute_void(self, sql, *args):
        try:
            await self._conn.execute(sql, *args)
            await self._conn.commit()
        except aiosqlite.Error as e:
            raise DBQueryException(str(e))

    async def close(self):
        if hasattr(self, '_conn'):
            await self._conn.close()
            del self._conn
