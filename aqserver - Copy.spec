# -*- mode: python -*-

block_cipher = None


a = Analysis(['aqserver.py'],
             pathex=['C:\\Users\\HZMMIC02\\Documents\\python\\Aqserver'],
             binaries=None,
             datas=[('snap7.dll', '.'),
					('aqserver.cfg', '.'),
					('aqserver.bat', '.'),
					('doc/_build/htmlhelp/aqserver.chm', '.'),
					('doc/_build/latex/aqserver.pdf', '.')
					],
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
