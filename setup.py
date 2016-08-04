# -*- coding: utf-8 -*-
"""
sentry-wechat
==============

An extension for Sentry which integrates with WeChat. It will forwards
notifications to an WeChat public account.

:copyright: (c) 2016 by the Arron Jheng.
:license: 3-clause BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name="sentry-wechat",
    version="1.0.0",
    description=u"A Sentry extension which integrates with WeChat",
    url="https://github.com/aaronjheng/sentry-wechat",
    author="Aaron Jheng",
    author_email="wentworth@outlook.com",
    license="3-clause BSD",
    packages=find_packages(),
    package_data={
        "": ["LICENSE"],
    },
    install_requires=[
        "sentry>=6.0.0"
    ],
    entry_points={
        "sentry.plugins": [
            "wechat=sentry_wechat.plugin:WechatMessage",
        ]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
    ]
)
