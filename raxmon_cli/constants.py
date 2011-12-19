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

__all__ = [
    'CREDENTIALS_FILE',
    'CONFIG_PATH',
    'API_URL_ADDRESS',
    'GLOBAL_OPTIONS',
    'ACTION_OPTIONS'
]

import os
from os.path import join as pjoin, expanduser

CREDENTIALS_FILE = '.raxrc'
CONFIG_PATH = pjoin(expanduser('~'), CREDENTIALS_FILE)

API_URL_ADDRESS = 'https://cmbeta.api.rackspacecloud.com/v1.0'

USERNAME = [['--username'], {'dest': 'username', 'help': 'API username'}]
API_KEY = [['--api-key'], {'dest': 'api_key', 'help': 'API key'}]
API_URL = [['--api-url'], {'dest': 'api_url', 'help': 'API URL'}]

DETAILS = [['--details'], {'dest': 'details', 'action': 'store_true',
                           'help': 'Display all the object attributes'}]

MARKER = [['--marker'], {'dest': 'marker',
                           'help': 'Marker. If provided only the entries' +
                           ' with the key larger then and equal to the' +
                           ' marker will be returned'}]

GLOBAL_OPTIONS = [
    API_URL,
    USERNAME,
    API_KEY
]

ACTION_OPTIONS = {
    'list': [
        DETAILS,
        MARKER
     ],

    'overview': [
        DETAILS,
        MARKER
     ]

}
