#!/usr/bin/env python

"""
Copyright 2019 ARC Centre of Excellence for Climate Systems Science

author: Aidan Heerdegen <aidan.heerdegen@anu.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import pytest
from analytics import utils

# print(utils.__file__)

def test_read_config():

    assert utils.read_config('test/capture_config.yaml') == {
           'short': [{'project': 'v45', 'outputdir': 'tmp', 'datestamp': "datetime.now().strftime('%F')"}, 
                     {'project': 'w48', 'outputdir': 'dumpdir', 'datestamp': "datetime.now().strftime('%F')"}], 
           'compute': [{'project': 'v45', 'outputdir': 'dumpdir', 'datestamp': "datetime.now().strftime('%F')"}, 
                       {'project': 'w48', 'outputdir': 'dumpdir', 'datestamp': "datetime.now().strftime('%F')"}], 
           'gdata': [{'mount': 'gdata1a', 'project': 'v45', 'outputdir': 'dumpdir', 'datestamp': "datetime.now().strftime('%F')"}, 
                     {'mount': 'gdata3', 'project': 'w48', 'outputdir': 'dumpdir', 'datestamp': "datetime.now().strftime('%F')"}]}

