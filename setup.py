import os, sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext = Extension("insta", sources=["insta.c"])

setup(
	ext_modules=[ext],
	cmdclass={"build_ext": build_ext}
)

try:
	os.system("rm -rf build")
except:
	pass

sys.exit("\n [!] info : install berhasil silakan jalankan script dengan mengetik : \033[0;92mpython2 run.py\033[0;97m")
