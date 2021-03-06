from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import set_volute, set_language
from loader import _

keybord_course = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text=_("๐ ะฏะทัะบ"),
                                                  callback_data="language"

                                              ),
                                              InlineKeyboardButton(
                                                  text=_("๐ ะััั"),
                                                  callback_data="course"

                                              ),

                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text=_("๐ต ะัะฑัะฐัั ะฒะฐะปััั"),
                                                  callback_data="volute"

                                              ),

                                          ]

                                      ]
                                      )

keybord_currency = InlineKeyboardMarkup(row_width=3,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="RUB",
                                                    callback_data=set_volute.new(text_name="set_volute", volute="RUB")

                                                ),
                                                InlineKeyboardButton(
                                                    text="USD",
                                                    callback_data=set_volute.new(text_name="set_volute", volute="USD")

                                                ),
                                                InlineKeyboardButton(
                                                    text="EUR",
                                                    callback_data=set_volute.new(text_name="set_volute", volute="EUR")

                                                ),

                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text=_("โฌ๏ธ ะะฐะทะฐะด"),
                                                    callback_data="backsettings"

                                                ),

                                            ]

                                        ]
                                        )

keybord_settings_back = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=_("โฌ๏ธ ะะฐะทะฐะด"),
                                                         callback_data="backsettings"

                                                     ),

                                                 ],

                                             ]
                                             )
keybord_language = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="๐ท๐บ",
                                                    callback_data=set_language.new(text_name="set_language",
                                                                                   language="ru")

                                                ),
                                                InlineKeyboardButton(
                                                    text="๐ฌ๐ง",
                                                    callback_data=set_language.new(text_name="set_language",
                                                                                   language="en")

                                                ),

                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text=_("โฌ๏ธ ะะฐะทะฐะด"),
                                                    callback_data="backsettings"

                                                ),

                                            ]

                                        ]
                                        )
