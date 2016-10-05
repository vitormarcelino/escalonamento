# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import json #IMPORTA O JSON PARA ESCREVER AS SAÍDAS NO GRÁFICO DO JS NO HTML
import webbrowser #IMPORTA O WEBBROWSER PARA ABRIR A PAGINA DO GRÁFICO COM O NAVEGADOR PADRÃO

#FUNÇÃO DO ALGORITMO FIFO
def fifo ():
	entradas = list(tmpEnt)
	tempos = list(tmpExe)
	for j in range(0,n): #ORDENA COM BASE NAS ENTRADAS (DA MENOR PARA A MAIOR)
		for i in range(0,n-1):
			if entradas[i]>entradas[i+1]:
				Aux = entradas[i+1] #TROCA A ENTRADA
				entradas[i+1] = entradas[i]
				entradas[i] = Aux
				Aux = tempos[i+1] #TROCA O TEMPO
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
	soma = 0
	relogio = 0
	for x in xrange(0,n):
		relogio += tempos[x] #INCREMENTA O RELOGIO COM O TEMPO DE EXECUÇÃO DO PROCESSO
		soma += relogio - entradas[x] #INCREMENTA A SOMA COM O TEMPO FINAL DO PROCESSO (RELOGIO) - O TEMPO DE ENTRADA
		pass
	return float(soma/n);

#FUNÇÃO DO ALGORITMO SJF
def sjf ():
	entradas = list(tmpEnt)
	tempos = list(tmpExe)
	for j in range(0,n): #ORDENA AS OS TEMPOS COM BASE NO TEMPO DE PROCESSO (DO MENOR PARA O MAIOR)
		for i in range(0,n-1):
			if tempos[i]>tempos[i+1]: 
				Aux = tempos[i+1] 	#TROCA O TEMPO
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
				Aux = entradas[i+1] #TROCA A ENTRADA
				entradas[i+1] = entradas[i]
				entradas[i] = Aux	
	soma = 0
	relogio = 0
	for x in xrange(0,n):
		for y in xrange(0,n):
			if entradas[y] <= relogio and entradas[y]>=0:
				escolhido = y
				break
			pass
		relogio += tempos[escolhido] #INCREMENTA O RELOGIO COM O TEMPO DE EXECUÇÃO DO PROCESSO
		soma += relogio - entradas[escolhido]
		entradas[escolhido]=-1
	return float(soma/n);

#FUNÇÃO DO ALGORITMO ROUND ROBIN
def rr ():
	entradas = list(tmpEnt) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(tmpExe) # MESMA IDEIA DE CIMA
	relogio = 0 
	processados = [0]*n  #CRIAMOS UMA LISTA ONDE A CADA EXECUÇÃO IREMOS INCREMENTAR O TEMPO QUE FOI EXECUTADO
	entraram = [0]*n  #CRIAMOS UMA LISTA DE 0/1 PARA SABER QUAIS PROCESSOS JA ENTRAM
	fila = [] #CRIAMOS UMA FILA, QUE IRÁ DETERMINAR QUAIS OS PROXIMOS PROCESSOS IRÃO EXECUTAR
	count = 0 
	soma = 0
	def entra():
		for x in xrange(0,n): #ADICIONA OS TEMPOS QUE NÃO ENTRARAM E MENORES OU IGUAL AO RELOGIO NA FILA
			if entradas[x] <= relogio and entraram[x] == 0:
				#print "Entrou ", x
				entraram[x] = 1  # OS PROCESSOS QUE JÁ ENTRARAM, RECEBEM 1, ASSIM SÓ ENTRAM NOVAMENTE NA FILA EM CASO DE PREEPÇÃO
				fila.append(x)  #O PROCESSO É ADICIONADO AO FIM DA FILA
			pass
	entra()
	for processo in fila:
		#print "=====", processo, "======"
		falta = tempos[processo]-processados[processo]  #VARIÁVEL FALTA RECEBE O TEMPO DO PROCESSO - O QUE JÁ FOI PROCESSADO
		if falta > quantum: #SE FALTA MAIS QUE O QUANTUM ENTRA NO BLOCO
			relogio+=quantum  #RELOGIO INCREMENTA O QUANTUM, POIS IRÁ EXECUTAR TODO O TEMPO DO QUANTUM
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=quantum #INCREMENTA EM UM QUANTUM O QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			#print "Executou ", processo, " até ", relogio
			#print "Sobrecarga até ", relogio+1
			#print processo, " foi pro fim da fila"
			fila.append(processo) #COMO O PROCESSO NÃO FOI EXECUTADO TOTALMENTE, ELE VOLTA PARA O FIM DA FILA DE EXECUÇÃO
			relogio+=1 #ADIOCIONA AO RELOGIO O TEMPO DA SOBRECARGA
		elif falta <= quantum and falta > 0: #NESSE CASO VERIFICAMOS SE FALTA ALGUM TEMPO ENTRE 0 E O QUANTUM A SER EXECUTADO
			relogio+=falta #INCREMENTA O RELÓGIO O TEMPO QUE FALTA
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=falta #INCREMENTA O QUE FALTA AO QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			soma+=relogio-entradas[processo] #INCREMENTA A SOMA COM O TURNAROUND DO PROCESSO
	return float(soma/n) #RETORNA A MEDIA DOS TURNAROUND

#FUNÇÃO DO ALGORITMO EDF
def edf():
	entradas = list(tmpEnt) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(tmpExe) # MESMA IDEIA DE CIMA
	relogio = 0 
	processados = [0]*n  #CRIAMOS UMA LISTA ONDE A CADA EXECUÇÃO IREMOS INCREMENTAR O TEMPO QUE FOI EXECUTADO
	entraram = [0]*n  #CRIAMOS UMA LISTA DE 0/1 PARA SABER QUAIS PROCESSOS JA ENTRAM
	count = 0 
	soma = 0
	def entra():
		for x in xrange(0,n): #ADICIONA OS TEMPOS QUE NÃO ENTRARAM E MENORES OU IGUAL AO RELOGIO
			if entradas[x] <= relogio and entraram[x] == 0:
				#print "Entrou ", x
				entraram[x] = 1  # OS PROCESSOS QUE JÁ ENTRARAM, RECEBEM 1
			pass
	entra()
	def buscaMenorDeadline():
		menorDeadline = 1000
		escolhido = -1
		for x in xrange(0,n):
			#PARA UM PROCESSO SER ESCOLHIDO ELE PRECISA: 1) TER CHEGADO, 2) TER A MENOR DEADLINE, 3) NÃO TER SIDO FINALIZADO
			if entraram[x] == 1 and deadlines[x] < menorDeadline and processados[x] < tempos[x]:
				menorDeadline = deadlines[x]
				escolhido = x
			pass
		return escolhido

	while buscaMenorDeadline() != -1:
		processo = buscaMenorDeadline()
		falta = tempos[processo]-processados[processo]  #VARIÁVEL FALTA RECEBE O TEMPO DO PROCESSO - O QUE JÁ FOI PROCESSADO
		if falta > quantum: #SE FALTA MAIS QUE O QUANTUM ENTRA NO BLOCO
			relogio+=quantum  #RELOGIO INCREMENTA O QUANTUM, POIS IRÁ EXECUTAR TODO O TEMPO DO QUANTUM
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=quantum #INCREMENTA EM UM QUANTUM O QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			#print "Executou ", processo, " até ", relogio
			#print "Sobrecarga até ", relogio+1
			relogio+=1 #ADIOCIONA AO RELOGIO O TEMPO DA SOBRECARGA
		elif falta <= quantum and falta > 0: #NESSE CASO VERIFICAMOS SE FALTA ALGUM TEMPO ENTRE 0 E O QUANTUM A SER EXECUTADO
			relogio+=falta #INCREMENTA O RELÓGIO O TEMPO QUE FALTA
			#print "Executou ", processo, " até ", relogio
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=falta #INCREMENTA O QUE FALTA AO QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			soma+=relogio-entradas[processo] #INCREMENTA A SOMA COM O TURNAROUND DO PROCESSO

	return float(soma/n) #RETORNA A MEDIA DOS TURNAROUND

#LEITURA DAS DEADLINES
def lerDeadlines():
	del deadlines[:] #ZERA A LISTA DE DEADLINES PARA A NOVA LEITURA
	for x in xrange(0,n):
		print "Informe a Deadline do processo ", x+1, ": "
		deadlines.append(input())
		pass

#LÊ A QUANTIDADE DE PROCESSOS E CRIA AS LISTAS DE TEMPO DE EXECUÇÃO E TEMPO DE ENTRADA PARA CADA PROCESSO
n = int(input ("Informe o numero de processos: "))
tmpExe = []
tmpEnt = []
deadlines = []

#LÊ OS TEMPOS DE EXECUÇÃO E DE ENTRADA PARA CADA PROCESSO
for x in xrange(1,n+1):
	print "Tempo de entrada do processo ", x, ": "
	tmpEnt.append(float(input()))
	print "Tempo de execução do processo ", x, ": "
	tmpExe.append(float(input()))

#SOLICITA AO USUARIO QUE INFORME O ALGORITMO DE ESCALONAMENTO DESEJADO
def menu():
	print "Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) SJF\n (3) Round Robin (Preemptivo)\n (4) EDF (Preemptivo)\n (5) Gerar Gráfico\n (0) Sair"

menu()
cmd = input ("Escolha: ")
#ENQUANDO A ESCOLHA FOR DIFERENTE DE 0, EXECUTA O RESPECTIVO ALGORITMO, OU RETORNA COMANDO INVALIDO
while cmd != 0:
	if cmd == 1:
		print "============ FIFO ============"
		print "TURNAROUND MEDIO: ", fifo()
		print "=============================="
		pass
	elif cmd == 2:
		print "============ SJF ============="
		print "TURNAROUND MEDIO: ", sjf()
		print "=============================="
		pass
	elif cmd == 3:
		quantum = float(input("Insira o valor do quantum: "))
		print "========= ROUND ROBIN ========"
		print "TURNAROUND MEDIO: ", rr()
		print "=============================="
		pass
	elif cmd == 4:
		quantum = float(input("Insira o valor do quantum: "))
		lerDeadlines()
		print "============ EDF ============="
		print "TURNAROUND MEDIO: ", edf()
		print "=============================="
		pass
	elif cmd == 5:
		quantum = float(input("Insira o valor do quantum: "))
		lerDeadlines()
		arquivo = open('resultados.json', 'w')
		saida = {'labels': ["FIFO", "SJF", "Round Robin", "EDF"],'datasets': [{'data': [fifo(), sjf(), rr(), edf()]}]}
		json.dump(saida, arquivo, indent=4)
		arquivo.close()
		webbrowser.open_new_tab("grafico.html")
		pass
	else:
		print "Comando Inválido"
		pass
	menu()
	cmd = input ("Escolha: ")