import os
from os import environ, getenv
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = "8062010233:AAExAW3Z-kpT17OTUXg0GQkCVsc7qnDUbXQ"
    API_ID = 20288994
    API_HASH = "d702614912f1ad370a0d18786002adbf"
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 4294967296  # 4GB in bytes (4 * 1024 * 1024 * 1024)
    TG_MAX_FILE_SIZE = 4294967296  # 4GB in bytes
    FREE_USER_MAX_FILE_SIZE = 4294967296  # 4GB in bytes
    CHUNK_SIZE = 128
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
    HTTP_PROXY = ""
    
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = "@UploaderXNTBot"

    BANNED_USERS = set()

    DATABASE_URL = "mongodb+srv://moviedatabase:venura%408907@cluster0.hg0etvt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    LOG_CHANNEL = -1002897456594
    LOGGER = logging
    OWNER_ID = 8304706556
    SESSION_NAME = "UploaderXNTBot"
    UPDATES_CHANNEL = "-1003280087333"

    TG_MIN_FILE_SIZE = 4294967296  # 4GB in bytes
    BOT_USERNAME = "@Urluploader_z_bot"
    ADL_BOT_RQ = {}

    # Set False off else True
    TRUE_OR_FALSE = False

    # Shortlink settings
    SHORT_DOMAIN = "omegalinks.in"
    SHORT_API = "a7ac9b3012c67d7491414cf272d82593c75f6cbb"

    # Verification video link
    VERIFICATION = ""
