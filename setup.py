# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='edx-nau-registration-form',
    version='1.0',
    description='Custom registration form extension apps for Open edX',
    packages=['form_extender'],
    install_requires=[
        'Django',
    ],
)
