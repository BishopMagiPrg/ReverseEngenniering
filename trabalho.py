import random
import time

#Criação da função insertionSort
def insertionSort(A):
	#O loop for começa no segundo elemento (indice 1) até o último elemento da string porque consideramos que o primeiro elemento está ordenado 
	for j in range(1, len(A)):
		#para cada elemento da string armazena em lista
		lista = A[j]
		#A variável i inicia na possição anterior à j (porque iniciamos na segunda posição)
		i = j-1
		#enquanto o primeira posição for maior ou igual a zero e o valor dessa possição for maior que o valor da lista
		while i >= 0 and A[i] > lista: 
			#o valor da possição é copiado para a posição seguinte (guarda em cima do valor mais baixo mas esse valor está na lista)
			A[i+1] = A[i]
			#voltamos a possição um passo para trás (atenção se o i for 0 estiver na primeira posição após o decremento fica a -1)
			i = i-1
		#copiamos o valor que estava guardano na lista (o que perdeu o valor) para o primeiro lugar da comparação, posição do i antes do while
		A[i+1] = lista
	return A

#Criação da função bubbleSort
def bubbleSort(A):
	#contagem do comprimento da lista
	x = len(A)
	# corre todos os indices até ao final que é x
	for i in range(x):
		# o valor de j começa com 0 e vai até ao penúltimo
		for j in range(0, x - i - 1):
			# verifica se o valor da posição do array onde está é maior que a próxima possição do mesmo array
			if A[j] > A[j + 1]:
				# troca as posições do array um pelo outro
				A[j], A[j + 1] = A[j + 1], A[j]
	return A

#Criação da função mergeSort
def mergeSort(A):
	# Verifica se a lista possui mais que um elemento, se tiver um elemento a lista encontra-se ordenada
	if len(A) > 1:
		#  Divide a lista (array) em duas partes iguais
		metade = len(A) // 2
		# A primeira metade coloca na variável A_esq (esquerda)
		A_esq = A[:metade]
		# A outra metade coloca na variável A_dir (direita)
		A_dir = A[metade:]
		# É novamente chamada a função mas só corre a A_esq, entra no ciclo if de novo até ficar com 1 elemento 
		mergeSort(A_esq)
		# Exatamente o mesmo mas com a parte direita
		mergeSort(A_dir)
		# criação das variáveis i, j e t com o valor de 0 para cada uma delas
		i = j = t = 0
		# Aqui verifica a existência das duas listas, verificando o valor de cada variável (i e j) sendo inferior a cada uma das partes
		while i < len(A_esq) and j < len(A_dir):
			# Aqui verifica se qual a parte menor
			if A_esq[i] < A_dir[j]:
				# aqui vai guardar o valor da parte esquerda na posição t da variável A
				A[t] = A_esq[i]
				# aqui incrementamos a variável i
				i += 1
			else:
				# aqui guardamos a parte direita na posição t da variável A
				A[t] = A_dir[j]
				# incrementamos a variável j
				j += 1
			# incrementamos a variável t
			t += 1
		# Aqui verifica a existência da lista da esquerda (A_esq)
		while i < len(A_esq):
			# guarda a parte da esquerda na posição t da variável A
			A[t] = A_esq[i]
			# incrementa a variável i
			i += 1
			# incrementa a variável t
			t += 1
		# Aqui verifica a existência da lista da direita (A_dir)
		while j < len(A_dir):
			# guarda a parte direita na posição t da variável A
			A[t] = A_dir[j]
			# incrementa a variável j
			j += 1
			# incrementa a variável t
			t += 1
	return A, tempo

# Criação da função Quick Sort
def quickSort(A):
	# Verificação se a lista tem mais que 1 elemento
	if len(A) <= 1:
		return A
	else:
		# Atribuição do pivot ao primeiro elemento da lista
		pivo = A[0]
		# colocação dos numeros menores que pivot para menos
		menos = [i for i in A[1:] if i <= pivo]
		# colocação dos numeros maiores que pivot para mais
		mais = [i for i in A[1:] if i > pivo]
		# o pivot é adicionado à lista de saída e o return faz voltar a repetir a função para os menores do pivot e outra repetição dos maiores
		# por cada vez que qualquer das listas reenicia o pivot fica na sua posição correcta
		# por cada vez que reeniciar a função é adicionado um pivot na posição correcta
		# quando acabar é retornado a lista total dos pivo ordenados
		return quickSort(menos) + [pivo] + quickSort(mais)

#criação da lista aleatória
def ale(tmin, tmax, vmin, vmax):
	t = random.randint(tmin, tmax)
	return [random.randint(vmin, vmax) for _ in range(t)]

# Quadro de tamanhos:
# tamanho mínimo do array
tmin = 1
# tamanho máximo do array
tmax = 20
# valor mínimo de cada elemento
vmin = -100
# valor máximo de cada elemento
vmax = 100

# Este conjunto vai gerar aleatóriamente uma lista e coloca para cada l esta mesma lista (l1, l2, l3 e l4)
lale = ale(tmin, tmax, vmin, vmax)
l1 = l2 = l3 = l4 = lale

sep = "--------------------------------------------------------"
sep2 = "########################################################"

# Juntar a lista aleatória com o tempo num único array
def juntaListaTempo(li,tp):
	li_str=str(li)
	tp_str=str(tp)
	st=li_str+tp_str
	return st

def contaInsertionSort(l1):
        #Início da contagem do tempo
        inicio=time.time()
        #Irá executar a função Quick Sort
        l1=bubbleSort(l1)
        #retorno da string completa para fora da função e a informação do tempo de execução também
        fim = time.time()
        tempo = fim - inicio
        return l1, tempo

def contaBubbleSort(l2):
	#Início da contagem do tempo
	inicio=time.time()
	#Irá executar a função Quick Sort
	l2=bubbleSort(l2)
	#retorno da string completa para fora da função e a informação do tempo de execução também
	fim = time.time()
	tempo = fim - inicio
	return l2, tempo

def contaMergeSort(l3):
	#Início da contagem do tempo
	inicio=time.time()
	#Irá executar a função Quick Sort
	l3=quickSort(l3)
	#retorno da string completa para fora da função e a informação do tempo de execução também
	fim = time.time()
	tempo = fim - inicio
	return l3, tempo

def contaQuickSort(l4):
	#Início da contagem do tempo
	inicio=time.time()
	#Irá executar a função Quick Sort
	l4=quickSort(l4)
	#retorno da string completa para fora da função e a informação do tempo de execução também
	fim = time.time()
	tempo = fim - inicio
	return l4, tempo

# Apresentação na tela os resultados
def apresentacaoresult(l1,l2,l3,l4):
    print ("\n")
    print (sep2)
    print ("Lista inicial aleatória:\n",lale,)
    print (sep2)
    print ("\n")
    l1=contaInsertionSort(l1)
    l1l=l1[0]
    l1t=l1[1]
    print ("Lista ordenada pelo método Insertion Sort:\n",l1l)
    print ("O tempo que executa o método Insertion Sort:\n", l1t)
    print (sep)
    print ("Lista inicial para o método Bubble Sort: ",l2)
    l2=contaBubbleSort(l2)
    l2l=l2[0]
    l2t=l2[1]
    print ("Lista ordenada pelo método Bubble Sort:\n",l2l)
    print ("O tempo que executa o método Bubble Sort:\n",l2t)
    print (sep)
    print ("Lista inicial para o método Merge Sort: ",l3)
    l3=contaMergeSort(l3)
    l3l=l3[0]
    l3t=l3[1]
    print ("Lista ordenada pelo método Merge Sort:\n",l3l)
    print ("O tempo que executa o método Merge Sort:\n",l3t)
    print (sep)
    print ("Lista inicial para o método Quick Sort: ",l4)
    l4=contaQuickSort(l4)
    l4l=l4[0]
    l4t=l4[1]
    print ("Lista ordenada pelo método Quick Sort:\n",l4l)
    print ("O tempo que executa o método Quick Sort:\n",l4t)
    print (sep)
    return l1t,l2t,l3t,l4t

#Declaração de Variáveis para os Cálculos Minimos, Médios e Máximos
l1tm=float('inf')
l1tmx=float('-inf')
l1total=0
l2tm=float('inf')
l2tmx=float('-inf')
l2total=0
l3tm=float('inf')
l3tmx=float('-inf')
l3total=0
l4tm=float('inf')
l4tmx=float('-inf')
l4total=0

#Este for faz gerar neste caso 200 listas aleatórias e vai fazer os cáculos
for i in range (200):
    #Cálculo Minimo, Médio e Máximo do Insertion Sort
    result=apresentacaoresult(l1,l2,l3,l4)
    l1total=l1total+result[0]
    if result[0] < l1tm:
        l1tm=result[0]
    if result[0] > l1tmx:
        l1tmx=result[0]
    #Cálculo Minimo, Médio e Máximo do Bubble Sort
    l2total=l2total+result[1]
    if result[1] < l2tm:
        l2tm=result[1]
    if result[1] > l2tmx:
        l2tmx=result[1]
    #Cálculo Mínimo, Médio e Máximo do Merge Sort
    l3total=l3total+result[2]
    if result[2] < l2tm:
        l3tm=result[2]
    if result[2] > l3tmx:
        l3tmx=result[2]
    #Cálculo Mínimo, Médio e Máximo do Quick Sort
    l4total=l4total+result[3]
    if result[3] < l4tm:
        l4tm=result[3]
    if result[3] > l4tmx:
        l4tmx=result[3]

#Apresentação dos cálculos do método Insertion Sort
print ("O tempo mínimo pelo método Insertion Sort, foi de : ", l1tm, " segundos.")
l1media=l1total/200
print ("O tempo médio do Insertion Sort foi : ", l1media)
print ("O tempo máximo pelo método Insertion Sort, foi de : ", l1tmx, " segundos.")
print (sep2)

#Apresentação dos cálculos do método Bubble Sort
print ("O tempo mínimo pelo método Bubble Sort foi de : ", l2tm, " segundos.")
l2media=l2total/200
print ("O tempo médio do Bubble Sort foi : ", l2media)
print ("O tempo máximo pelo método Bubble Sort foi de : ", l2tmx, " segundos.")
print (sep2)

#Apresentação dos cálculos do método Merge Sort
print ("O tempo mínimo pelo método Merge Sort foi de : ", l3tm, " segundos.")
l3media=l3total/200
print ("O tempo médio do Merge Sort foi : ", l3media)
print ("O tempo máximo pelo método Merge Sort foi de : ", l3tmx, " segundos.")
print (sep2)

#Apresentação dos cálculos do método Quick Sort
print ("O tempo mínimo pelo método Quick Sort foi de : ", l4tm, " segundos.")
l4media=l4total/200
print ("O tempo médio do Quick Sort foi : ", l4media)
print ("O tempo máximo pelo método Quick Sort foi de : ", l4tmx, " segundos.")
print (sep2)



