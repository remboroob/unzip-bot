# Copyright (c) 2022 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("16092439"))
    API_HASH = os.environ.get("2583b8bdc2ff7e6d4acca21ae33411cd")
    BOT_TOKEN = os.environ.get("5732579204:AAH0nB0d4z63RRZWCpyrvdS2m4xCdd76UIM")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL"))
    MONGODB_URL = os.environ.get("MONGODB_URL")
    BOT_OWNER = int(os.environ.get("1993084922"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2040108421
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 6
