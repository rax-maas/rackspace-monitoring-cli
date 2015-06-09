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

from __future__ import absolute_import

import os
import os.path
import sys
import traceback
from pprint import pprint
from optparse import OptionParser

from . import optcomplete

from rackspace_monitoring.providers import get_driver
from rackspace_monitoring.types import Provider

import libcloud.security
from libcloud import _init_once

CA_CERT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'data/cacert.pem')
libcloud.security.CA_CERTS_PATH.insert(0, CA_CERT_PATH)

from raxmon_cli.constants import GLOBAL_OPTIONS, ACTION_OPTIONS
from raxmon_cli.printers import print_list, print_error, print_success
from raxmon_cli.utils import get_config

__all__ = [
    'run_action',
    'get_instance'
]


def get_parser():
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    return parser


def run_action(cmd_options, required_options, resource, action, callback):
    cmd_options = cmd_options or []
    all_options = GLOBAL_OPTIONS + cmd_options
    required_options = required_options or []
    parser = get_parser()

    def done(result=None):
        if action == 'list':
            print_list(result, options.details)
        elif action == 'create':
            print_success('Resource created. ID: ' + result.id)
        elif action == 'update':
            print_success('Resource has been successfully updated')
        elif action == 'delete':
            if result:
                print_success('Resource deleted')
            else:
                print_success('Resource not deleted')
        elif result:
            pprint(result)

    if action in ACTION_OPTIONS:
        all_options.extend(ACTION_OPTIONS[action])

    for args, kwargs in all_options:
        parser.add_option(*args, **kwargs)

    optcomplete.autocomplete(parser)
    (options, args) = parser.parse_args()

    for option in required_options:
        if not getattr(options, option, None):
            parser.print_help()
            print('\nMissing required options: ' + option)
            sys.exit(1)

    result = get_config()
    username, api_key = result['username'], result['api_key']
    auth_token, api_url = result['auth_token'], result['api_url']
    auth_url = result['auth_url']
    ssl_verify = result['ssl_verify']

    if options.username:
        username = options.username

    if options.api_key:
        api_key = options.api_key

    if options.api_url:
        api_url = options.api_url

    if options.auth_token:
        auth_token = options.auth_token

    if options.auth_url:
        auth_url = options.auth_url

    if (not username or not api_key) and (not auth_token or not api_url):
        print('No username/API key or auth token/API URL provided!')
        print('You need to either put credentials in ~/.raxrc or '
              'pass them to the command using --username/--api-key '
              'or --auth-token/--api-url options')
        sys.exit(1)

    if options.debug:
        os.environ['LIBCLOUD_DEBUG'] = '/dev/stderr'
        _init_once()

    if options.no_ssl_verify or ssl_verify == False:
        libcloud.security.VERIFY_SSL_CERT = False

    instance = get_instance(username, api_key, api_url, auth_url, auth_token)

    if not getattr(options, 'who', None):
        options.who = username

    try:
        callback(instance, options, args, done)
    except Exception:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


def get_instance(username, api_key, url, auth_url=None, auth_token=None):
    driver = get_driver(Provider.RACKSPACE)

    kwargs = {}
    kwargs['ex_force_base_url'] = url
    kwargs['ex_force_auth_url'] = auth_url
    kwargs['ex_force_auth_token'] = auth_token
    instance = driver(username, api_key, **kwargs)

    return instance
