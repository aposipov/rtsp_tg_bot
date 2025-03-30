from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_cams = InlineKeyboardButton(text='камеры 🎥', callback_data='cameras')
start_menu = InlineKeyboardMarkup(inline_keyboard=[[btn_cams]])

cam_1 = InlineKeyboardButton(text='На Большой (ул. Куйбышева 36)', callback_data='cam_1')
cam_2 = InlineKeyboardButton(text='"И РЫБА И МЯСО" (Краснореченская 92/1)', callback_data='cam_2')
cam_3 = InlineKeyboardButton(text='ТЦ Норд (ул. Даниловского 6Б)', callback_data='cam_3')
cam_4 = InlineKeyboardButton(text='Реми Сити (ул. Краснореченская 213)', callback_data='cam_4')
cams_menu = InlineKeyboardMarkup(inline_keyboard=[[cam_1], [cam_2], [cam_3],
                                                  [cam_4]])

back_cams_btn = InlineKeyboardButton(text='назад ↩', callback_data='back_cams')
back_menu = InlineKeyboardMarkup(inline_keyboard=[[back_cams_btn]])

back_btn = InlineKeyboardButton(text='назад ↩', callback_data='cameras')
snap_btn = InlineKeyboardButton(text='снимок 📷', callback_data='snap')
gif_btn = InlineKeyboardButton(text='видео 🎥', callback_data='gif')
tools_menu = InlineKeyboardMarkup(inline_keyboard=[[snap_btn, gif_btn],
                                                   [back_btn]])
