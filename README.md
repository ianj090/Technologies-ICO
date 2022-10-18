# Technologies and Freedom - Lab ICO - CoralineToken (COR)
#### Ian Jenatz 20190014

<br>

## Description
This project contains a flask application which controls a simple html page for an Initial Coin Offering. The Token was created on the Ethereum test network Goerli and can be searched on websites such as etherscan.io. The token is called Coraline Token after the movie and as such the HTML follows the same theme. Users can enter their Metamask Wallet address, their private key to approve the transaction, and how many tokens they want to purchase. Any approved transactions (only if they have the required amount of Ethereum on the Goerli test network) can be seen in etherscan with the link below.

<br>

Link to Contract Address (To see any purchases):
https://goerli.etherscan.io/address/0x8c218e3ce341d04cc9a59fa61e8cc442a99a9109 

## How to run
Running this project is very simple, all you need to do is run `python app.py` in a terminal to lift the application. The requirements must be met first. 

1. Run `pip install flask` and run `pip install web3` to meet the requirements.
2. Run `python app.py` in a terminal.
2. Access the frontend at: `http://127.0.0.1:5000/`
