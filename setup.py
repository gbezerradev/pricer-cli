from setuptools import setup

setup(
    name="pricer",
    version="0.1.0",
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pricer = main:cli",
        ],
    },
)
