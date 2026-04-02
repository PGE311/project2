#/usr/bin/env python
#
# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert
import numpy as np


with open("project2.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("project2.py", "w") as f:
    f.write(python_file)

from project2 import *


class TestSolution(unittest.TestCase):

    def test_compute_largest_member_force_1(self):

        f_all = np.array([[400., 600, 0], [700, 100, 200], [100, 1000, 100], [0, 500, 500], 
                  [500, 0, 1500],  [1200, 0, 100], [1600, 0, 0], [0, 0, 1600], [0, 1600, 0], [500, 500, 500]])

        member, force, magnitude = compute_largest_member_force(f_all)
        self.assertEqual(member, 'CD')
        self.assertEqual(force, 'F5')
        self.assertAlmostEqual(magnitude, 1750.0, places=2)

    def test_compute_largest_member_force_2(self):

        f_all = np.array([[1200., 600, 0], [700, 100, 200], [100, 1000, 100], [0, 500, 500], 
                  [500, 0, 1500],  [1200, 0, 1000], [1600, -10000, 1800], [0, 0, 1600], [0, 1600, 0], [500, 500, 500]])

        member, force, magnitude = compute_largest_member_force(f_all)
        self.assertEqual(member, 'BC')
        self.assertEqual(force, 'F7')
        self.assertAlmostEqual(magnitude, 10000.0, places=2)
#        
if __name__ == '__main__':
    unittest.main()
