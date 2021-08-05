
import configparser
import sys
from api.db.dbStructure import BASE, Project, User
from web3 import Web3
import json


# für Wei umrechnung int(Web3.toWei(0.01, 'ether'))
acc4 = "0x3a954185daaFC35eF1F7aB23D695c2FD4210eb8E" #Empänger Account 0 ETH 
acc1 = "0x2eE0659F4D414a0090174f475CfBf4Fd7bd70DDB" #Erstellt Contract 0.9 ETH
acc1Private = "ab023ad3b1023e85309c8257780741fa58f5781be002d0f5a9c33382ba40afba"
acc2 = "0x54DD30d58a423332C64a180D830e264D8C23a8cF" #der Spendende Account 1 ETH
acc2Private = "e7ef6fa199620acaa0c1b04f6bcbbbb6c22e2c52e9685386427f128eae4c8630"
with open(str("api/data/artifacts/collect.json")) as json_file:
    PROJECT_JSON: dict = json.load(json_file)

CFG_PARSER: configparser.ConfigParser = configparser.ConfigParser()
CFG_PARSER.read("config.ini")


WEB3: Web3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/1ca4dfc921ac4e999a2bd1cfe7de87dc"))


def project_constructor(goal: int, duration: int):
    projects_sc = WEB3.eth.contract(abi=PROJECT_JSON["abi"], bytecode=PROJECT_JSON["data"]["bytecode"]["object"])

    # constructor (address payable _receiver, uint _goal ,uint durationinday)
    
    ctor = projects_sc.constructor(acc4, goal, duration)
    
    tx_hash = ctor.buildTransaction(
                                {
                                    'nonce': WEB3.eth.getTransactionCount(acc1), 
                                    'from': acc1, 
                                    'value': goal, 
                                    'gasPrice': WEB3.toHex(WEB3.toWei('20', 'gwei')),
                                    'gas': 1000000,
                                    'value':0
                                })
    
    signed_tx = WEB3.eth.account.sign_transaction(tx_hash, private_key=acc1Private)
    
    tx_hash = WEB3.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    tx_receipt = WEB3.eth.wait_for_transaction_receipt(tx_hash,timeout=180,poll_latency=0.1) #hier fehler
    print(tx_receipt.contractAddress)
    print(tx_receipt.status)
    if tx_receipt.status != 1:
       raise RuntimeError("SC Call failed!")

    return tx_receipt.contractAddress #Sollte in einem Projekt gespeichert werden vlt in paymentInformationProject
    

def project_donate(project: Project, user_inst: User, amount: int):

    donations_sc = WEB3.eth.contract(project.paymentInformationProject, abi=PROJECT_JSON["abi"]) #vlt wenn möglich nicht hardcode
    
    tx_hash = donations_sc.functions.donate() \
        .buildTransaction(
        {
            'nonce': WEB3.eth.getTransactionCount(user_inst.publickeyUser),
            'from': user_inst.publickeyUser,
            'value': int(amount)
        })
        
    signed_tx = WEB3.eth.account.sign_transaction(tx_hash, private_key=user_inst.privatkeyUser)
    tx_hash2 = WEB3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = WEB3.eth.waitForTransactionReceipt(tx_hash2)


'''
def project_cashout(project: Project):

    donations_sc = WEB3.eth.contract([...],'0x2eE0659F4D414a0090174f475CfBf4Fd7bd70DDB') #vlt wenn möglich nicht hardcode

    tx_hash = donations_sc.functions.donate() \
        .buildTransaction(
        {
            'nonce': WEB3.eth.getTransactionCount(user_inst.publickeyUser),
            'from': user_inst.publickeyUser,
        })
    signed_tx = WEB3.eth.account.sign_transaction(tx_hash, private_key=user_inst.privatekeyUser)
    tx_hash2 = WEB3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = WEB3.eth.waitForTransactionReceipt(tx_hash2)
'''
