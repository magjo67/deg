#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'deg',
    version = '2.0.3',
    description = 'Program för att skapa degrecept',
    url='https://github.com/magjo67/deg.git',
    author = 'Magnus Johansson',
    author_email='magjo67@gmail.com',
    license='BSD 2-clause',
    packages=['deg'],
    install_requires=['pandas',                     
                      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Intended Audience :: Other Audience",
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    include_package_data=True,
    scripts=['bin/deg'],
    

)
