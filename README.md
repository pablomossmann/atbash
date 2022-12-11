# atbash

<h3>Descrição</h3>
O Atbash é uma cifra de substituição onde o alfabeto é invertido/espelhado, por exemplo A=Z e B=Y. Neste código exite uma melhoria onde os números também são invertidos, por exemplo 0=9 e 1=8. Porém os demais caracteres especiais permanecerão iguais.

<h3>Código</h3>
É iniciado com a importação da biblioteca sys para, para possibilitar o encerramento do programa quando necessário. É realizada a chamada do método Main(), onde serão chamados os demais métodos.

```py
import sys
```

```py
def main():
    verificar()
    criptografar()
    descriptografar()

if __name__ == "__main__":
    main()
```

<h3>Verificar</h3>
Este método é responsável por verificar a existência do arquivo "nome_arquivo.txt", caso já exista o programa irá continuar mas caso contrário e irá cria-lo e encerrar o programa.

```py
def verificar():
    try:
        f = open('nome_arquivo.txt')
        f.close()
    except:
        f = open('nome_arquivo.txt', 'w')
        f.close()
        sys.exit()
```

<h3>GetInfo</h3>
Este método é responsável por coletar e fornecer o conteúdo no arquivo solicitado. Será utilizado pelos métodos criptografar() e descriptografar().

```py
def getInfo(nome, op):
    with open(nome, op) as f:
        arquivo = f.readlines()

    f.close()
    return arquivo
```

<h3>Criptografar</h3>
Este método é responsável por realizar a chamada do método cifra() enviando como parâmetro o conteúdo do "nome_arquivo.txt" e por fim criando o arquivo "nome_arquivo_cripto.txt" que terá como conteúdo o retorno da cifra.

```py
def criptografar():
    nome = 'nome_arquivo.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('nome_arquivo_cripto.txt', 'w')

    for frase in arquivo:
        criptografado = cifra(frase, 1)
        f.write(criptografado)
    f.close()
```

<h3>Descriptografar</h3>
Este método é responsável por realizar a chamada do método cifra() enviando como parâmetro o conteúdo do "nome_arquivo_cripto.txt" e por fim criando o arquivo "nome_arquivo_descripto.txt" que terá como conteúdo o retorno da cifra.

```py
def descriptografar():
    nome = 'nome_arquivo_cripto.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('nome_arquivo_descripto.txt', 'w')

    for frase in arquivo:
        descriptografado = cifra(frase, 0)
        f.write(descriptografado)
    f.close()
```

<h3>Cifra</h3>
Este é o método principal do código, que recebe como parâmetro o texto e o modo e é onde acontece a criptografia. Primeiramente criei duas strings, "az" contendo o alfabeto normal e "za" contendo o alfabeto invertido, elas serão a base para a substituição. Também é criada a string "atbash" que começará vazia e terá seu conteúdo preenchido ao decorrer do código.

É realizado um laço de repetição onde a variável "x" percorrerá caractere por caractere do texto. Para cada caractere terá um segundo laço de repetição dentro que percorrerá a string "za" e será feita uma comparação, isso servirá para tentar encontrar o caractere do texto na string e caso seja encontrado, a posição na string será usada como base para que a "atbash" receba o caractere porém da string "za".

Caso após percorrer a string "za" não seja encontrado o caractere (em resumo, caso não seja uma letra ou número) será adicionado na "atbash" o caractere original.

```py
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
```
