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

"""
Unit tests for the netplan.interface module.
"""

import unittest

import ddt

from netplan import interface as npiface


@ddt.ddt
class TestInterfaces(unittest.TestCase):
    """
    Test various aspects of the *Interface classes.
    """
    @ddt.data(
        npiface.Interface,
        npiface.PhysicalInterface,
        npiface.EthernetInterface,
        npiface.WirelessInterface,
        npiface.VLANInterface,
        npiface.BondInterface,
        npiface.BridgeInterface,
    )
    def test_interfaces_basic(self, cls):
        """
        Test some basic functionality of the interface classes.
        """
        obj = cls('iface', 'section', {'mtu': 1500})
        self.assertIsInstance(obj, npiface.Interface)
        self.assertIsInstance(obj, cls)
        self.assertEqual(obj.name, 'iface')
        self.assertEqual(obj.section, 'section')

        self.assertEqual(str(obj), 'section/iface')
        got = repr(obj)
        exp = "{name}(name='iface', section='section', data={{'mtu': 1500}})" \
              .format(name=cls.__name__)
        self.assertEqual(got, exp)

        self.assertEqual(obj.data, {'mtu': 1500})
        self.assertEqual(obj.data.get('mtu'), 1500)
        self.assertEqual(obj.data.get('mtux'), None)
        self.assertEqual(obj.data.get('mtu', 9000), 1500)
        self.assertEqual(obj.data.get('mtux', 9000), 9000)

        obj.set('mtu', 1600)
        self.assertEqual(obj.data, {'mtu': 1600})
        self.assertEqual(obj.data.get('mtu'), 1600)
        self.assertEqual(obj.data.get('mtux'), None)
        self.assertEqual(obj.data.get('mtu', 9000), 1600)
        self.assertEqual(obj.data.get('mtux', 9000), 9000)

        obj.set('mtux', 1600)
        self.assertEqual(obj.data, {'mtu': 1600, 'mtux': 1600})
        self.assertEqual(obj.data.get('mtu'), 1600)
        self.assertEqual(obj.data.get('mtux'), 1600)
        self.assertEqual(obj.data.get('mtu', 9000), 1600)
        self.assertEqual(obj.data.get('mtux', 9000), 1600)

        if cls is npiface.Interface or \
           cls is npiface.PhysicalInterface:
            self.assertRaises(Exception, obj.get_parent_names)
        else:
            self.assertEqual(obj.get_parent_names(), [])

    @ddt.data(
        (npiface.EthernetInterface, []),
        (npiface.WirelessInterface, []),
        (npiface.VLANInterface, ['lnk']),
        (npiface.BondInterface, ['i1', 'i2']),
        (npiface.BridgeInterface, ['i1', 'i2']),
    )
    @ddt.unpack
    def test_parent_interface(self, cls, parents):
        """
        Test querying an interface for its parent.
        """
        obj = cls('iface', 'section',
                  {'interfaces': ['i1', 'i2'], 'link': 'lnk'})
        self.assertEqual(obj.get_parent_names(), parents)
