# This file is part of Maker Keeper Framework.
#
# Copyright (C) 2017-2018 reverendus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from web3 import Web3, EthereumTesterProvider

from pymaker import Address
from pymaker.auctions import Flipper, Flapper, Flopper
from pymaker.token import DSToken


class TestFlipper:
    def setup_method(self):
        self.web3 = Web3(EthereumTesterProvider())
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.our_address = Address(self.web3.eth.defaultAccount)
        self.pie = DSToken.deploy(self.web3, 'DAI')
        self.gem = DSToken.deploy(self.web3, 'REP')
        self.flipper = Flipper.deploy(self.web3, self.our_address, 111, self.pie.address, self.gem.address)

    def test_pie(self):
        assert self.flipper.pie() == self.pie.address

    def test_gem(self):
        assert self.flipper.gem() == self.gem.address


class TestFlapper:
    def setup_method(self):
        self.web3 = Web3(EthereumTesterProvider())
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.our_address = Address(self.web3.eth.defaultAccount)
        self.pie = DSToken.deploy(self.web3, 'DAI')
        self.gem = DSToken.deploy(self.web3, 'MKR')
        self.flapper = Flapper.deploy(self.web3, self.pie.address, self.gem.address)

    def test_pie(self):
        assert self.flapper.pie() == self.pie.address

    def test_gem(self):
        assert self.flapper.gem() == self.gem.address


class TestFlopper:
    def setup_method(self):
        self.web3 = Web3(EthereumTesterProvider())
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.our_address = Address(self.web3.eth.defaultAccount)
        self.pie = DSToken.deploy(self.web3, 'DAI')
        self.gem = DSToken.deploy(self.web3, 'MKR')
        self.flopper = Flopper.deploy(self.web3, self.pie.address, self.gem.address)

    def test_pie(self):
        assert self.flopper.pie() == self.pie.address

    def test_gem(self):
        assert self.flopper.gem() == self.gem.address
