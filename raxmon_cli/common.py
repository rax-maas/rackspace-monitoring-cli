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

import sys
import traceback
from pprint import pprint
from optparse import OptionParser

from . import optcomplete

from rackspace_monitoring.providers import get_driver
from rackspace_monitoring.types import Provider

from raxmon_cli.constants import GLOBAL_OPTIONS, ACTION_OPTIONS
from raxmon_cli.constants import API_URL_ADDRESS
from raxmon_cli.printers import print_list, print_error, print_success
from raxmon_cli.utils import get_credentials

__all__ = [
    'run_action',
    'get_instance'
]


def get_parser():
    usage = 'usage: %prog --config=<path to the config file>'
    parser = OptionParser(usage=usage)
    return parser


def run_action(cmd_options, required_options, resource, action, callback):
    cmd_options = cmd_options or []
    all_options = GLOBAL_OPTIONS + cmd_options
    required_options = required_options or []
    parser = get_parser()

    def done(result):
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
        else:
            pprint(result)

    if action in ACTION_OPTIONS:
        all_options.extend(ACTION_OPTIONS[action])

    for args, kwargs in all_options:
        parser.add_option(*args, **kwargs)

    optcomplete.autocomplete(parser)
    (options, args) = parser.parse_args()

    for option in required_options:
        if not getattr(options, option, None):
            raise Exception('Missing required option: ' + option)

    username, api_key, api_url = get_credentials()

    if options.username:
        username = options.username

    if options.api_key:
        api_key = options.api_key

    api_url = api_url or API_URL_ADDRESS

    if options.api_url:
        api_url = options.api_url

    if not username or not api_key:
        print('No username and API key provided!')
        print('You need to either put credentials in ~/.raxrc or ' +
              'pass them to the command using --username and --api-key option')
        sys.exit(1)

    instance = get_instance(username, api_key, api_url)

    try:
        callback(instance, options, args, done)
    except Exception:
        traceback.print_exc(file=sys.stderr)


def get_instance(username, api_key, url):
    driver = get_driver(Provider.RACKSPACE)
    instance = driver(username, api_key, ex_force_base_url=url)
    return instance
