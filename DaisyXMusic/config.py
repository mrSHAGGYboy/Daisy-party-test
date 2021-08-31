# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("BQANXNVDDh3hW_G31Z6C0_SjYZCa081-pUoob12_NoTuEWDoT3gNE_-L_CxOC29CEzSpk8jd_Dk-O2tf76ew1IfLvw-cuuO3Azb8TWP-rokxkeJ7HYZ94KIXHoFaYuR_6S5Yh3e_ho_WJyxwAlZtzppilyvM0pIblmgcsd01EXiG597v2ktuYHfADkUkOX6eIihN8tgqbUOyHSLghnel5dEeJXdZO1sYFJY6DiqkO3y_GjbTxCNuQQfaXwU1hubjp7_mHq8A3lJmv-y0uWknQu8YfRRh-JKcY6SloVDewIx2a_ya05H72eOqbAfgv8QyDzMSn16tmr0kR9eMNb_y7IcGRMcZRQA", "session")
BOT_TOKEN = getenv("1955724129:AAHn8D2Uu8-lu72onLEY44GNiPD_JfMoVu8")
BOT_NAME = getenv("Music player")
UPDATES_CHANNEL = getenv("1001116136659", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/915ee4ce67cf32e7787c3.jpg")
admins = {}
API_ID = int(getenv("6065291"))
API_HASH = getenv("dc7873c0a5c737af4356d4f245fe696d")
BOT_USERNAME = getenv("@Music_player_sl_meadia_tech_bot")
ASSISTANT_NAME = getenv("MR.SHAGGY [ °• SL MEDIA TECH ™ •° ]", "NA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DaisySupport_Official")
PROJECT_NAME = getenv("PROJECT_NAME", "DaisyXMusic v4")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamOfDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ITXYBL-RRSXCY-GPFIQC-KEPKZC-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
PMMSG = getenv("PMMSG", f"Hi there, This is a music assistant service of @{BOT_USERNAME}.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don t add this user to secret groups.\n   - Don t Share private info here\n\n")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
