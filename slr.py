

def analise(tabela, estados, simbolos, item):
    x = tabela[estados[0]][item]
    if x[0] != 0:
        if x[0] == 5:
            print('aceite')
            return 1
        else:
            if x[0] == 1:
                estados.insert(0,x[1])
                simbolos.insert(0,item)
                return 0 
            else:
                estados.pop(0)
                match x[1]:
                    case 1:
                        simbolos.pop(2)
                        simbolos.pop(1)
                        simbolos.pop(0)
                        simbolos.insert(0,item)
                        estados.insert(0,tabela[estados[0]][item][5])
                        return 0 
                    case 2:
                        simbolos.pop(0)
                        simbolos.insert(0,item)
                        estados.insert(0,tabela[estados[0]][item][5])
                        return 0 
                    case 3:
                        simbolos.pop(2)
                        simbolos.pop(1)
                        simbolos.pop(0)
                        simbolos.insert(0,item)
                        estados.insert(0,tabela[estados[0]][item][6])
                        return 0 
                    case 4:
                        simbolos.pop(0)
                        simbolos.insert(0,item)
                        estados.insert(0,tabela[estados[0]][item][6])
                        return 0 
                    case 5:
                        simbolos.pop(0)
                        simbolos.insert(0,item)
                        estados.insert(0,tabela[estados[0]][item][7])
                        return 0 
                    case 6:
                        simbolos.pop(0)
                        simbolos.insert(0,item)
                        estados.insert(0,tabela[estados[0]][item][7])
                        return 0 

    print("erro")
    return 1

e = 1
r = 2
#REGRAS
# 1) E -> E v T         4) T -> F
# 2) E -> T             5) F -> (E)
# 3) T -> T & F         6) F -> id

#tabela de ações e transições
#           id     v     &     (     )      $    E   T   F 
tabela = [[[e,5],[0,0],[0,0],[e,4],[ 0,0],[0,0],[1],[2],[3]],
          [[0,0],[e,6],[0,0],[0,0],[ 0,0],[5,0],[0],[0],[0]],
          [[0,0],[r,2],[e,7],[0,0],[r,2 ],[r,2],[0],[0],[0]],
          [[0,0],[r,4],[r,4],[0,0],[r,4 ],[r,4],[0],[0],[0]],
          [[e,5],[0,0],[0,0],[e,4],[ 0,0],[0,0],[8],[2],[3]],
          [[0,0],[r,6],[r,6],[0,0],[r,6 ],[r,6],[0],[0],[0]],
          [[e,5],[0,0],[0,0],[e,4],[ 0,0],[0,0],[0],[9],[3]],
          [[e,5],[0,0],[0,0],[e,4],[ 0,0],[0,0],[0],[0],[10]],
          [[0,0],[e,6],[0,0],[0,0],[e,11],[0,0],[0],[0],[0]],
          [[0,0],[r,1],[e,7],[0,0],[r,1 ],[r,1],[0],[0],[0]],
          [[0,0],[r,3],[r,3],[0,0],[r,3 ],[r,3],[0],[0],[0]],
          [[0,0],[r,5],[r,5],[0,0],[r,5 ],[r,5],[0],[0],[0]]]

entrada = ["id", "&", "id", "v", "id", "$"]
simbolos = []
estados = [0]
erro = 0
for item in entrada:
    if erro == 1:
        print ('deu erro')
        break
    match item:
        case "id":
            erro = analise(tabela,estados,simbolos,0)

        case "v":
            erro = analise(tabela,estados,simbolos,1)

        case "&":
            erro = analise(tabela,estados,simbolos,2)

        case "(":
            erro = analise(tabela,estados,simbolos,3)

        case ")":
            erro = analise(tabela,estados,simbolos,4)

        case "$":
            erro = analise(tabela,estados,simbolos,5)
