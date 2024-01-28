## At first => pip install pywhatkit => your machine
import pywhatkit

phone_no = '+8801713430911'
# message = 'Hello,Hafizur Rahman Omar, How are you'
# pywhatkit.sendwhatmsg(phone_no, message, 10, 30, 10, True, 10)

image = 'SocialMedia\kentbeck.jpg'
pywhatkit.sendwhats_image(phone_no, image, 'image')
