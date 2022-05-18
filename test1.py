from libhindimagz.libhindimagz import *

fetcher = Fetcher(mag_id=527, limit=10, img_size=3, issue_id=36358, cat_id=3)

print(a.send_otp(b'+91XXXXXXX').content)
print(a.verify_otp(b'+91XXXXXXXX', 'OTP').content)
b=fetcher.get_magazine('JN:ms:user:<stuff>:<stuff>')
print(b.content.decode('utf-8'))
b = fetcher.get_issue_det()
print(b.content.decode('utf-8'))
