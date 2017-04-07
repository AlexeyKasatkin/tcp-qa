#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tcp_tests.managers.execute_commands import ExecuteCommandsMixin


class OpenstackManager(ExecuteCommandsMixin):
    """docstring for OpenstackManager"""

    _config = None
    _underlay = None

    def __init__(self, config, underlay, salt):
        self._config = config
        self._underlay = underlay
        self._salt = salt
        super(OpenstackManager, self).__init__()

    def install(self, commands):
        self.execute_commands(commands,
                              label='Install OpenStack services')
        self._config.common_services.common_services_installed = True
