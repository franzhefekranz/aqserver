pyinstaller -F aqserver.spec
mkdir dist\de\
mkdir dist\en\
copy snap7.dll dist\
copy aqserver.cfg dist\
copy aqserver.bat dist\
copy doc\de\_build\latex\aqserver.pdf dist\de\
copy doc\de\_build\htmlhelp\aqserver.chm dist\de\
copy doc\en\_build\latex\aqserver.pdf dist\en\
copy doc\en\_build\htmlhelp\aqserver.chm dist\en\
