# -*- mode: python ; coding: utf-8 -*-
import sys
import os

block_cipher = None

datas = [
    ('icon.png', '.'),
    ('dist', 'dist')
]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on'
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
    name='MorgiFile',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.png' if sys.platform == 'win32' else None,
)

if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='MorgiFile.app',
        icon='icon.icns',
        bundle_identifier='com.morgifile.app',
        info_plist={
            'LSUIElement': True,
            'CFBundleShortVersionString': '2.0.0',
            'CFBundleVersion': '2.0.0',
        }
    )
