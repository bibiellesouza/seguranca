#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
from random import randint
from random import randrange, uniform
 
print "Entre com método e o nome do arquivo:"
info = raw_input()
metodo, aIn = info.split()

def verificaTrans(tCol, text):
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

def compara(tDeci, saida):
	porcent = 0
	for i in xrange(0, len(tDeci)):
		try:
			if tDeci[i] == saida[i]:
				porcent = porcent + 1
		except IndexError:
			break
	porcent = float(porcent) / len(tDeci)
	porcent = porcent * 100
	return porcent 
	

class Decifra :
	def cesar(self, tEncri, tDeci):
		if len(tEncri) > 0:
			chave  = ord(tDeci[0]) - ord(tEncri[0])
			return chave
	def substituicao(self, tEncri, tDeci):
		saida = {}
		for i in xrange(0, len(tEncri)):
			saida[tEncri[i]] = tDeci[i]
		return saida
	def vigenere(self, tEncri, tDeci):
		chave = ""
		for i in xrange(0, len(tEncri)):
			c = ord(tDeci[i]) - ord(tEncri[i])
			chave = chave + chr(c)		
		return chave
	def transposicao(self, tEncri, tDeci):
		chave = 1
		while 1:
			saida = verificaTrans(int(chave), tEncri)
			if compara(tDeci, saida) >= 90:
				break
			chave = chave + 1
		return chave
		
## Main
saida = 0
encri = open("arquivos/inputs/"+aIn, "rb")
tEncri = encri.read()
deci = open("arquivos/outputs/"+aIn, "rb")
tDeci = deci.read()
d = Decifra()
if metodo == "cesar":
	saida = d.cesar(tEncri, tDeci)
if metodo == "transposicao":
	saida = d.transposicao(tEncri, tDeci)
if metodo == "vigenere":
	saida = d.vigenere(tEncri, tDeci)	
if metodo == "substituicao":
	saida = d.substituicao(tEncri, tDeci)
print "Chave encontrada: "
print saida
encri.close()
deci.close()
