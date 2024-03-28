import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="two-fa", # Replace with your own username
    version="1.0.0",
    author="Samson Ilemobayo",
    author_email="ilemobayosamson@gmail.com",
    description="TwoFa typically refers to 'Two-Factor Authentication,' a security process that requires users to provide two different authentication factors to verify their identity.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finedevsam/two-fa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    
    ],
    python_requires='>=3.6',
    install_requires=[
        "cloudinary",
        "pillow",
        "PyQRCode",
        "qrcode"
    ],
)