import pyshorteners, sys, pyperclip

TOKEN = "85555c15223b53d4856f4875f92b4d38db33d049"

if len(sys.argv) > 1: url = sys.argv[-1]
else: url = pyperclip.paste()

url_shortener = pyshorteners.Shortener(api_key=TOKEN)

short_url = url_shortener.bitly.short(url)

print(short_url)
pyperclip.copy(short_url)
