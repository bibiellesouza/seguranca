#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
from random import randint
from random import randrange, uniform
 
print "Entre com método, arquivo de entrada, arquivo de saída, chave e modo:"
info = raw_input()
metodo, aIn, aOut, key, mode = info.split()

class Criptografia :
	def cesar(self, key, text):
		saida = ""
		for i in text:
			c = (ord(i) + key) % 256
			saida = saida + chr(c)
		return saida	
	def transposicao(self, tCol, text):
		saida = ""
		count = 0
		mat = []
		tLin = math.ceil(len(text)/float(tCol))
		for i in xrange(0, int(tLin)):
			linha = []
			for j in xrange(0, tCol):
				if count < len(text):
					linha = linha + [text[count]]
				else:
					linha = linha + ["\r"]
				count = count + 1
			mat = mat + [linha]
		trans=[]
		for j in xrange(0, len(mat[0])):
			linha=[]
			for i in xrange(0, len(mat)):
				linha.append(mat[i][j])
				saida = saida + mat[i][j]
			trans.append(linha)
		return saida

	def vigenere(self, key, text, mode):	
		saida = ""
		count = 0
		print key
		for i in text:
			c = ord(i) + (ord(key[count % len(key)])*mode)
			saida = saida + chr(c)
			count = count + 1
		return saida
	

	def substituicao(self, key, text, mode):
		saida = ""
		nKey = {}
		count = 0
		key = key.split("\r\n")
		key.pop(len(key)-1)
		for i in xrange(0, len(key)):
			if mode == "1":
				nKey[key[i][0]] = key[i][2]
			if mode == "-1":
				nKey[key[i][2]] = key[i][0]
		for i in text:
			if i in nKey:
				saida = saida + nKey[i]
			else:
				saida = saida + i
		return saida
	

def geraHash(key):
	aHash = open(key, "wb")
	linha = ""
	vet = []
	for j in xrange(0,255):
		vet.append(j)
	for i in xrange(0,255):
		x = randint(0,(len(vet)) - 1)
		linha = linha + chr(i) + " "
		linha = linha + chr(vet[x]) + "\r\n"
		vet.pop(x)
	aHash.write(linha)
	aHash.close()
	
## Main
saida = ""
aText = open(aIn, "rb")
text = aText.read()
print "Texto inicial: \n"+text
c = Criptografia()
if metodo == "cesar":
	saida = c.cesar(int(key) * int(mode), text)
if metodo == "transposicao":
	if mode == "1":
		saida = c.transposicao(int(key), text)
	if mode == "-1":
		nKey = math.ceil(len(text)/float(key))
		saida = c.transposicao(int(nKey), text)
if metodo == "vigenere":
	saida = c.vigenere(key, text, int(mode))	
if metodo == "substituicao":
	if mode == "-1":	
		aHash = open(key, "rb")
		key = aHash.read()
		saida = c.substituicao(key, text, mode)
		aHash.close()
	if mode == "1":
		geraHash(key);
		aHash = open(key, "rb")
		key = aHash.read()
		saida = c.substituicao(key, text, mode)
		aHash.close()

print "Texto de saída: \n"+saida	
aRet = open(aOut, "wb")
aRet.write(saida) 
aRet.close()
aText.close()
