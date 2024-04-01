# TwoFa: Two-Factor Authentication for Python

## Introduction

TwoFa is a Python library designed to make two-factor authentication (2FA) integration seamless and secure for applications. By providing an easy-to-use interface for adding an additional layer of security, TwoFa ensures that user authentication is more robust and resistant to unauthorized access.

### Features
1. **Easy Integration:** Simplify the process of adding 2FA to your Python applications.
2. **Multiple 2FA Methods:** Supports various two-factor authentication methods, including SMS, email, and authenticator apps.
3. **Customizable:** Flexible configuration to suit different security requirements.
4. **Secure:** Implements industry-standard protocols to ensure the security of authentication processes.
5. **Support Multiple Storage Device:** Support AWS S3Bucket, Cloudinary e.t.c to manage authentication QR code.


### Installation

Install `TwoFa` using pip:

```python
pip install twofa
```

### Quick Start
Here's how to quickly set up `TwoFa` in your project:

#### 1. Import TwoFa
```python
from twofa import TwoFa
```

#### 2. Initialize TwoFa
```python
twofa = TwoFa(issuer_name='MyApp')
```

### 3. Generate QR Code For Authentication App
```python
resp = twofa.generate_qr_code(identifier="identifier", storage="s3bucket", bucket_name="bucket", access_key="s3 secrete access", secret_access="s3 secrete access key")
print(resp)
```
The generate_qr_code function generates a QR code for two-factor authentication, stores it in a specified storage service, and returns the URL to the stored QR code image. This function is particularly useful for applications implementing 2FA where the QR code is scanned by a user's authentication app.

### Parameters
1. **identifier (str):** A unique identifier for the user, such as an email address or username, to be encoded within the QR code.
2. **storage (str):** The storage service to use for saving the QR code image. Currently supports "s3bucket" and "cloudinary"; future versions may include additional services.

    #### S3 Bucket Configuration
    i. **bucket_name (str):** The name of the bucket in the storage service where the QR code image will be saved.
    ii. **access_key (str):** The access key ID for authenticating with the storage service.
    iii. **secret_access (str):** The secret access key for authenticating with the storage service.

    #### Cloudinary Configuration
    i. **cloud_name (str):** The name of the bucket in the storage service where the QR code image will be saved.

    ii. **api_key (str):** The access key ID for authenticating with the storage service.
    
    iii. **api_secret (str):** The secret access key for authenticating with the storage service.
3. 