from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.filters import Command
import logging

import os
from datetime import datetime
import ffmpeg
from ffmpeg import Error as FFmpegError

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import LEXICON, CAMERAS
from keyboards.kb import start_menu, cams_menu, tools_menu, back_menu
from config import Settings

router = Router()
settings = Settings(_env_file='.env')


@router.callback_query(F.data.startswith("cam_"))
async def get_camera(callback: CallbackQuery, state: FSMContext):
	camera = str(callback.data.split('_')[1])
	await state.update_data(cam=camera)
	await callback.message.edit_text(
		text=f"<b>{CAMERAS[camera]}</b>",
		parse_mode="HTML",
		reply_markup=tools_menu)


# @router.callback_query(F.data == "back")
# async def press_cams(callback: CallbackQuery, state: FSMContext):
# 	await callback.message.answer(
# 		text="Choose Camera:",
# 		parse_mode="HTML",
# 		reply_markup=cams_menu)
# 	await state.clear()


@router.callback_query(F.data == "back_cams")
async def press_cams(callback: CallbackQuery, state: FSMContext):
	# await callback.message.delete()
	await callback.message.delete()
	await callback.message.answer(
		text=LEXICON['cameras'],
		parse_mode="HTML",
		reply_markup=cams_menu)
	await state.clear()


@router.callback_query(F.data.startswith("snap"))
async def get_snap(callback: CallbackQuery, state: FSMContext):
	try:
		await callback.answer(text="Подготовка изображения ...")
		storage = await state.get_data()
		cam_rtsp = getattr(settings, f"CAM_{storage['cam']}", None)
		nowTime = datetime.now()
		caption = datetime.now().strftime('%H:%M:%S')
		nowOut = nowTime.strftime("snap-%d-%m-%Y-%H-%M-%S.jpg")
		(
			ffmpeg
			.input(cam_rtsp, rtsp_transport="tcp", vsync="2")
			.output(nowOut, vframes="1")
			.run(capture_stderr=True)
		)
		await callback.message.delete()
		await callback.message.answer_photo(FSInputFile(nowOut),
		                                caption=
		                                    f"<b>{CAMERAS[storage['cam']]}</b>\n"
		                                    "<b>фото сделано:</b> " + str(caption),
		                                    parse_mode="HTML",
		                                    reply_markup=back_menu)
		os.remove(nowOut)
	except FFmpegError as _ex:
		if "Connection refused" in _ex.stderr.decode('utf8'):
			await callback.message.reply(
				f"❌ Ошибка подключения к камере:\n\n<code>Connection refused</code>")
		elif "401" in _ex.stderr.decode('utf8'):
			await callback.message.reply(
				f"❌ Ошибка подключения к камере:\n\n<code>Неправильный логин или пароль</code>")


@router.callback_query(F.data.startswith("gif"))
async def get_gif(callback: CallbackQuery, state: FSMContext):
	try:
		await  callback.answer(text="Подготовка видео ...")
		storage = await state.get_data()
		cam_rtsp = getattr(settings, f"CAM_{storage['cam']}", None)
		nowTime = datetime.now()
		caption = datetime.now().strftime('%H:%M:%S')
		nowOut = nowTime.strftime("gif-%d-%m-%Y-%H-%M-%S.mp4")
		(
			ffmpeg
			.input(cam_rtsp, rtsp_transport="tcp", vsync="2")
			.output(nowOut, crf=40, pix_fmt='yuv420p', preset='ultrafast',
			        vcodec='copy', t=5)
			.run(capture_stderr=True)
		)
		await callback.message.delete()
		await callback.message.answer_video(FSInputFile(nowOut),
		                                caption=
		                                    f"<b>{CAMERAS[storage['cam']]}</b>\n"
		                                    "<b>видео сделано:</b> " + str(caption),
		                                    parse_mode="HTML",
		                                    reply_markup=back_menu)
		os.remove(nowOut)
	except FFmpegError as _ex:
		if "Connection refused" in _ex.stderr.decode('utf8'):
			await callback.message.reply(
				f"❌ Ошибка подключения к камере:\n\n<code>Connection refused</code>")
		elif "401" in _ex.stderr.decode('utf8'):
			await callback.message.reply(
				f"❌ Ошибка подключения к камере:\n\n<code>Неправильный логин или пароль</code>")
