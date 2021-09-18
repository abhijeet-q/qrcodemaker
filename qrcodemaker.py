import qrcode
import image

intro =''' HELLO !
WELCOME TO QRCODE MAKER'''

print(intro)
qr =input("ENTER ANYTHING YOU WANT TO CHANGE IN QR CODE\n")
saveit =input("WHICH NAME YOU WANT TO SAVE QR CODE IMG\n")

img =qrcode.make(qr)
img.save(saveit+".jpg")
