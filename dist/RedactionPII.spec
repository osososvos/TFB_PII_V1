# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from PyInstaller.utils.hooks import collect_all

sys.path.append(os.path.abspath('.'))

# Collect spacy and en_core_web_md
spacy_datas, spacy_binaries, spacy_hiddenimports = collect_all('spacy')
en_core_web_md_datas, en_core_web_md_binaries, en_core_web_md_hiddenimports = collect_all('en_core_web_md')

# Add pkg_resources to hidden imports
pkg_resources_hiddenimports = ['pkg_resources.py2_warn', 'pkg_resources.markers']

block_cipher = None

a = Analysis(['main.py'],
             pathex=[],
             binaries=spacy_binaries + en_core_web_md_binaries,
             datas=spacy_datas + en_core_web_md_datas,
             hiddenimports=['docx'] + spacy_hiddenimports + en_core_web_md_hiddenimports + pkg_resources_hiddenimports,
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='RedactionPII',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,  # Changed to True for debugging
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='app_icon.ico')