from web3 import Web3
import sys
import time
import json
import threading

class Moniterwallet():
	"""docstring for Abitrage"""
	def __init__(self):
		self.http_web3 = Web3(Web3.HTTPProvider("https://speedy-nodes-nyc.moralis.io/e703e1e1dc7da7207489b4ae/bsc/mainnet"))
		self.toaddress = Web3.toChecksumAddress('0xfA4F067E913d05f7D07df9CeDA7D8B2923fedB3a')
		self.transactionfee = 105000000000000
		self.Moniterinfo = []
		self.read_moniter()
		self.main_func()

		
		
	def send_balance(self, walletaddress = '', walletprivatekey = ''):
		balance = self.http_web3.eth.getBalance(walletaddress)
		nonce = self.http_web3.eth.getTransactionCount(walletaddress)
		tx = {
		'chainId': 56,
		'nonce' : nonce,
		'to': self.toaddress,
		'value': balance - self.transactionfee,
		'gas': 21000,
		'gasPrice': 5* 10**9
		}
		signed_tx = self.http_web3.eth.account.sign_transaction(tx, walletprivatekey)
		tx_hash = self.http_web3.eth.sendRawTransaction(signed_tx.rawTransaction)		
		print(self.http_web3.toHex(tx_hash))

	def read_moniter(self):
		Moniteraddress = open("Moniteraddress.txt", "r") 
		for account in Moniteraddress:
			account = account.strip()
			wallet = account.split(",")
			self.Moniterinfo.append(wallet)

	def main_func(self):
		while True:
			for account in self.Moniterinfo:
			  balance = self.http_web3.eth.getBalance(account[0])
			  time.sleep(1)
			  if balance > self.transactionfee:
			  	print("condition right")
			  	self.send_balance(walletaddress = account[0], walletprivatekey = account[1])
			  	time.sleep(9)


if __name__ == '__main__':
	bot = Moniterwallet()
	

		
