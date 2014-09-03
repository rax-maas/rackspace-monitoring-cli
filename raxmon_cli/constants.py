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
    'GLOBAL_OPTIONS',
    'ACTION_OPTIONS',
    'REVERSE'
]

import os
from os.path import join as pjoin, expanduser

CREDENTIALS_FILE = '.raxrc'
CONFIG_PATH = pjoin(expanduser('~'), CREDENTIALS_FILE)

USERNAME = [['--username'], {'dest': 'username', 'help': 'API username'}]
API_KEY = [['--api-key'], {'dest': 'api_key', 'help': 'API key'}]
API_URL = [['--api-url'], {'dest': 'api_url', 'help': 'API URL excluding the ' +
                                                      'tenant id'}]
AUTH_URL = [['--auth-url'], {'dest': 'auth_url', 'help': 'Auth URL'}]
AUTH_TOKEN = [['--auth-token'], {'dest': 'auth_token', 'help': 'Auth token'}]

DETAILS = [['--details'], {'dest': 'details', 'action': 'store_true',
                           'help': 'Display all the object attributes'}]

MARKER = [['--marker'], {'dest': 'marker',
                           'help': 'Marker. If provided only the entries' +
                           ' with the key larger then and equal to the' +
                           ' marker will be returned'}]
DEBUG = [['--debug'], {'dest': 'debug',
                       'action': 'store_true',
                       'help': 'Enable debug mode - log all the requests' +
                       ' and responses.'}]
NO_SSL_VERIFY = [['--no-ssl-verify'], {'dest': 'no_ssl_verify',
                                       'action': 'store_true',
                                       'help': 'Don\'t verify the SSL certificate.'}]

WHO = [['--who'], {'dest': 'who',
                           'help': 'Person who performed the action'}]
WHY = [['--why'], {'dest': 'why',
                           'help': 'Reason for this action which is stored in' +
                           'the audit log'}]


GLOBAL_OPTIONS = [
    API_URL,
    USERNAME,
    API_KEY,
    DEBUG,
    NO_SSL_VERIFY,
    AUTH_URL,
    AUTH_TOKEN
]

ACTION_OPTIONS = {
    'list': [
        DETAILS,
        MARKER
     ],

    'create': [
      WHO,
      WHY
    ],

    'update': [
      WHO,
      WHY
    ],

    'delete': [
      WHO,
      WHY
    ],

    'overview': [
        DETAILS,
        MARKER
     ]

}

REVERSE = [['-r', '--reverse'], {'dest': 'reverse',
                                 'action': 'store_true',
                                 'default': False,
                                 'help': 'Reverse results'}]
