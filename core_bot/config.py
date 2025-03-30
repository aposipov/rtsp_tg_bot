from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
	BOT_TOKEN: str
	ADMIN_ID: list[int]
	CAM_1: str
	CAM_2: str
	CAM_3: str
	CAM_4: str

# settings = Settings(_env_file=".env")

