

def analise(tabela, estados, simbolos, item):

    return erro

e = 1
r = 2
#REGRAS
# 1) E -> E v T         4) T -> F
# 2) E -> T             5) F -> (E)
# 3) T -> T & F         6) F -> id

#tabela de ações e transições
#           id     v     &     (     )      $    E   T   F 
tabela = [[[e,5],[ 0 ],[ 0 ],[e,4],[ 0  ],[ 0 ],[1],[2],[3]],
          [[ 0 ],[e,6],[ 0 ],[ 0 ],[ 0  ],["a"],[0],[0],[0]],
          [[ 0 ],[r,2],[e,7],[ 0 ],[r,2 ],[r,2],[0],[0],[0]],
          [[ 0 ],[r,4],[r,4],[ 0 ],[r,4 ],[r,4],[0],[0],[0]],
          [[e,5],[ 0 ],[ 0 ],[e,4],[ 0  ],[ 0 ],[8],[2],[3]],
          [[ 0 ],[r,6],[r,6],[ 0 ],[r,6 ],[r,6],[0],[0],[0]],
          [[e,5],[ 0 ],[ 0 ],[e,4],[ 0  ],[ 0 ],[0],[9],[3]],
          [[e,5],[ 0 ],[ 0 ],[e,4],[ 0  ],[ 0 ],[0],[0],[10]],
          [[ 0 ],[e,6],[ 0 ],[ 0 ],[e,11],[ 0 ],[0],[0],[0]],
          [[ 0 ],[r,1],[e,7],[ 0 ],[r,1 ],[r,1],[0],[0],[0]],
          [[ 0 ],[r,3],[r,3],[ 0 ],[r,3 ],[r,3],[0],[0],[0]],
          [[ 0 ],[r,5],[r,5],[ 0 ],[r,5 ],[r,5],[0],[0],[0]]]

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
            analise(tabela,estados,simbolos,0)

        case "v":
            analise(tabela,estados,simbolos,1)

        case "&":
            analise(tabela,estados,simbolos,2)

        case "(":
            analise(tabela,estados,simbolos,3)

        case ")":
            analise(tabela,estados,simbolos,4)

        case "$":
            analise(tabela,estados,simbolos,5)

        case "E":
            analise(tabela,estados,simbolos,6)

        case "T":
            analise(tabela,estados,simbolos,7)

        case "F":
            analise(tabela,estados,simbolos,8)

