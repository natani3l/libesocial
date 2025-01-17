# Copyright 2018, Qualita Seguranca e Saude Ocupacional. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from esocial import utils


def test_format_xsd_version():
    versions = ['2.5.0', '1.1.1', 'S-1.0', 'S-1.2']
    expected = ['2_5_0', '1_1_1', 'S_1_0', 'S_1_2']
    for i, v in enumerate(versions):
        xsd_version = utils.format_xsd_version(v)
        assert  xsd_version == expected[i], 'Expetected [{}], Got [{}]'.format(expected[i], xsd_version)

