"""Unde stau fișierele asistentului.

    <rădăcină>/
    ├── Project/   codul + prompturile implicite (GitHub)
    └── Data/      voice_chat_config.json, prompts/ (ale tale), .env, temp/,
                   logs/, screenshots/ (doar dacă e pornită salvarea pentru depanare)

Ca .exe, Data/ se creează lângă executabil. VOICECHAT_DATA_DIR mută datele oriunde.
"""
import os
import shutil
import sys

FROZEN = getattr(sys, "frozen", False)
CODE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
INSTALL_DIR = os.path.dirname(sys.executable) if FROZEN else os.path.dirname(CODE_DIR)
DATA_DIR = os.environ.get("VOICECHAT_DATA_DIR") or os.path.join(INSTALL_DIR, "Data")

CONFIG_FILE = os.path.join(DATA_DIR, "voice_chat_config.json")
ENV_FILE = os.path.join(DATA_DIR, ".env")
PROMPTS_DIR = os.path.join(DATA_DIR, "prompts")
TEMP_DIR = os.path.join(DATA_DIR, "temp")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
SCREENSHOTS_DIR = os.path.join(DATA_DIR, "screenshots")

# Capturile de ecran se trimit la Gemini din memorie. Pe disc se salvează DOAR pentru
# depanare, la cerere: VOICECHAT_SAVE_SCREENSHOTS=1.
SAVE_SCREENSHOTS = os.environ.get("VOICECHAT_SAVE_SCREENSHOTS") == "1"

for _d in (DATA_DIR, TEMP_DIR):
    os.makedirs(_d, exist_ok=True)

# La prima pornire, prompturile implicite din cod devin prompturile tale (editabile).
if not os.path.isdir(PROMPTS_DIR):
    shutil.copytree(os.path.join(CODE_DIR, "prompts"), PROMPTS_DIR)
