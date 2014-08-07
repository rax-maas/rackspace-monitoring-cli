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

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

from raxmon_cli.constants import CONFIG_PATH

__all___ = [
    'str_to_list',
    'str_to_dict',
    'instance_to_dict',
    'get_credentials',
    'read_json_from_file'
]


def str_to_list(string):
    if not string:
        return None

    return string.split(',')


def str_to_dict(string):
    if not string:
        return None

    result = {}
    split = string.split(',')

    for value in split:
        split2 = value.split('=')

        if len(split2) == 2:
            key, value = split2
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value

    return result


def instance_to_dict(instance, keys, include_none=False):
    result = {}

    for key in keys:
        value = getattr(instance, key, None)

        if value is None and not include_none:
            continue

        result[key] = value
    return result


def get_config():
    keys = [['credentials', 'username', 'username'],
            ['credentials', 'api_key', 'api_key'],
            ['api', 'url', 'api_url'],
            ['api', 'token', 'auth_token'],
            ['auth_api', 'url', 'auth_url'],
            ['ssl', 'verify', 'ssl_verify']]

    result = {}

    result['username'] = os.getenv('RAXMON_USERNAME', None)
    result['api_key'] = os.getenv('RAXMON_API_KEY', None)
    result['api_url'] = os.getenv('RAXMON_API_URL', None)
    result['auth_url'] = os.getenv('RAXMON_AUTH_URL', None)
    result['ssl_verify'] = os.getenv('RAXMON_SSL_VERIFY', None)
    result['auth_token'] = os.getenv('RAXMON_AUTH_TOKEN', None)

    config = ConfigParser.ConfigParser()
    config.read(os.getenv('RAXMON_RAXRC') or CONFIG_PATH)

    for (config_section, config_key, key) in keys:
        if result[key]:
            # Already specified as an env variable
            continue

        try:
            value = config.get(config_section, config_key)
        except ConfigParser.Error:
            continue

        result[key] = value

    # convert "false" to False
    if result['ssl_verify']:
        result['ssl_verify'] = not (result['ssl_verify'].lower() == 'false')
    else:
        result['ssl_verify'] = True

    return result


def read_json_from_file(file_path):
    with open(file_path, 'r') as fp:
        content = fp.read()

    return content
