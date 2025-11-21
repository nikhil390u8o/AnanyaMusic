# Copyright (c) 2025 Akash Daskhwanshi <ZoxxOP>
# Location: Mainpuri, Uttar Pradesh 
#
# All rights reserved.
#
# This code is the intellectual property of Akash Dakshwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: akp954834@gmail.com


import os
from os import getenv
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = "20898349"
API_HASH = getenv("API_HASH", "9fdb830d1e435b785f536247f49e7d87")
BOT_TOKEN = getenv("BOT_TOKEN", "7850782505:AAEqo9EqgfkrsZ8fUx8W9A5ayL2EcJUwDxU")
OWNER_ID = int(os.getenv("OWNER_ID", 7450385463))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "WTF_NoHope")
BOT_USERNAME = os.getenv("BOT_USERNAME", "RADHIKA_688U_MUSIC_BOT")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://gurjasharma3:B8osAJ8FeinFOjNV@cluster0pandababy.cwkui6e.mongodb.net/AviaxMusic?retryWrites=true&w=majority&tls=true")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1002564592666"))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/ZOXXOP/AnanyaMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/AnanyaBots")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/AnanyaBotSupport")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/akash_daksh1c")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/@akash_editz")
GITHUB = os.getenv("GITHUB", "https://github.com/akashprajapati9548")
DONATE = os.getenv("DONATE", "https://t.me/AnanyaBots/128")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION", "BQE-4i0ATEUTJrONIEvASz7hl-HPfSFLJkDK7DX2YsoLr1j_nkqqGxDGEsyeL-RlRmThTd2-E-F7475AkGhL1Fo6FTrwhKi0ySJ51ZKRpmsAj2vPYQ6b73jBTcGK21jpTC6O3o2CvA3tIRzVno_nhmV838DGkpvf06XjZtqZzabAC1cVETWLiCDoOG1zYsbqQWcqFzA-MNmXJdTQKvWEevaFdjWyZuaFlP0X9HW40qJCB1hxXZe5yjeEODiTMyQRCzpOs1ac1A-zQA56zRoYUFvGUVEq2LGsgXxQNbvQAGz5-rvgdBjDq-0_8s_dLqR7lnWDU-Rv71qjF2azR2dhsnpAtoVnHgAAAAHKarFXAA")
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Can be customized)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API_URL = os.getenv("API_URL", "https://api.thequickearn.xyz") #youtube song url
VIDEO_API_URL = os.getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")
API_KEY = os.getenv("30DxNexGenBots4d6508", None) # youtube song api key, generate free key or buy paid plan from panel.thequickearn.xyz

START_VIDEO_URL = os.getenv("START_VIDEO_URL", "https://files.catbox.moe/1tnq00.mp4")
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/hee6pf.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/hee6pf.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/hee6pf.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/hee6pf.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/hee6pf.jpg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & Bot State Stores
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏳ Time Conversion Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )


# ©️ Copyright Reserved - @ZoxxOP  Akash Dakshwanshi

# ===========================================
# ©️ 2025 Akash Dakshwanshi (aka @ZoxxOP)
# 🔗 GitHub : https://github.com/ZoxxOP/AnanyaMusic
# 📢 Telegram Channel : https://t.me/AnanyaBots
# ===========================================


# ❤️ Love From AnanyaBots
