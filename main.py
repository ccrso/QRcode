import sys
import qrcode   # ставим 6.1 - на последней версии почему-то не работает(???)

if len(sys.argv) > 1:
    data = sys.argv[1]
else:
    data = input('Enter data: ')

img = qrcode.make(data)
img.show(data)
