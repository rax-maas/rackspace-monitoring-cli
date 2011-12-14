# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from distutils.core import setup
from distutils.core import Command
from subprocess import call
from os.path import join as pjoin


def read_version_string():
    version = None
    sys.path.insert(0, pjoin(os.getcwd()))
    from raxmon_cli import __version__
    version = __version__
    sys.path.pop(0)
    return version


class Pep8Command(Command):
    description = "run pep8 script"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pep8
            pep8
        except ImportError:
            print 'Missing "pep8" library. You can install it using pip: ' + \
                  'pip install pep8'
            sys.exit(1)

        cwd = os.getcwd()
        retcode = call(('pep8 %s/raxmon_cli/' %
                (cwd)).split(' '))
        sys.exit(retcode)

scripts = os.listdir(pjoin(os.getcwd(), 'commands/'))
scripts = [pjoin(os.getcwd(), 'commands/', path) for path in scripts]

setup(
    name='rackspace-monitoring-cli',
    version=read_version_string(),
    description='Command Line Utility for rackspace-monitoring library',
    author='Rackspace',
    author_email='cmbeta@rackspace.com',
    install_requires=['rackspace_monitoring >= 0.1.0'],
    scripts=scripts,
    packages=[
        'raxmon_cli',
    ],
    package_dir={
        'raxmon_cli': 'raxmon_cli',
    },
    license='Apache License (2.0)',
    url='tba',
    cmdclass={
        'pep8': Pep8Command
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
