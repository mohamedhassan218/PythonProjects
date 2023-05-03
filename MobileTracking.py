import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from sys import argv
"""
    - Take the phone number from the command line.
    - Tranfrom it from a string to a phonenumber object using pase().
    - Store timezone, carrier and geographical region of the number, then print them.
"""
def phone_tracker():
    phone = argv[1]
    number = phonenumbers.parse(phone)
    time = timezone.time_zones_for_number(number)
    phone_carrier = carrier.name_for_number(number, 'en')
    phone_region = geocoder.description_for_number(number, 'en')
    print(number)
    print(time)
    print(phone_carrier)
    print(phone_region)
phone_tracker()