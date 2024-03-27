from two_fa import TwoFa

sub = TwoFa(issuer_name="Prembly", storage="cloudinary", cloud_name="dxfl9fici", api_key="287688117815528", api_secret="CWhkICvYBDJgUrCDs2zLgUenxVI")

# Create QRCode
t = sub.create_otp(identifier="samson@myidentitypass.com")
print(t)

# Validate OTP
# t = sub.validate_otp(user_key="DEPB73TJNMZYAVZ7IGUMX42W5DJVLDLX", code="856864")
# print(t)