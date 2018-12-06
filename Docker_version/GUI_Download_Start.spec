# -*- mode: python -*-

block_cipher = None


a = Analysis(['GUI_Download_Start.py'],
             pathex=['./', './funcs_forload', '/loader'],
             binaries=[],
             datas=[('exit.png', '.'), ('hutro.png', '.')],
             hiddenimports=['funcs_forload.funcconvertvideo', 'tkinter'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='GUI_Download_Start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
