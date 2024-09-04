#!/usr/bin/env python

# Copyright 2018-2021 John T. Foster
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
from numpy.testing import assert_array_almost_equal

with open("assignment3.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment3.py", "w") as f:
    f.write(python_file)


from assignment3 import (water_rel_perm,
                         add_well_activity,
                         add_well_activity_from_file,
                         get_bhp_well_values,
                         get_bhp_well_values_from_file)


class TestSolution(unittest.TestCase):

    def test_water_rel_perm(self):
        assert_array_almost_equal(water_rel_perm(0.6, 0.2, 0.2, 3),
                                  (0.0, 0.07499999999999994, 0.6), decimal=1)


    def test_add_well_activity(self):

        well_list1 = add_well_activity([['well1', 'producing', '0']],
                                       'well2', 'shut-in', '100')
        well_list2 = add_well_activity(well_list1, 'well3', 'injecting', '10')

        assert well_list2 == [['well1', 'producing', '0'],
                              ['well3', 'injecting', '10'],
                              ['well2', 'shut-in', '100']]


    def test_add_well_activity_from_file(self):

        well_list = add_well_activity_from_file('well_activity.csv', 'well4',
                                                'injecting', '1000')

        assert well_list == [['well1', 'producing', '0'],
                             ['well2', 'shut-in', '0'],
                             ['well3', 'shut-in', '0'],
                             ['well4', 'injecting', '1000'],
                             ['well2', 'injecting', '2000'],
                             ['well3', 'producing', '3000'],
                             ['well1', 'injecting', '3000'],
                             ['well1', 'shut-in', '7000'],
                             ['well2', 'shut-in', '7000'],
                             ['well3', 'shut-in', '7000']]


        def test_get_bhp_well_values(self):

            assert (abs(get_bhp_well_values({'wells': {'bhp':
                                            {'values': 10.0}}}) - 10.0)
                    < 1e-6)

        def test_get_bhp_well_values_from_file(self):

            assert_array_almost_equal(
                    get_bhp_well_values_from_file('wells.yml'),
                    [2200.0, 2000.0], decimal=1)


if __name__ == '__main__':
    unittest.main()
