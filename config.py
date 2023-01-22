import os
from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("27589257"))
API_HASH = getenv("0af78b04b48361bc117fa4e06d6d2292")
BOT_TOKEN = getenv("1739231223:AAGBcJ3vgHOW_0vvVnoYB61zNgz9hx9vWn0")
SESSION_NAME = getenv("SESSION_NAME", "BQBWyDVGYIFakF-R0UBhvhfd3cIHP6DuhsacsgrZXtcW6-BLyJTJWYLDOrZeJ2_dkZiwYOg0Q-I4O6K3A-EskeePXqI6xRIICum8bojB_hBlbxlZ7jgqysG6tJiPUg_jymC4aULXN6uiZTjSOIwzFyZ52xzuRfrWVjY7v1uoHgEl9vb7GEDg631LphGHNHU0mnFhef4IwzdF7E4b27R9TcnAiKyMklS05d4eHjpMDJ1JgyMXK7DINUKQDSpWejQ0Am_Iy06ON8PlwDgsE-Y9AjehyvbafjtyFLYe-N-RxmQzxvMNTUsFSxk873T43uxeqAdS5asN8gvnbt1B0xTV0HL6AAAAAVqdMQcA")

# mandatory vars
OWNER_USERNAME = getenv("drxew")
ALIVE_NAME = getenv("umban")
BOT_USERNAME = getenv("amiciarobot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Official-Afk-xD/BLAZE-MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Team_Bot_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Team_Bot_Update")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
