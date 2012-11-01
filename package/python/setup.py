#!/usr/bin/env python

from distutils.core import setup

setup(name='CloudStackClient',
            version='1.1',
            description='Python CloudStack Client',
            author='Julien Garet',
            author_email='julien@garet.info',
            url='https://github.com/jgaret/cloudstack-client-generator',
            packages=['BaseCloudStackClient','CloudStackClient'],
           )
