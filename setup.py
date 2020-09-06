from setuptools import setup

setup(
    name='snov-python',
    version='0.1.0',
    author='Nathan Workman',
    author_email='nathancworkman@gmail.com',
    description='An (unofficial) Python Client for the Snov.io API',
    url='https://github.com/NathanWorkman/snov-python.git',
    packages=['snov'],
    requires=['requests (>=2.18.4)'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
