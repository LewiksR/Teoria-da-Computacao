'''
Autômato Finito Não Determinístico (AFN)
'''
# 2 - delta do AFN
def delta(automato, estado, simbolo):
    try:
        return automato[2][(estado, simbolo)]
    except KeyError:
        return {}


# o retorno é uma lista de estados
# passando referencia da lista ao inves de valor string. A diferença no AFN ocorre  quando ele esta entrando no estado (o que ainda nao é esse parte)

# 3 - Fecho-Epsilon
# A função eclose pode receber um estado com apenas um elemento (Set1 = 'a') ou um conjunto de elementos (Set2 = 'a','b','c','d').
def eclose(automato,estado):
    simbolo = ''   # O simbolo possui valor '' para definir como se fosse um épsilon.
    eclosure = set()   # Nesta linha foi criado um set vazio eclosure = { }
    for estados in estado:   # Este for serve para percorrer cada estado presente no Set de entrada(estado), seja eles Set1 ou Set2, por exemplo.
        eclosure = eclosure.union({estados}) # @Conrado Luiz Pela definição: q ∈ ECLOSE(q)
        eclosure = eclosure.union(delta(automato, estados, simbolo))  # Nesta linha o eclosure está utilizando o .union para somar o eclose de cada elemento do set de entrada e guardar na própria variável.
    return eclosure # Será retornado um Set com o resultado da soma do eclose de cada Set de entrada.

# 4 - Delta estendido do AFN
def delta_hat(automato, estado, palavra):
    if palavra == []:
        return estado
    else:
        simbolo = palavra.pop()
        fe = eclose(automato, estado)
        fn = set()
        for e in fe:
            estados = delta_hat(automato, {e}, palavra)
            deltas = [delta(automato, estado, simbolo) for estado in estados]
            fn = fn.union(*deltas)
        return fn
#Assim como no AFD a função vai partir do estado inicial recebido e recursivamente chamar a função delta() até o fim da palavra. Porém no AFN deverá calcular o fecho epsilon (fe)
#para cada estado e posteriormente chamar a função delta() para cada um dos estados preenchendo o vetor de estados encontrados (fn).


# 5 - Função aceitação
def aceita(automato, palavra): # palavra é um array com os simbolos. e.g. [1, 0, 1]
    estados_finais = delta_hat(automato, {automato[3]}, palavra)
    for estado in estados_finais:
        if estado in automato[4]:
            return True
    return False

    
