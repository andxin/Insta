import os, sys
if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			os.system("rm -f license.txt")
			sys.exit(" [!] berhasil menghapus api key")
		else:
			sys.exit(" [!] cara menggunakan : python run.py remove")
	try:
		__import__("insta.c").main()
	except Exception as e:
		exit(str(e))
