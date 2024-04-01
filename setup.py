import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twofa", # Replace with your own username
    version="1.0.0",
    author="Samson Ilemobayo",
    author_email="ilemobayosamson@gmail.com",
    description="TwoFa is a Python library designed to make two-factor authentication (2FA) integration seamless and secure for applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finedevsam/two-fa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    
    ],
    python_requires='>=3.7',

    install_requires=[
        "pyqrcode",
        "qrcode",
        "pyotp",
        "boto3",
        "pillow",
        "cloudinary",
        "wheel"
    ],
)