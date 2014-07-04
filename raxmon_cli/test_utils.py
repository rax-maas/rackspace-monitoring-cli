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

import unittest

import utils

class TestRaxmonClientUtils(unittest.TestCase):
    # WIP
    # Status: Testing str_to_dict for nested listed handling.
    # 
    # Others to follow:
    # test_str_to_list
    # test_instance_to_dict
    # test_get_credentials
    # test_read_json_from_file

    def setUp(self):
        self.simple_url_input_string = "url=http://foobar.com/justin,args=foo,otherKey=42"
        self.nested_url_input_string = "url=http://foobar.com/justin,args=foo,args=justin,otherKey=AnotherKey,finalKey=42,args=bar"

    def test_str_to_dict(self):
        assert utils.str_to_dict(None) is None

        # Basic behavior for poorly formed inputs
        self.assertEquals(None, utils.str_to_dict(None))
        self.assertEquals(None, utils.str_to_dict(""))
        self.assertEquals({}, utils.str_to_dict("no_vals"))

        # Unnested arguments lists are parsed
        expected_dict_simple = {
            "url": "http://foobar.com/justin", 
            "args": "foo", 
            "otherKey": "42"
        }
        self.assertEquals(expected_dict_simple, utils.str_to_dict(self.simple_url_input_string))

        # Nested List Behavior
        expected_dict_nested = {
            "url": "http://foobar.com/justin",
            "args": ["foo", "justin", "bar"],
            "otherKey": "AnotherKey",
            "finalKey": "42"
        }
        self.assertEquals(expected_dict_nested, utils.str_to_dict(self.nested_url_input_string))

if __name__ == '__main__':
    unittest.main()
