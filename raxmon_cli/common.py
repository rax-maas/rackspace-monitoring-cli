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

from raxmon_cli.constants import GLOBAL_OPTIONS, ACTION_OPTIONS, CONFLICTING_OPTIONS
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

    for options_list in CONFLICTING_OPTIONS:
        matched = []
        for opt in options_list:
            if getattr(options, opt):
                matched.append(opt)

        if len(matched) > 1:
            print('\nConflicting options %s' % str(options_list))
            sys.exit(1)

    for option in required_options:
        if not getattr(options, option, None):
            parser.print_help()
            print('\nMissing required options: ' + option)
            sys.exit(1)

    result = get_config()
    username, api_key = result['username'], result['api_key']
    api_url, auth_url = result['api_url'], result['auth_url']
    ssl_verify = result['ssl_verify']

    if options.username:
        username = options.username

    if options.api_key:
        api_key = options.api_key

    if options.api_url:
        api_url = options.api_url

    if options.auth_url:
        auth_url = options.auth_url

    api_token = options.api_token if options.api_token else None

    if not api_token and not username and not api_key or username and not api_key:
        print('No username and API key or API token provided!')
        print('You need to either put credentials in ~/.raxrc or ' +
              'pass them to the command using --username and --api-key option')
        sys.exit(1)

    if api_token and not options.tenant:
        print("--api-token requires a --tenant id!")
        sys.exit(1)
    else:
        api_url = api_url + '/' + options.tenant

    if options.debug:
        os.environ['LIBCLOUD_DEBUG'] = '/dev/stderr'
        _init_once()

    if options.no_ssl_verify or ssl_verify == False:
        libcloud.security.VERIFY_SSL_CERT = False

    instance = get_instance(username, api_url, auth_url=auth_url, api_key=api_key,
                            api_token=api_token)

    if not getattr(options, 'who', None):
        options.who = username

    try:
        callback(instance, options, args, done)
    except Exception:
        traceback.print_exc(file=sys.stderr)


def get_instance(username, url, api_key=None, api_token=None, auth_url=None):
    driver = get_driver(Provider.RACKSPACE)

    kwargs = {}
    kwargs['ex_force_auth_token'] = api_token
    kwargs['ex_force_base_url'] = url
    kwargs['ex_force_auth_url'] = auth_url
    instance = driver(username, api_key, **kwargs)

    return instance
