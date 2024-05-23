# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erp-app/__init__.py
from erp-app import __version__ as version

setup(
	name='erp-app',
	version=version,
	description='Sample Applications Development',
	author='Yuan-Yao Lou',
	author_email='yuanyao.lou@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
