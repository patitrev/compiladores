# Montar AFD fixo:
x=12  
#       i f d o + - * < > =  a  b
afd = {{1,x,3,x,5,6,7,8,9,10,11,11},
       {x,2,x,x,x,x,x,x,x,x,x,x},    #1
       {x,x,x,x,x,x,x,x,x,x,x,x},   #2 aceite do 'if'
       {x,x,x,4,x,x,x,x,x,x,x,x},    #3
       {x,x,x,x,x,x,x,x,x,x,x,x},   #4 aceite do 'do'
       {x,x,x,x,x,x,x,x,x,x,x,x},   #5 aceite do +
       {x,x,x,x,x,x,x,x,x,x,x,x},   #6 aceite do -
       {x,x,x,x,x,x,x,x,x,x,x,x},   #7 aceite do *
       {x,x,x,x,x,x,x,x,x,x,x,x},   #8 aceite do <
       {x,x,x,x,x,x,x,x,x,x,x,x},   #9 aceite do >
       {x,x,x,x,x,x,x,x,x,x,x,x},   #10 aceite do =
       {x,x,x,x,x,x,x,x,x,x,11,11}, #11 aceite das variáveis
       {x,x,x,x,x,x,x,x,x,x,x,x}    #x estado de erro
       }