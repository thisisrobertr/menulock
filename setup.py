from setuptools import setup
import subprocess
import os

APP=['menulock.py']
DATA_FILES=['menuicon-light.png', 'menuicon-dark.png']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'iconfile': 'menulock.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
