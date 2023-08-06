"""da pra melhorar muuuuita coisa, especialmente nas mensagens
exibidas. mas mo preguiça.
vim do futuro e melhorei um pouco(quase nada ;-;)"""

def matriz_nula(lin, col):
	matriz = [[0]]*lin
	
	for i in range(lin):
		linha = [0]*col
		matriz[i] = linha
	return matriz

def gab(quests, alts):
	M = matriz_nula(quests, alts)
	questoes = len(M)
	
	for i in range(questoes):
		aux = input(f"Digite a letra correta da questão número {i+1}: ")
		if aux == "A":
			M[i][0] = "x"
		elif aux == "B":
			M[i][1] = "x"
		elif aux == "C":
			M[i][2] = "x"
		elif aux =="D":
			M[i][3] = "x"
		else:
			M[i][4] = "x"
	return M

def cart_resp(quests, alts, aluno):
	prova = matriz_nula(quests,alts)
	
	for i in range(len(prova)):
		aux = input(f"Digite a resposta da questão {i+1} do aluno(a) {aluno}: ")
		
		if aux == "A" or "a":
			prova[i][0] = "x"
		elif aux == "B" or "b":
			prova[i][1] = "x"
		elif aux == "C" or "c":
			prova[i][2] = "x"
		elif aux == "D" or "d":
			prova[i][3] = "x"
		else:
			prova[i][4] = "x"
	return prova

def correcao(gabarito, prova):
	acertos = 0
	
	for i in range(len(gabarito)):
		if gabarito[i] == prova[i]:
			acertos += 1
	return acertos

questoes = int(input("Informe a quantidade de questões da prova:\n"))
alternativas = int(input("Informe quantas alternativas cada questão possui:\n"))

gabarito = gab(questoes, alternativas)

quant_alunos = int(input("\nInforme quantos alunos realizarão a prova: "))

nomes = [0]*quant_alunos
notas = [0]*quant_alunos

for i in range(quant_alunos):
		aux = input("\nDigite o nome do(a) aluno(a): ")
		nomes[i] = aux
		p = cart_resp(questoes, alternativas,aux)
		nota = correcao(gabarito,p)
		notas[i] = nota
		#print(f"O(A) aluno(a) {aux} acertou {nota} questões.")

for j in range(len(notas)):
	print(f"O(A) aluno(a) {nomes[j]} acertou {notas[j]} questões.")