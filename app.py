from flask import Flask, render_template, request, flash
from web3 import Web3

DEBUG = True # debug flag to print error information
SECRET_KEY = 'e68f24d3f205cdc28ab9ef8e' # Used for flask flash

app = Flask(__name__)
app.config.from_object(__name__) # loads workspace values

web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/9fd28f1720854a338e23aae0d1fe8b72'))

contract = '0x8c218E3CE341d04cc9A59Fa61e8cc442A99A9109'

@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        account = request.form["account"]
        privateKey = request.form["privateKey"]
        amount = request.form["amount"]

        try:
            nonce = web3.eth.getTransactionCount(account)

            gasVal = web3.eth.estimateGas({
                "from"      : account,       
                "nonce"     : nonce, 
                "to"        : contract,     
                "value"      : web3.toWei(amount,'ether')
            })
            print(gasVal)
            
            tx = {
                'nonce': nonce,
                'to' : contract,
                'value': web3.toWei(amount,'ether'),
                'gas': gasVal+100,
                'gasPrice': web3.toWei(40,'gwei')
            }

            signed_tx = web3.eth.account.sign_transaction(tx, privateKey)
            tx_transaction = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(tx_transaction)
            flash("Operation completed")
        except:
            flash("Error, please try again")
    return render_template('main.html')

if __name__ == '__main__':
    app.run()

# Account = 0x42fAF6Ebc269A7648307c34722Ea782F1aF51333
# Private Key = fb9fd945f75060d2cc2149dcfeeb797c9f39efc06d1de11fdfd1dd935eb03824
# Amount = 5
