import os
import sys

from setuptools import setup

packages = [
    'hulu'
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    # Basic package information.
    name='hulu',
    version='0.1.0',
    packages=packages,
    include_package_data=True,
    install_requires=['requests>=1.0.0, <2.0.0', 'requests_oauthlib==0.3.0'],
    author='Mike Helmick',
    author_email='mikehelmick@me.com',
    license=open('LICENSE').read(),
    url='http://github.com/michaelhelmick/hulu/tree/master',
    keywords='hulu python api json',
    description='A Python library to interact with Hulu\'s "hidden" 2.0 API.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
