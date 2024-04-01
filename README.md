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
from twofa.auth import TwoFa
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

### Returns

After calling the QR code generation function, the service returns a JSON object containing the following fields:

1. **status (bool):** Indicates the success or failure of the QR code generation and storage process. A value of True means the operation was successful, while False indicates a failure.
2. **url (str):** The URL where the generated QR code image has been stored. This URL can be used to display the QR code to the user for scanning with a 2FA app.
3. **user_key (str):** A unique key associated with the user's 2FA setup. This key is important for identifying the 2FA configuration specific to the user and may be needed for verifying the 2FA token generated by the user's authentication app.
4. **identifier (str):** The unique identifier provided during the QR code generation request. Typically, this is the user's email address or username. It confirms the entity for which the QR code was generated.

```json
    {
    "status": true,
    "url": "http://res.cloudinary.cvvxm2e4kj.png",
    "user_key": "4CXDI7QR53NTBWA3DD4DSY",
    "identifier": "johndoe@gmail.com"
    }
```

### Fields Description
i. **status:** This boolean field is crucial for error handling in your code. Always check this field to ensure the operation was successful before proceeding.

ii. **url:** Use this URL to retrieve the QR code image. You can embed it in an <img> tag in HTML or download it for display in other applications.

iii. **user_key:** Securely store this key in your application's database associated with the user's account. It will be required for validating 2FA tokens.

iv. **identifier:** Provides a way to double-check that the QR code generated corresponds to the correct user account, especially in systems where multiple requests might be processed simultaneously.

### Handling Errors
In case of failure, the status field will be `False`, and the response may include an additional field, error, detailing the reason for the failure. Ensure your application can gracefully handle such scenarios and provide appropriate feedback to the user.

### 4. Validate Code
The `validate_code` function is designed to validate a two-factor authentication (2FA) code provided by the user. It checks the code against the user's previously generated and stored 2FA setup, ensuring that the code is correct and within its validity period.

### Parameters
1. **user_key (str):** A unique key associated with the user's 2FA setup. This key should have been saved during the 2FA setup process.
2. **code (str):** The 2FA code that the user entered, which needs to be validated.

### Returns
A dictionary containing the following keys:
1. **status (bool):** Indicates the success or failure of the code validation. A value of True means the code is valid, while False indicates it is invalid or expired.
2. **message (str):** Provides additional information about the validation result. Typical messages include 'valid' for successful validations or error messages if the validation fails.

### Example Usage

Here's how to use the `validate_code` function:
```python
resp = twofa.validate_code(user_key="DEPB73TJNMZYAVZ7IG", code="856864")
print(resp)
```

```json
{"status": false, "message": "not valid"}
```
### Handling Errors
The function is designed to be robust against common errors, returning a `False` status for any issue encountered during validation, including invalid codes, expired codes, or internal errors. Always check the `status` field to determine the outcome of the validation process.

### Notes
i. Ensure the `user_key` corresponds to the correct user's 2FA setup before attempting to validate a code.

ii. The `code` parameter should be treated as sensitive information and handled securely throughout your application.

iii. This function should be integrated as part of your application's authentication flow, typically after the user has provided their primary credentials.

### Advanced Usage

Refer to the documentation for advanced configurations, including setting up different 2FA methods and customizing token expiration times.

### Contributing

We welcome contributions to `TwoFa`! If you have suggestions for improvements or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

Please refer to our contribution guidelines for more details.

### License
`TwoFa` is released under the GNU GENERAL PUBLIC LICENSE.