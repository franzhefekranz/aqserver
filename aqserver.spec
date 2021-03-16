# -*- mode: python -*-

block_cipher = None


a = Analysis(['aqserver.py'],
             pathex=['Z:\\G\\hzmmic02\\documents\\10_privat\\aqserver\\Aqserver'],
             binaries=[ ( 'snap7.dll', '.' ) ],
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='aqserver',
          debug=False,
          strip=False,
          upx=True,
          console=True )
