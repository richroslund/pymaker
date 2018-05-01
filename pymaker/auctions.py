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

from web3 import Web3

from pymaker import Contract, Address, Transact


class Flapper(Contract):
    """A client for the `Flapper` contract, TODO.

    You can find the source code of the `Flapper` contract here:
    <TODO>.

    Attributes:
        web3: An instance of `Web` from `web3.py`.
        address: Ethereum address of the `Flapper` contract.
    """

    abi = Contract._load_abi(__name__, 'abi/Flapper.abi')
    bin = Contract._load_bin(__name__, 'abi/Flapper.bin')

    @staticmethod
    def deploy(web3: Web3, pie: Address, gem: Address):
        assert(isinstance(pie, Address))
        assert(isinstance(gem, Address))

        return Flapper(web3=web3, address=Contract._deploy(web3, Flapper.abi, Flapper.bin, [pie.address, gem.address]))

    def __init__(self, web3: Web3, address: Address):
        assert(isinstance(web3, Web3))
        assert(isinstance(address, Address))

        self.web3 = web3
        self.address = address
        self._contract = self._get_contract(web3, self.abi, address)

    def pie(self) -> Address:
        """Returns the `pie` token.

        Returns:
            The address of the `pie` token.
        """
        return Address(self._contract.call().pie())

    def gem(self) -> Address:
        """Returns the `gem` token.

        Returns:
            The address of the `gem` token.
        """
        return Address(self._contract.call().gem())

    def __repr__(self):
        return f"Flapper('{self.address}')"


class Flopper(Contract):
    """A client for the `Flopper` contract, TODO.

    You can find the source code of the `Flopper` contract here:
    <TODO>.

    Attributes:
        web3: An instance of `Web` from `web3.py`.
        address: Ethereum address of the `Flopper` contract.
    """

    abi = Contract._load_abi(__name__, 'abi/Flopper.abi')
    bin = Contract._load_bin(__name__, 'abi/Flopper.bin')

    @staticmethod
    def deploy(web3: Web3, pie: Address, gem: Address):
        assert(isinstance(pie, Address))
        assert(isinstance(gem, Address))

        return Flapper(web3=web3, address=Contract._deploy(web3, Flopper.abi, Flopper.bin, [pie.address, gem.address]))

    def __init__(self, web3: Web3, address: Address):
        assert(isinstance(web3, Web3))
        assert(isinstance(address, Address))

        self.web3 = web3
        self.address = address
        self._contract = self._get_contract(web3, self.abi, address)

    def pie(self) -> Address:
        """Returns the `pie` token.

        Returns:
            The address of the `pie` token.
        """
        return Address(self._contract.call().pie())

    def gem(self) -> Address:
        """Returns the `gem` token.

        Returns:
            The address of the `gem` token.
        """
        return Address(self._contract.call().gem())

    def __repr__(self):
        return f"Flopper('{self.address}')"
