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

# Standard libraries
import datetime
import os
import pwd
import shlex
import subprocess
import sys

# Third party libraries
import ncimonitor
import yaml

def read_config(filename):
    """
    Return a configuration dictionary
    """
    try:
        with open(filename, 'r') as config_file:
            configs = list(yaml.safe_load_all(config_file))
    except IOError as exc:
        print('Warning: config file {0} not found!'
                .format(filename))
        raise
    else:
        config = configs.pop(0)
        if configs:
            # Check if there is another "yaml" document, where
            # default values are stored
            defaults = configs.pop(0)
            for cmd in config.keys():
                for item in config[cmd]:
                    # Loop through all the defaults and add them
                    # to the config if they aren't already defined
                    for k,v in defaults.items():
                        if k not in item:
                            item[k] = v

    return config

def run_cmd(cmd, **kwargs):
    """
    Run a cmd using subprocess
    """
    subprocess.check_call(shlex.split(cmd.format(kwargs)))
