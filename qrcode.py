
# qr code
import pyqrcode
url=input("Please enter the web URL:")
qr=pyqrcode.create(url)
qr.svg("qrcode.svg",scale= 8)