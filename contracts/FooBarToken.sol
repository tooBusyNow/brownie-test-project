// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "node_modules/@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "node_modules/@openzeppelin/contracts/access/Ownable.sol";

contract FooBaseToken is ERC20, Ownable {

    event UnrecognizableCall(string);

    constructor (uint256 startAmount) ERC20('FooBaseToken', 'FBT') {
        _mint(msg.sender, startAmount);
    }

    function destruct () external onlyOwner {
        selfdestruct(payable(msg.sender));
    }

    function mint (uint256 amount, address account) onlyOwner external {
        _mint(account, amount);
    }

    function burn (uint256 amount, address account) onlyOwner external {
        _burn(account, amount);
    }

    fallback() external {
        emit UnrecognizableCall('Caused unexpected behaviour');
    }
}