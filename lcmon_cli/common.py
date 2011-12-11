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

from pprint import pprint
from optparse import OptionParser

from libcloud_monitoring.providers import get_driver
from libcloud_monitoring.types import Provider

from lcmon_cli.constants import GLOBAL_OPTIONS, ACTION_OPTIONS
from lcmon_cli.printers import print_list, print_error, print_success

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

    (options, args) = parser.parse_args()

    for option in required_options:
        if not getattr(options, option, None):
            raise Exception('Missing required option: ' + option)

    instance = get_instance(options.username, options.api_key,
                            options.api_url)

    try:
        callback(instance, options, args, done)
    except Exception, e:
        print_error(e)


def get_instance(username, api_key, url):
    driver = get_driver(Provider.RACKSPACE)
    instance = driver(username, api_key, ex_force_base_url=url)
    return instance
