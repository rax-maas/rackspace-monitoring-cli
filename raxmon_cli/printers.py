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


__all__ = [
    'print_list',
    'print_success',
    'print_error'
]


def print_list(data, include_details=False):
    if not data:
        pprint(data)
        return

    for item in data:
        if include_details:
            pprint(item.__dict__)
        else:
            pprint(item)

    print('')
    print('Total: ' + str(len(data)))


def print_success(message):
    print(message)


def print_error(error):
    pprint(error)
