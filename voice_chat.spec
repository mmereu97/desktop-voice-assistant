# -*- mode: python ; coding: utf-8 -*-

# spec file pentru Advanced Voice Chat with Gemini

block_cipher = None

import os

# Modelul Silero VAD, descărcat automat de PyTorch la prima rulare a aplicației.
VAD_MODEL_PATH = os.path.join(os.path.expanduser('~'), '.cache', 'torch', 'hub', 'snakers4_silero-vad_master')

a = Analysis(
    ['voice_chat.py'],
    pathex=[],
    binaries=[],
    datas=[
        (VAD_MODEL_PATH, 'snakers4_silero-vad_master'), # Include modelul VAD
        ('prompts', 'prompts'),                        # Include folderul de prompturi
        ('icon.ico', '.')                              # Include iconița
    ],
    hiddenimports=[
        'sounddevice',
        'pyaudio', # Adăugat ca măsură de siguranță pentru speech_recognition
        'PySide6.QtSvg',
        'PySide6.QtNetwork'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ChatVocalGemini',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,         # --- SETARE IMPORTANTĂ: False pentru a ascunde consola ---
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'        # --- SETARE IMPORTANTĂ: Aici specificăm iconița ---
)