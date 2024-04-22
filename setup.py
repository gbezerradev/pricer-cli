from setuptools import setup, find_packages

setup(
    name="pricer",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pricer = main:cli",
        ],
    },
)
