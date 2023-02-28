from distutils.command.config import config
from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','21199736'))
    API_HASH = getenv('API_HASH','3ed76d05d92a5203ca076066146a47bc')
    BOT_TOKEN = getenv('BOT_TOKEN','123456789:AAF8-1234-1234-1234-1234567890AB')

config = Config()
