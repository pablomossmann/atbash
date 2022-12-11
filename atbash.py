import sys
##Definições dos modos e da chave para (des)criptografar.
MODO_CRIPTOGRAF = 1
MODO_DESCRIPTOGRAF = 0
CHAVE = 12

def cifra(texto, chave, modo): #Desenvolvimento da Cifra de Cesar
    az = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 0123456789'
    za = 'ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa 9876543210'

    atbash = ''

    for x in texto:
        c = 0
        for y in az:
            if x == y:
                atbash += za[c]
            c += 1
            
    return atbash

def verificaArquivo(): #Verifica se há um arquivo com esse nome, caso não tenha ele cria
    try:
        f = open('entrada.txt')
        f.close()
    except:
        f = open('entrada.txt', 'w')
        f.close()
        sys.exit()
    
def getInfo(nome, op):
    with open(nome, op) as f:
        arquivo = f.readlines()

    f.close()
    return arquivo

def descriptografar():
    nome = 'criptografado.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('descriptografado.txt', 'w')

    for frase in arquivo:
        descriptografado = cifra(frase, CHAVE, MODO_DESCRIPTOGRAF)
        f.write(descriptografado)
    f.close()

def criptografar():
    nome = 'entrada.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('criptografado.txt', 'w') #Cria o arquivo caso não exista com a possibilidade de acrescentar

    for frase in arquivo:
        criptografado = cifra(frase, CHAVE, MODO_CRIPTOGRAF)
        f.write(criptografado)
    f.close()

def main():
    verificaArquivo()
    criptografar()
    descriptografar()

if __name__ == "__main__":
    main()
