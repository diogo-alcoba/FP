#Diogo Alcobaca; numero 95553

def eh_labirinto(lab):
    #eh_labirinto: universal --> booleano
    '''Esta funcao recebe um argumento de qualquer tipo e devolve 'True' se
    o seu argumento corresponde a um labirinto e 'False' caso contrario'''
    if type(lab) is not tuple:
        return(False) #verificar que o input e um tuplo
    elif len(lab)<3:
        return(False) #verificar que o tuplo tem pelo menos 3 tuplos
    for i in lab:
        if type(i) is not tuple:
                return(False) #verificar que o tuplo de input contem apenas tuplos
        elif len(i)<3:
                return(False) #verificar que sao 3 ou mais
        elif len(i)!=len(lab[0]):
                return(False) #verificar que todos os tuplos dentro do tuplo de input tem o mesmo tamanho
        for j in i:
            if not isinstance(j,int): 
                return(False)
            if j!=0 and j!=1:
                return(False) #verificar que os tuplos apenas contem 0's e 1's e mais nenhum numero ou caracter
            elif i[0]==0 or i[-1]==0:
                return(False) #verificar que todos os tuplos comecam e acabam com  1
            elif not (lab[0][1:]==lab[0][:-1] and lab[-1][1:]==lab[-1][:-1]):
                return(False)  #verificar que o primeiro e ultimo tuplo sao apenas constituidos por 1's
    return(True)               

def eh_posicao(pos):
    #eh_posicao: universal --> booleano
    '''Esta funcao recebe um argumento de qualquer tipo e devolve 'True' se o 
    seu argumento corresponde a uma posicao e 'False' caso contrario'''
    if type(pos) is not tuple: 
        return(False) #verificar que a posicao e um tuplo
    elif len(pos)!=2:
        return(False) #verificar que a posicao e constituida apenas por dois caracteres
    for i in pos:
            if i<0 or not isinstance(i,int): 
                return(False) #verificar que esses caracters sao numeros naturais
    return(True)    

def eh_conj_posicoes(conj_pos):
    #eh_conj_posicoes: universal ---> booleano
    '''Esta funcao recebe um argumento de qualquer tipo e devolve 'True' se o
    seu argumento corresponde a um conjunto de posicoes unicas e 'False' caso
    contrario'''
    if type(conj_pos) is not tuple: 
        return(False) 
    visto=() 
    for i in conj_pos: #verificar que o input e constituido por posicoes apenas
        if type(i) is not tuple:                                                      
            return(False)
        elif len(i)!=2:
            return(False)
        elif i in visto:
            return(False) 
        visto=visto+(i,) #verificar que nao ha posicoes repetidas
        for j in i:
            if j<0 or not isinstance(j,int):
                return(False)
    return(True)            

def tamanho_labirinto(lab):
    #tamanho_labirinto: labirinto ---> tuplo
    '''Esta funcao recebe um labirinto e devolve um tuplo de dois valores
    inteiros, correspondendo o primeiro ao numero de colunas e o segundo ao
    numero de linhas do labirinto'''
    if not eh_labirinto(lab):
        raise ValueError('tamanho_labirinto: argumento invalido')
    else:
        col=len(lab) #determinar quantas colonuas tem o labirinto
        lin=len(lab[0]) #determinar quantas linhas tem o labirinto
    return(col,lin)

def eh_mapa_valido(lab,conj_pos):
    #eh_mapa_valido: labirinto x conj_posicoes ---> booleano
    '''Esta funcao recebe um labirinto e um conjunto de posicoes correspondente
    as unidades presentes no labirinto, e devolve 'True' se o segundo 
    argumento corresponde a um conjunto de posicoes compativeis (nao ocupadas
    por paredes) dentro do labirinto e 'False' caso contrario'''
    if not eh_labirinto(lab) or not eh_conj_posicoes(conj_pos):
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
    else:
        for i in conj_pos:
            if not 0<=i[0]<=len(lab)-1:
                return(False) 
            elif not 0<=i[1]<=len(lab[0])-1:
                return(False) #verificar que cada posicao do conjunto de posicoes esta dentro da dimensao do labirinto
            elif lab[i[0]][i[1]]==1: 
                return(False) #verificar que essa posicao nao corresponde a uma parede
    return(True)

def eh_posicao_livre(lab,conj_pos,pos):
    #eh_posicao_livre: labirinto x conj_posisoces x posicao ---> booleano
    '''Esta funcao recebe um labirinto, um conjunto de posicoes correspondente
    a unidades presentes no labirinto e uma posicao, e devolve 'True' se a 
    posicao corresponde a uma posicao livre (nao ocupada nem por paredes, 
    nem pode unidades) dentro do labirinto e 'False' caso contrario'''
    if not eh_labirinto(lab) or not eh_conj_posicoes(conj_pos) or not eh_mapa_valido(lab,conj_pos) or not eh_posicao(pos):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    else:
        for i in conj_pos:
            if i==pos: 
                return(False) #verificar que a posicao nao corresponde a nenhuma do conjunto de posicoes
            elif not 0<=i[0]<=len(lab)-1:
                return(False)
            elif not 0<=i[1]<=len(lab[0])-1:
                return(False)
            elif lab[i[0]][i[1]]==1:
                return(False)
        if not 0<=pos[0]<=len(lab)-1:
            return(False)
        elif not 0<=pos[1]<=len(lab[0])-1:
            return(False)
        elif lab[pos[0]][pos[1]]==1:
            return(False)
    return(True)

def posicoes_adjacentes(pos):
    #posicoes_adjacentes: posicao ----> conj_pos
    '''Esta funcao recebe uma posicao e devolve o conjunto de posicoes
    adjacentes da posicao em ordem de leitura de um labirinto'''
    if not eh_posicao(pos):
        raise ValueError('posicoes_adjacentes: argumento invalido') 
    elif pos==(0,0): 
        res=((1,0),(0,1)) #caso da origem de modo a nao ultrapassar a dimensao do labirinto
    elif pos[0]==0:
        res=((pos[0],pos[1]-1),(pos[0]+1,pos[1]),(pos[0],pos[1]+1)) #caso para a as posicoes na fronteira da esquerda, de modo a nao ultrapassar a dimensao do labirinto
    elif pos[1]==0:
        res=((pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]+1)) #caso para as posicoes fronteira de cima, de modo a nao ultrapassar a dimensao do labirinto
    else:
        res=((pos[0],pos[1]-1),(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]+1)) #caso para qualquer outra posicao
    return(res)
    
def mapa_str(lab,conj_pos):
    #mapa_str: labirinto x conj_pos ---> cadeia de caracteres
    '''Esta funcao recebe um labirinto e um conjunto de posicoes correspondente
    as unidades presentes no labirinto e devolve a cadeia de caracteres que as
    representa'''
    if not eh_labirinto(lab) or not eh_conj_posicoes(conj_pos) or not eh_mapa_valido(lab,conj_pos):
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    else:
        res=''
        c=0
        while c<=len(lab[0])-1: #analise do primeiro elemento de cada tuplo do labirinto; depois do segundo elemento, e assim sucessivamente
            for i in lab:
                if i[c]==1:
                    res=res+'#' #verificar se essa posicao corresponde a uma parede
                else:
                    res=res+'.' #neste caso a posicao nao e uma parede
            res=res+'\n'
            c=c+1
        res=res[:-1]
        for j in conj_pos:
            a=j[1]*(len(lab)+1)+j[0]+1
            res=res[:a-1]+'O'+res[a:] #apos ter o labirinto concluido, inserir as unidades, sendo os pontos substituidos por O's
    return(res)

def posicao_valida(lab,pos):
    #posicao_valida: labirinto x posicao ----> boleano
    '''Funcao auxiliar que recebe um labirinto e uma posicao, e devolve
    'True' se o segundo argumento corresponde a uma posicao compativel 
    (nao ocupada por paredes) dentro do labirinto e 'False' caso contrario'''
    if eh_labirinto(lab)==False or eh_posicao(pos)==False:
        raise ValueError('eh_posicao_valida: algum dos argumentos e invalido')
    elif not 0<=pos[0]<=len(lab)-1:
        return(False)
    elif not 0<=pos[1]<=len(lab[0])-1:
        return(False)
    elif lab[pos[0]][pos[1]]==1:
        return(False)
    return(True)

def obter_objetivos(lab, conj_pos, pos):
    #obter_objetivos: labirinto x conj_posicoes x posicao -----> conj_posicoes
    '''Esta funcao recebe um labirinto, um conjunto de posicoes correspondente
    as unidades presentes no labirinto e uma posicao correspondente a uma das
    unidades, e devolve o conjunto de posicoes (em qualquer ordem) nao ocupadas 
    dentro do labirinto correspondente a todos os possiveis objetivos da 
    unidade correspondente a posicao dada'''
    if not eh_labirinto(lab) or not eh_conj_posicoes(conj_pos) or not eh_posicao(pos) or not eh_mapa_valido(lab,conj_pos) or pos not in conj_pos:
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    a=()
    for i in conj_pos:
        if i!=pos:
            a=a+(i,) #tuplo com todos os elementos do conjunto de posicoes exceto a posicao dada como argumento
    b=()
    for j in a:
        b=b+posicoes_adjacentes(j) #obtencao das posicoes adjacentes a essas posicoes
    res=()
    for k in b:    
        if posicao_valida(lab,k) and k not in res and k not in conj_pos and k!=pos: 
            res=res+(k,) #verificar que as posicoes sao validas tendo em conta o tamanho do labirinto, que nao ha repetidas, e que nenhuma delas pertence ao conjunto de posicoes ou e igual a posicao dada como argumento
    return(res)

def obter_caminho(lab,conj_pos,pos):
    #obter_caminho: labirinto x conj_posicoes x posicao ----> conj_posicoes
    '''Esta funcao recebe um labirinto, um conjunto de posicoes correspondente
    as unidades presentes no labirinto e uma posicao correspondente a uma das
    unidades, e devolve um conjunto de posicoes (potencialmente vazio caso
    nao exista nenhuma unidade alcancavel) correspondente ao caminho de 
    numero minimo de passos desde a posicao dada ate a posicao objetivo'''
    if not eh_labirinto or not eh_conj_posicoes(conj_pos) or not eh_posicao(pos) or not eh_mapa_valido(lab,conj_pos) or pos not in conj_pos:
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    objetivos=obter_objetivos(lab,conj_pos,pos) #definicao dos objetivos
    fila_exploracao=(pos,)+((),) #inicializacao da fila de exploracao que contem a posicao atual e o caminho atual
    visitadas=() #assinalacao das posicoes ja visitadas
    while len(fila_exploracao)>0:
        pos_atual=fila_exploracao[0] 
        cam_atual=fila_exploracao[1]
        if pos_atual not in visitadas:
            visitadas=visitadas+(pos_atual,) #atualizacao das posicoes visitadas
            cam_atual=cam_atual+(pos_atual,) #atualizacao do caminho atual
            if pos_atual in objetivos:
                res=cam_atual
                return(res) #obtencao do caminho minimo
            else:
                adjacentes=posicoes_adjacentes(pos_atual)
                for i in adjacentes:
                    if eh_posicao_livre(lab,conj_pos,i):
                        fila_exploracao=(fila_exploracao)+((i),)+((cam_atual),) #atualizacao da fila de exploracao com as posicoes adjacentes e o caminho atual para cada uma
        fila_exploracao=fila_exploracao[2:] #eliminacao da primeira posicao e primeiro caminho (os que ja foram percorridos) da fila, passando para os proximos que la estao
    return(())

def mover_unidade(lab,conj_pos,pos):
    #mover_unidade: labirinto x conj_posicoes x posicao ----> conj_posicoes
    '''Esta funcao recebe um labirinto, um conjunto de posicoes correspondente
    as unidades presentes no labirinto e uma posicao correspondente a uma das
    unidades, e devolve o conjunto de posicoes atualizado correspondente
    as unidades presentes no labirinto apos a unidade dada ter realizado 
    um unico movimento'''
    if not eh_labirinto(lab) or not eh_conj_posicoes(conj_pos) or not eh_posicao(pos) or not eh_mapa_valido(lab,conj_pos) or pos not in conj_pos:
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    adjacentes=posicoes_adjacentes(pos)
    for i in adjacentes:
        if i in conj_pos:
            return(conj_pos) #verificar se a unidade dada como argumento ja se encontra adjacente a uma outra posicao
    cam=obter_caminho(lab,conj_pos,pos)
    if cam==():
        return(conj_pos) #verificar se realmente existe um caminho possivel
    for j in range(len(conj_pos)):
        if conj_pos[j]==pos:
            a=j #guardar a ordem no tuplo da posicao dada como argumento, para de seguida, poder ser colocada de novo no mesmo sitio, apos ter sido atualizada
    res=conj_pos[:a]+(cam[1],)+conj_pos[a+1:] #colocacao da posicao, depois de atualizada, onde estava originalmente no tuplo
    return(res)

