import os
from pyqrcode import QRCode
import pyqrcode
import png
import string, random
import qrcode
import pyotp
from PIL import Image
import io

import cloudinary
import cloudinary.uploader
import cloudinary.api


class ManageOTP:
    
    @staticmethod
    def image_name():
        res = ''.join(random.choices(string.digits, k=4))
        code = str(res)
        _id = "image{}".format(code)
        return _id
    
    @staticmethod
    def create_otp(cloud_name: str, api_key: str, api_secret: str, identifier: str, issuer_name:str):
        try:
            cloudinary.config(cloud_name=cloud_name, api_key=api_key, api_secret=api_secret)
            user_keys = pyotp.random_base32()
            otp = pyotp.totp.TOTP(user_keys).provisioning_uri(identifier, issuer_name=issuer_name)
            img = qrcode.make(otp)
            img_url = cloudinary.uploader.upload(ManageOTP.image_to_byte_array(img))
            return user_keys, img_url.get("url")
        except Exception as e:
            return False, e
    
    @staticmethod
    def verify_otp(identifier: str, otp_code: str):
        totp = pyotp.TOTP(identifier)
        if totp.now() == otp_code:
            return True
        return False
    
    
    def create_time_base_otp(self):
        data = QRCode.objects.filter(email=self.email).first()
        
        totp = pyotp.TOTP(data.user_key, interval=600)
        otpcode = totp.now()
        # print(otpcode)
        self.send.send_otp(self.email, otpcode)
        pass
    
    def verify_time_base_otp(self):
        data = QRCode.objects.filter(email=self.email).first()
        totp = pyotp.TOTP(data.user_key, interval=600)
        check = totp.verify(self.otp_code)
        return check
    
    @staticmethod
    def image_to_byte_array(image: Image) -> bytes:
        # BytesIO is a file-like buffer stored in memory
        imgByteArr = io.BytesIO()
        # image.save expects a file-like as a argument
        image.save(imgByteArr, format=image.format)
        # Turn the BytesIO object back into a bytes object
        imgByteArr = imgByteArr.getvalue()
        return imgByteArr