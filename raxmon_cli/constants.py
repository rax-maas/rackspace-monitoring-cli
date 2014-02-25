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
API_URL = [['--api-url'], {'dest': 'api_url', 'help': 'API URL Example: '
                                                      'https://monitoring.api.'
                                                      'rackspacecloud.com/v1.0'}]
TENANT = [['--tenant'], {'help': 'Tenant id'}]
API_TOKEN = [['--api-token'], {'dest': 'api_token', 'help': 'API Auth token from a '
                               'previous request or an impersonation token. '
                               'Requires: --tenant Conflicts: --api-key.'}]
AUTH_URL = [['--auth-url'], {'dest': 'auth_url', 'help': 'Auth URL'}]

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
    TENANT,
    API_KEY,
    API_TOKEN,
    DEBUG,
    NO_SSL_VERIFY,
    AUTH_URL,
]

ACTION_OPTIONS = {
    'list': [
        DETAILS,
        MARKER
    ],

    'get': [
        DETAILS,
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

CONFLICTING_OPTIONS = [['api_key', 'api_token']]

REVERSE = [['-r', '--reverse'], {'dest': 'reverse',
                                 'action': 'store_true',
                                 'default': False,
                                 'help': 'Reverse results'}]
