#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.3.8'

setup(
    name="sbo-selenium",
    version=version,
    packages=find_packages(),
    zip_safe=False,
    description="",
    long_description="""\
""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    package_data={
        'sbo_selenium': [
            'static/js/*.js',
        ],
    },
    install_requires=[
        'Django>=1.5.1,<1.6',
        'django-nose',
        'selenium>=2.37.2',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
