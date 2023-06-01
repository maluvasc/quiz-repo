def apresentacao_quiz():
    print("""Bem vindo a um quiz de Bridge. Bridge é um jogo de cartas jogado por dois pares 
    de jogadores, originado no Reino Unido e derivado do jogo Whist.
    Aqui tem 3 perguntas para testar seu conhecimento básico sobre bridge!
    Você está pronto?""")
    
    afirmativo = input("Responda com 'sim': ").lower()

    if afirmativo == "sim":
        pergunta_um()

def pergunta_um():

    print("""
    Primeira pergunta:
    O que é um leilão no Bridge?
    ________________________
    1. Leilão é o ato de compra e venda de objetos pelo preço de maior valor pronunciado.
    ________________________
    2. Leilão é uma aposta que o jogador faz sozinho quando sabe que ganhará o contrato sem nenhum problema.
    ________________________
    3. Leilão é a comunicação entre a dupla de jogadores, onde cada um tenta descrever
    as cartas que possuem na sua mão na linguagem do jogo, para jogar um contrato que esperam 
    vencer.
    """)

    resposta_certa_um = input("Digite aqui a resposta que você considera correta entre 1, 2 e 3: ")

    if resposta_certa_um == "3":
        print("""Parabéns, você acertou a questão um! A resposta certa era realmente a alternativa 3, comunicação entre a dupla.
                Vamos para a próxima pergunta.""")
        pergunta_dois()
    elif resposta_certa_um == "2":
        print("""Você errou! Foi escolhido aposta que o jogador faz sozinho, mas a resposta certa era comunicação entre a dupla.
                Tente novamente.""")
    elif resposta_certa_um == "1":
        print("""Você errou! Foi escolhido ato de compra e venda, mas a resposta certa era comunicação entre a dupla.
                Tente novamente.""")
    else: 
        print("Resposta inválida! Tente novamente.")


def pergunta_dois():
    print("""
    Segunda pergunta:
    Quantas cartas tem na mão de cada jogador na mesa do Bridge?
    ________________________
    1. 13
    ________________________
    2. 26
    ________________________
    3. 52
    """)

    resposta_certa_dois = input("Digite aqui a resposta que você considera correta entre 1, 2 e 3: ")

    if resposta_certa_dois == "1":
        print("Parabéns, você acertou a questão dois, 13 cartas! Vamos para a próxima pergunta.")
        pergunta_tres()
    elif resposta_certa_dois == "2":
        print("""Você errou! Foi escolhido 26 cartas, mas a resposta certa era a alternativa 1, 13 cartas.
                Tente novamente.""")
    elif resposta_certa_dois == "3":
        print("""Você errou! Foi escolhido 52 cartas, mas a resposta certa era a alternativa 1, 13 cartas.
                Tente novamente.""")
    else: 
        print("Resposta inválida! Tente novamente.")

def pergunta_tres():
    print("""
    Terceira pergunta:
    Como são chamadas as cartas de valores mais altos de cada naipe no Bridge?
    ________________________
    1. Trunfos.
    ________________________
    2. Honras.
    ________________________
    3. Vazas.
     """)

    resposta_certa_tres = input("Digite aqui a resposta que você considera correta entre 1, 2 e 3: ")

    if resposta_certa_tres == "2":
        print("Parabéns, você acertou todas as questões. São chamadas Honras, sabe muito de Bridge ;).")
    elif resposta_certa_tres == "1":
        print("""Você errou! Você escolheu Trunfos, mas a resposta certa era Honras.
                Tente novamente.""")
    elif resposta_certa_tres == "3":
        print("""Você errou! Você escolheu Vazas, mas a resposta certa era Honras.
                Tente novamente.""")
    else: 
        print("Resposta inválida! Tente novamente.")


apresentacao_quiz()


