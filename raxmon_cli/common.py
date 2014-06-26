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
from raxmon_cli.printers import print_list, print_item, print_error, print_success
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
        elif action == 'get':
            print_item(result, options.details)
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
    api_token = result['api_token']
    tenant = result['tenant']

    if options.username:
        username = options.username

    if options.api_key:
        api_key = options.api_key

    if options.api_url:
        api_url = options.api_url

    if options.auth_url:
        auth_url = options.auth_url

    if options.api_token:
        api_token = options.api_token

    if options.tenant:
        tenant = options.tenant

    if not api_token and not api_key:
        print("No authentication credentials provided")
        sys.exit(1)
    elif api_token and not tenant:
        print("--api-token provided but no --tenant")
        sys.exit(1)
    elif not api_token and api_key and not username:
        print("--api-key but no --username")
        sys.exit(1)

    if api_token and tenant:
        # token should override all api_key
        api_url = api_url + '/' + options.tenant
        api_key = None

    if options.debug:
        os.environ['LIBCLOUD_DEBUG'] = '/dev/stderr'
        _init_once()

    if options.no_ssl_verify or not ssl_verify:
        libcloud.security.VERIFY_SSL_CERT = False

    try:
        instance = get_instance(username, api_url, auth_url=auth_url, api_key=api_key,
                                api_token=api_token)
    except Exception as e:
        if options.debug:
            raise

        if hasattr(e, 'value'):
            print(e.value)
        elif hasattr(e, 'message'):
            print(e.message)
        else:
            raise
        sys.exit(1)

    if not getattr(options, 'who', None):
        options.who = username

    try:
        callback(instance, options, args, done)
    except Exception as e:
        if options.debug:
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)
        else:
            if hasattr(e, 'value'):
                print(e.value)
            elif hasattr(e, 'message'):
                try:
                    print('Error: %s %s' % (e.message['code'], e.message['details']))
                    sys.exit(1)
                except KeyError:
                    print(e.message)
            else:
                raise
            sys.exit(1)


def get_instance(username, url, api_key=None, api_token=None, auth_url=None):
    driver = get_driver(Provider.RACKSPACE)

    kwargs = {}
    kwargs['ex_force_auth_token'] = api_token
    kwargs['ex_force_base_url'] = url
    kwargs['ex_force_auth_url'] = auth_url
    instance = driver(username, api_key, **kwargs)

    return instance
