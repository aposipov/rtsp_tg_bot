from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import logging

from lexicon.lexicon import LEXICON, CAMERAS
from keyboards.kb import start_menu, cams_menu


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
	await message.answer(
		text=LEXICON['/start'],
		parse_mode="HTML",
		reply_markup=start_menu)


@router.callback_query(F.data == "cameras")
async def press_cams(callback: CallbackQuery, state: FSMContext):

	await callback.message.edit_text(
		text=LEXICON['cameras'],
		parse_mode="HTML",
		reply_markup=cams_menu)
	await state.clear()
