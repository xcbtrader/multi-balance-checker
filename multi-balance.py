__author__ = 'xcbtrader'
# -*- coding: utf-8 -*-

import requests
import json
import time

def abrir_fichero():
	global direcciones
	f = input('Nombre del fichero con las direcciones:? ')
	try:
		fit = open(f, 'r')
		direcciones = []
		a = fit.readline()
		while a != "":
			a = a[0 :-1]
			direcciones.append(a)
			a = fit.readline()
		fit.close()
		print ('>> CARGADO FICHERO CON ' + str(len(direcciones)) + ' DIRECCIONES')
	except:
		print ('### ERROR FICHERO NO EXISTENTE ###')

def b1(addr):
	try:
		request = 'https://blockchain.info/q/addressbalance/' + addr
		response = requests.get(request, timeout=10)
		content = int(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b2(addr):
	try:
		request = 'http://btc.blockr.io/api/v1/address/info/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['data'] ['balance'] * 100000000)
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b3(addr):
	try:
		request = 'https://bitcoin.toshi.io/api/v0/addresses/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = content['balance']
		return content
	except KeyboardInterrupt:
		exit()
	except:
		if 'response' in locals():
			if response.status_code == 404:
				return 0
			else:
				return -1
		else:
			return -1
			
def b4(addr):
	try:
		request = 'https://blockexplorer.com/api/addr/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balanceSat'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b5(addr):
	try:
		request = 'https://chain.api.btc.com/v3/address/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = content['balance']
		return content
	except KeyboardInterrupt:
		exit()
	except:
		if 'response' in locals():
			if response.status_code == 200:
				return 0
			else:
				return -1
		else:
			return -1

def b6(addr):
	try:
		request = 'https://www.bitgo.com/api/v1/address/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['confirmedBalance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b7(addr):
	try:
		request = 'https://api.blocktrail.com/v1/btc/address/' + addr + '?api_key=MY_APIKEY'
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b8(addr):
	try:
		request = 'https://api.blockcypher.com/v1/btc/main/addrs/' + addr + '/balance'
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b9(addr):
	try:
		request = 'https://bitcoin.toshi.io/api/v0/addresses/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except:
		if 'response' in locals():
			if response.status_code == 404:
				return 0
			else:
				return -1
		else:
			return -1

def b10(addr):
	try:
		request = 'https://api.kaiko.com/v1/addresses/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['total']['balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b11(addr):
	try:
		request = 'https://chainflyer.bitflyer.jp/v1/address/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['confirmed_balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b12(addr):
	try:
		request = 'https://insight.bitpay.com/api/addr/' + addr + '/?noTxList=1'
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balanceSat'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b13(addr):
	try:
		request = 'https://api.coinprism.com/v1/addresses/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b14(addr):
	try:
		request = 'https://www.blockonomics.co/api/balance' 
		response = requests.post(request, data=json.dumps({"addr":addr}), timeout=10)
		content = response.json()
		content = int(content['response'][0]['confirmed'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

global direcciones

n = 1
naddr = 0
pausa = 0.2
nerror = 0
abrir_fichero()

while naddr<= len(direcciones):
	if n == 1:
		saldo = b1(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b1')
			time.sleep(pausa)
			n = 2
			naddr +=1
			nerror = 0
		else:
			n = 2
			nerror += 1
	elif n == 2:
		saldo = b2(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b2')
			time.sleep(pausa)
			n = 3
			naddr +=1
			nerror = 0
		else:
			n = 3
			nerror += 1
	elif n == 3:
		saldo = b3(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b3')
			time.sleep(pausa)
			n = 4
			naddr +=1
			nerror = 0
		else:
			n = 4
			nerror += 1
	elif n == 4:
		saldo = b4(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b4')
			time.sleep(pausa)
			n = 5
			naddr +=1
			nerror = 0
		else:
			n = 5
			nerror += 1
	elif n == 5:
		saldo = b5(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b5')
			time.sleep(pausa)
			n = 6
			naddr +=1
			nerror = 0
		else:
			n = 6
			nerror += 1
	elif n == 6:
		saldo = b6(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b6')
			time.sleep(pausa)
			n = 7
			naddr +=1
			nerror = 0
		else:
			n = 7
			nerror += 1
	elif n == 7:
		saldo = b7(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b7')
			time.sleep(pausa)
			n = 8
			naddr +=1
			nerror = 0
		else:
			n = 8
			nerror += 1
	elif n == 8:
		saldo = b8(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b8')
			time.sleep(pausa)
			n = 9
			naddr +=1
			nerror = 0
		else:
			n = 9
			nerror += 1
	elif n == 9:
		saldo = b9(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b9')
			time.sleep(pausa)
			n = 10
			naddr +=1
			nerror = 0
		else:
			n = 10
			nerror += 1
	elif n == 10:
		saldo = b10(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b10')
			time.sleep(pausa)
			n = 11
			naddr +=1
			nerror = 0
		else:
			n = 11
			nerror += 1
	elif n == 11:
		saldo = b11(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b11')
			time.sleep(pausa)
			n = 12
			naddr +=1
			nerror = 0
		else:
			n = 12
			nerror += 1
	elif n == 12:
		saldo = b12(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b12')
			time.sleep(pausa)
			n = 13
			naddr +=1
			nerror = 0
		else:
			n = 13
			nerror += 1
	elif n == 13:
		saldo = b13(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b13')
			time.sleep(pausa)
			n = 14
			naddr +=1
			nerror = 0
		else:
			n = 14
			nerror += 1
	elif n == 14:
		saldo = b14(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b14')
			time.sleep(pausa)
			n = 1
			naddr +=1
			nerror = 0
		else:
			n = 1
			nerror += 1
	if nerror > 14:
		exit()
	
