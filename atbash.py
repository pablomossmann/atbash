import sys

def cifra(texto, modo):
    az = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 0123456789'
    za = 'ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa 9876543210'
    atbash = ''
    i = 0

    for x in texto:
        c = 0
        flag = 0
        for y in az:
            if x == y:
                flag = 1
                atbash += za[c]
            c += 1
        if flag == 0:
            atbash += texto[i]
        i += 1
            
    return atbash

def verificar():
    try:
        f = open('nome_arquivo.txt')
        f.close()
    except:
        f = open('nome_arquivo.txt', 'w')
        f.close()
        sys.exit()
    
def getInfo(nome, op):
    with open(nome, op) as f:
        arquivo = f.readlines()

    f.close()
    return arquivo

def criptografar():
    nome = 'nome_arquivo.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('nome_arquivo_cripto.txt', 'w')

    for frase in arquivo:
        criptografado = cifra(frase, 1)
        f.write(criptografado)
    f.close()

def descriptografar():
    nome = 'nome_arquivo_cripto.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('nome_arquivo_descripto.txt', 'w')

    for frase in arquivo:
        descriptografado = cifra(frase, 0)
        f.write(descriptografado)
    f.close()

def main():
    verificar()
    criptografar()
    descriptografar()

if __name__ == "__main__":
    main()
