"""
Setup script for Dental Mobile Application
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='dental-mobile-app',
    version='1.0.0',
    description='A comprehensive dental practice management mobile application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dental App Team',
    author_email='contact@dentalapp.com',
    url='https://github.com/dentalapp/dental-mobile-app',
    py_modules=['main'],
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Office/Business',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='dental healthcare mobile application kivy practice-management',
    entry_points={
        'console_scripts': [
            'dental-app=main:DentalApp',
        ],
    },
)
