#!/usr/bin/env python
#
# Copyright (c) 2018  StorPool.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

import netplan

setuptools.setup(
    name='netplan',
    version=netplan.VERSION,
    packages=('netplan',),

    author='Peter Pentchev',
    author_email='pp@storpool.com',
    description='A library for parsing the netplan configuration data',
    license='Apache License 2.0',
    keywords='netplan',
    url='https://github.com/storpool/netplan',

    zip_safe=True,

    scripts=['bin/netplan-parser'],
)
