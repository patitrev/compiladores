def analise(token, afd):
    aceite = 12
    i = 0
    for simb in token:
        match simb:
            case "i":
                j = 0
                aceite = afd[i][j]
                i = aceite
            case "f":
                j = 1
                aceite = afd[i][j]
                i = aceite
            case "d":
                j = 2
                aceite = afd[i][j]
                i = aceite
            case "o":
                j = 3
                aceite = afd[i][j]
                i = aceite
            case "+":
                j = 4
                aceite = afd[i][j]
                i = aceite
            case "-":
                j = 5
                aceite = afd[i][j]
                i = aceite
            case "*":
                j = 6
                aceite = afd[i][j]
                i = aceite
            case "<":
                j = 7
                aceite = afd[i][j]
                i = aceite
            case ">":
                j = 8
                aceite = afd[i][j]
                i = aceite
            case "=":
                j = 9
                aceite = afd[i][j]
                i = aceite
            case "a":
                j = 10
                aceite = afd[i][j]
                i = aceite
            case "b":
                j = 11
                aceite = afd[i][j]
                i = aceite
    return aceite 


# Montar AFD fixo:
x=12  
#       i f d o + - * < > =  a  b
afd = [[1,x,3,x,5,6,7,8,9,10,11,11],
       [x,2,x,x,x,x,x,x,x,x,x,x],   #1
       [x,x,x,x,x,x,x,x,x,x,x,x],   #2 aceite do 'if'
       [x,x,x,4,x,x,x,x,x,x,x,x],   #3
       [x,x,x,x,x,x,x,x,x,x,x,x],   #4 aceite do 'do'
       [x,x,x,x,x,x,x,x,x,x,x,x],   #5 aceite do +
       [x,x,x,x,x,x,x,x,x,x,x,x],   #6 aceite do -
       [x,x,x,x,x,x,x,x,x,x,x,x],   #7 aceite do *
       [x,x,x,x,x,x,x,x,x,x,x,x],   #8 aceite do <
       [x,x,x,x,x,x,x,x,x,x,x,x],   #9 aceite do >
       [x,x,x,x,x,x,x,x,x,x,x,x],   #10 aceite do =
       [x,x,x,x,x,x,x,x,x,x,11,11], #11 aceite das variáveis
       [x,x,x,x,x,x,x,x,x,x,x,x]]   #x 12 estado de erro

fita = []
mensagemErro = []
#abrir aquivo
with open('code.txt','r') as codigo:
    linhas = codigo.readlines()
    i = 0
    for linha in linhas:
        if len(linha) > 1:
            texto = linha.rsplit(' ')
            for palavra in texto:
                aceite = analise(palavra,afd)
                fita.append(aceite)
                if aceite == x :
                    mensagemErro.append([palavra, i])

        i+=1
print(fita)
codigo.close()