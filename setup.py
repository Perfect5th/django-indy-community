import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-indy-community',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='996.ICU License',  # see https://github.com/996icu/996.ICU
    description='A simple Django package to build web-based Indy agent applications.',
    long_description=README,
    url='https://github.com/AnonSolutions/django-indy-community',
    author='Ian Costanzo',
    author_email='ian@anon-solutions.ca',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: Hyperledger Indy',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: 996.ICU License',  
        'Operating System :: Ubuntu, Mac OS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Hyperledger Indy',
        'Topic :: Internet :: WWW/HTTP :: Self Soverign Identity',
    ],
)
