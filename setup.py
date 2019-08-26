# -*- coding: utf-8 -*-
"""
Created on 24 Aug 2019

@author: steph
"""

from setuptools import setup, find_packages

setup(

    name='tuneRs',
    url='https://github.com/metriczulu/wordvecpy',
    author='Shane Stephenson / metriczulu',
    author_email='stephenson.shane.a@gmail.com', 
    packages=find_packages(),
    install_requires = ['numpy', 'tqdm', 'sklearn'],
    version='v0.3',
    license="None",
    description='Package for tuning hyperparameters with resampling methods',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r').read(),
    download_url = 'https://github.com/metriczulu/tuneRs/archive/v0.3.tar.gz'
)
