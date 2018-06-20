import pygame
import time, sys
from pygame.locals import *
pygame.init()
from pygame.locals import *
pygame.init()
import socket
print " \n Servidor_@! " 
print " \n Radio Eduarda e Herick _UFC_@ :)\n"
								 	
HOST = ''
PORT = 3999

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Escutando a porta..."
s.bind((HOST,PORT))
s.listen(5)
print "Aceitando a conexao..."

tempoAtualMusica = time.time()
tempoinicio = time.time()

musica = 1

while 1:	
	
	tempoAtualMusica = time.time()
	if musica < 4 and (tempoinicio+01.0) < tempoAtualMusica:
		musica += 1
		tempoinicio = time.time()
	else:		
		musica=1
		tempoinicio = time.time()
	
	conn,addr= s.accept()
	print 'endereco ip:', addr
	arq=open('music'+ str(musica) +'.mp3','rb')
	
	print "enviando music"+ str(musica)
	print tempoinicio + 03.0, tempoinicio, tempoAtualMusica
	for i in arq:
			conn.send(i)

 
	print "saindo..."
	arq.close()
	conn.close()
