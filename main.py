#!/usr/bin/python3

from random import choices

# Global
GABARITO = list()
N_QUESTOES = 20
ALTERNATIVAS = ['a', 'b', 'c', 'd', 'e']
N_TENTATIVAS = int()

# Funções da Prova
def gerar_gabarito() -> None:
	global GABARITO

	for _ in range(N_QUESTOES):
		altertiva = choices(ALTERNATIVAS)[0]
		GABARITO.append(altertiva)

	pass

def corrigir_prova(respostas:list) -> int:
	global N_TENTATIVAS

	N_TENTATIVAS += 1/2
	acertos = int()

	for (resposta_teste, resposta_gab) in zip(respostas, GABARITO):
		if resposta_teste == resposta_gab:
			acertos += 1
			pass
		pass

	return acertos

# Funções do Bot
def responder_prova() -> list:
	respostas = list()

	for _ in range(N_QUESTOES):
		altertiva = choices(ALTERNATIVAS)[0]
		respostas.append(altertiva)

	return respostas

def comparar_respostas(respostas_1:list, respostas_2: list):
	diff_index = list()
	c_iguais = int()

	for (resposta_1, resposta_2, i) in zip(respostas_1, respostas_2, range(N_QUESTOES)):
		if resposta_1 == resposta_2:
			c_iguais += 1
		else:
			diff_index.append(i)

		pass

	return (diff_index, c_iguais)

# Funções Extras
def no_repeat_alts(alt_remove: str) -> list:
	altertivas = ALTERNATIVAS.copy()
	return altertivas.remove(alt_remove)

# Main
def main() -> None:
	gerar_gabarito()

	# conjunto_respostas = [{
	# 	respostas: responder_prova(),
	# 	pontuacao: corrigir_prova(self.respostas)
	# }]

	pontuacao_inicial_1 = 0
	pontuacao_inicial_2 = 0

	resposta_1 = responder_prova()
	resposta_2 = responder_prova()

	nova_pontuacao_1 = corrigir_prova(resposta_1)
	nova_pontuacao_2 = corrigir_prova(resposta_2)

	diff_index, c_iguais = comparar_respostas(resposta_1, resposta_2)

	print( nova_pontuacao_1 , nova_pontuacao_2, c_iguais, "-", N_TENTATIVAS)
	

	while True:

		if (nova_pontuacao_2 - pontuacao_inicial_1) > (nova_pontuacao_1 - pontuacao_inicial_2):

			mudar_diff_index = choices(diff_index)[0]
			mudar_rand_index = choices(range(N_QUESTOES))[0]

			resposta_1[mudar_rand_index] = choices(ALTERNATIVAS)[0]
			resposta_1[mudar_diff_index] = choices(ALTERNATIVAS)[0]
		else:
			mudar_diff_index = choices(diff_index)[0]
			mudar_rand_index = choices(range(N_QUESTOES))[0]

			resposta_2[mudar_rand_index] = choices(ALTERNATIVAS)[0]
			resposta_2[mudar_diff_index] = choices(ALTERNATIVAS)[0]

		pontuacao_inicial_1 = nova_pontuacao_1
		pontuacao_inicial_2 = nova_pontuacao_2

		nova_pontuacao_1 = corrigir_prova(resposta_1)
		nova_pontuacao_2 = corrigir_prova(resposta_2)

		diff_index, c_iguais = comparar_respostas(resposta_1, resposta_2)
		
		print( nova_pontuacao_1 , nova_pontuacao_2, c_iguais, "-", N_TENTATIVAS)

		# print( (nova_pontuacao_1 -pontuacao_inicial_1), (nova_pontuacao_2 -pontuacao_inicial_2), c_iguais)

	pass

if __name__ == '__main__':
	main()