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

from __future__ import with_statement

import os
import sys

from distutils.core import setup
from distutils.core import Command
from subprocess import call
from os.path import join as pjoin


if (sys.version_info < (2, 5, 0) or sys.version_info >= (3, 0, 0)):
    raise RuntimeError('Unsupported Python version. Supported versions are:' +
                       '2.5, 2.6, 2.7 / PyPy')


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


class GenerateCompletionsCommand(Command):
    description = "Generate bash completions file for all the commands"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        path = pjoin(os.getcwd(), 'commands/')
        files = os.listdir(path)
        content = '\n'.join(['complete -F _optcomplete %s' % (f) for f in files])

        with open('contrib/completions.sh', 'w') as fp:
            fp.write(content)

        print('Done')

scripts = os.listdir(pjoin(os.getcwd(), 'commands/'))
scripts = [pjoin(os.getcwd(), 'commands/', path) for path in scripts]

pre_python26 = (sys.version_info[0] == 2 and sys.version_info[1] < 6)


requires = ['rackspace-monitoring>=0.7.1']

if pre_python26:
    requires.append('simplejson')

setup(
    name='rackspace-monitoring-cli',
    version=read_version_string(),
    description='Command Line Utility for Rackspace Cloud Monitoring (MaaS)',
    author='Rackspace, Inc.',
    author_email='monitoring@rackspace.com',
    install_requires=requires,
    scripts=scripts,
    packages=[
        'raxmon_cli',
    ],
    package_dir={
        'raxmon_cli': 'raxmon_cli',
    },
    package_data={
        'raxmon_cli': ['data/cacert.pem'],
    },
    license='Apache License (2.0)',
    url='https://github.com/racker/rackspace-monitoring-cli',
    cmdclass={
        'pep8': Pep8Command,
        'gencompletions': GenerateCompletionsCommand
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
