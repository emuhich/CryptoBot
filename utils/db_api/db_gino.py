from typing import List

from aiogram import Dispatcher
from gino import Gino
import sqlalchemy as sa
from sqlalchemy import Integer, Column, String, DateTime, BigInteger, sql

from data import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimeBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=db.func.now())
    updated_at = Column(DateTime(True), default=db.func.now(),
                        onupdate=db.func.now(),
                        server_default=db.func.now())


class User(TimeBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    chat_id = Column(BigInteger)
    btc = Column(String)
    eth = Column(String)
    qiwi = Column(String)
    sol = Column(String)
    language = Column(String)
    currency = Column(String)
    invited = Column(BigInteger)
    called = Column(BigInteger)

    query: sql.Select


async def on_startup(dispatcher: Dispatcher):
    print("Установка связи с PostgreSQL")
    await db.set_bind(config.POSTGRES_URL)
    print("Готово")
    print("Создаем таблицу")
    await db.gino.create_all()
    print("Готово")
