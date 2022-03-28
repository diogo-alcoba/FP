#Diogo Alcobaca, numero 95553

#---------------------------------TAD posicao----------------------------------------------------

def cria_posicao(x,y):
    #cria_posicao: natural x natural ---> posicao
    '''Construtor que recebe argumentos correspondentes as coordenadas de uma
    posicao e devolve a posicao correspondente'''
    if type(x) is int and x>=0 and type(y) is int and y>=0: #verificar que as coordenadas sao inteiros positivos
        return (x,y)
    else:
        raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(pos):
    #cria_copia_posicao: posicao --->posicao
    '''Construtor que recebe uma posicao como argumento e devolve uma copia
    dessa posicao'''
    return cria_posicao(pos[0],pos[1])

def obter_pos_x(pos):
    #obter_pos_x: posicao ----> natural
    '''Seletor que devolve a abcissa da posicao'''
    return pos[0]

def obter_pos_y(pos):
    #obter_pos_y: posicao ----> natural
    '''Seletor que devolve a ordenada da posicao'''
    return pos[1]

def eh_posicao(pos):
    #eh_posicao: universal ---> booleano
    '''Reconhecedor que devolve True se o seu argumento for uma posicao
    e devolve False se nao for'''
    if type(pos) is tuple:
        if len(pos)==2: #verificar que o argumento e um tuplo com exatamente dois numeros, um para a abcissa e outro para a ordenada
            if type(pos[0]) is int and pos[0]>=0 and type(pos[1]) is int and pos[1]>=0: #verificar se esses numeros sao inteiros positivos
                return True
            return False
        return False
    return False

def posicoes_iguais(pos1,pos2):
    #posicoes_iguais: posicao x posicao --> booleano
    '''Teste que devolve True apenas se as posicoes que recebe como
    argumentos sao iguais'''
    return pos1==pos2

def posicao_para_str(pos):
    #posicao_para_str: posicao ---> str
    '''Transformador que devolve a representacao externa duma posicao,
    sendo esta do tipo '(x,y)', em que x e y sao, respetivamente, a abcissa e 
    a ordenada da posicao'''
    return str(pos)

def obter_posicoes_adjacentes(pos):
    #obter_posicoes_adjacentes: posicao ---> tuplo de posicoes
    '''Funcao de alto nivel que devolve um tuplo com as posicoes adjacentes
    a posicao dada como argumento, de acordo com a ordem de leitura do
    labirinto'''
    if pos==(0,0): #caso da origem de modo a nao ultrapassar a dimensao do labirinto
        return ((1,0),(0,1)) 
    elif obter_pos_x(pos)==0: #caso para a as posicoes na fronteira da esquerda, de modo a nao ultrapassar a dimensao do labirinto
        return ((obter_pos_x(pos),obter_pos_y(pos)-1),(obter_pos_x(pos)+1,obter_pos_y(pos)),(obter_pos_x(pos),obter_pos_y(pos)+1))
    elif obter_pos_y(pos)==0: #caso para as posicoes fronteira de cima, de modo a nao ultrapassar a dimensao do labirinto
        return ((obter_pos_x(pos)-1,obter_pos_y(pos)),(obter_pos_x(pos)+1,obter_pos_y(pos)),(obter_pos_x(pos),obter_pos_y(pos)+1))
    else: #caso para qualquer outra posicao
        return ((obter_pos_x(pos),obter_pos_y(pos)-1),(obter_pos_x(pos)-1,obter_pos_y(pos)),(obter_pos_x(pos)+1,obter_pos_y(pos)),(obter_pos_x(pos),obter_pos_y(pos)+1))

#-----------------------------------TAD unidade--------------------------------------

def cria_unidade(pos,vida,forca,exercito):
    #cria_unidade: posicao x natural x natural x str ---> unidade
    '''Construtor que recebe uma posicao, dois valores maiores que 0, 
    correspondentes a forca e vida da unidade, e uma cadeia de carateres
    nao vazia correspondente ao exercito da unidade, e devolve a unidade
    correspondente'''
    if type(forca) is int and type(vida) is int and forca>0 and vida>0 and eh_posicao(pos) and type(exercito) is str and len(exercito)!=0:
        return {'pos':pos, 'vida':vida, 'forca':forca, 'exercito':exercito} #verificar que a vida e forca sao inteiros maiores que 0 e que a cadeia de carateres nao e vazia 
    else:
        raise ValueError('cria_unidade: argumentos invalidos')

def cria_copia_unidade(uni):
    #cria_copia_unidade: unidade ---> unidade
    '''Construtor que recebe uma unidade e devolve uma copia dessa unidade'''
    return cria_unidade(uni['pos'],uni['vida'],uni['forca'],uni['exercito'])

def obter_posicao(uni):
    #obter_posicao: unidade ---> posicao
    '''Seletor que devolve a posicao da unidade'''
    return uni['pos']

def obter_exercito(uni):
    #obter_exercito: unidade ---> str
    '''Seletor que devolve o exercito da unidade'''
    return uni['exercito']

def obter_forca(uni):
    #obter_forca: unidade ---> natural
    '''Seletor que devolve a forca da unidade'''
    return uni['forca']

def obter_vida(uni):
    #obter_vida: unidade ---> natural
    '''Seletor que devolve a vida da unidade'''
    return uni['vida']

def muda_posicao(uni,pos):
    #muda_posicao: unidade x posicao ---> unidade
    '''Modificador que modifica destrutivamente a unidade, alterando a sua 
    posicao pela posicao dada como argumento, e devolve a propria unidade'''
    uni['pos']=pos
    return uni

def remove_vida(uni,pontos_vida):
    #remove_vida: unidade x natural ----> unidade
    '''Modificador que modifica destrutivamente a unidade, alterando os seus 
    pontos de vida, subtraindo o argumento, e devolve a propria unidade'''
    uni['vida']=uni['vida']-pontos_vida
    return uni

def eh_unidade(uni):
    #eh_unidade: universal ---> booleano
    '''Reconhecedor que verifica se o argumento e uma unidade, devolvendo True
    se for'''
    if type(uni) is dict: #verificar que e um dicionario
        if len(uni)==4 and 'pos' in uni and 'vida' in uni and 'forca' in uni and 'exercito' in uni: #verificar que tem 4 chaves, que correspondem a posicao, vida, forca, exercito
            if eh_posicao(uni['pos']) and type(uni['vida']) is int and uni['vida']>0 and type(uni['forca']) is int and uni['forca']>0 and type(uni['exercito']) is str and uni['exercito']!=0: #verificar que a posicao dada e uma posicao valida, que a vida e forca sao inteiros positivos, e que o exercito e uma string nao vazia
                return True
            return False
        return False
    return False

def unidades_iguais(uni1,uni2):
    #unidades_iguais: unidade x unidade ---> booleano
    '''Teste que devolve True apenas se as unidades dadas como argumentos sao
    iguais'''
    return uni1==uni2

def unidade_para_char(uni):
    #unidade_para_chr: unidade ---> str
    '''Transformador que devolve a cadeia de carateres de um unico elemento,
    correspondente ao primeiro caracter em maiuscula do exercito da unidade
    dada como argumento'''
    if ord(uni['exercito'][0])>=97: #verificar se o primeiro caracter da string e uma minuscula
        return chr(ord(uni['exercito'][0])-32) #se for, subtrair 32 ao seu codigo ASCII, de modo a passar de minuscula a maiuscula
    else:
        return uni['exercito'][0] #se o primeiro caracter da string ja for uma maiuscula, devolve esse proprio caracter

def unidade_para_str(uni):
    #unidade_para_str: unidade ---> str
    '''Transformador que devolve a representacao externa de uma unidade'''
    lst=[uni['vida']]+[uni['forca']] #colocacao da vida e forca da unidade numa lista
    return unidade_para_char(uni)+str(lst)+'@'+str(uni['pos']) #devolver essa lista, mais a representacao externa de uma unidade, separadas por um '@'

def unidade_ataca(uni1,uni2):
    #unidade_ataca: unidade x unidade ----> booleano
    '''Funcao de alto nivel que modifica destrutivamente uni2, retirando-lhe
    aos pontos de vida o valor correspondente a forca de ataque da uni1, e
    devolve True se uni2 for destruida e False caso contrario'''
    attack=obter_forca(uni1)
    remove_vida(uni2,attack) #tirar a vida de uni2 o ataque de uni1
    health=obter_vida(uni2) #ver a vida de uni2 apos o ataque
    if health<=0: #ver se a vida e zero ou menos, ou seja, ver se a unidade morreu
        return True
    else:
        return False
    
def ordenar_unidades(tup_unidades):
    #ordenar_unidades: tuplo de unidades ---> tuplo de unidades
    '''Funcao de alto nivel que devolve um tuplo com as mesmas unidades do tuplo
    fornecido como argumento, mas ordenadas pela ordem de leitura do labirinto'''
    cont=1 #contador que percorre cada unidade to tuplo
    while cont<=len(tup_unidades)-1: 
        for i in range(len(tup_unidades)-1):
            if obter_pos_y(obter_posicao(tup_unidades[i]))>obter_pos_y(obter_posicao(tup_unidades[i+1])): #ver se a ordenada da posicao duma unidade e superior a da unidade seguinte
                tup_unidades=tup_unidades[:i]+(tup_unidades[i+1],)+(tup_unidades[i],)+tup_unidades[i+2:] #se for, troca-las de ordem
            elif obter_pos_y(obter_posicao(tup_unidades[i]))==obter_pos_y(obter_posicao(tup_unidades[i+1])): #no caso de as ordenadas serem iguais, comparar as abcissas
                if obter_pos_x(obter_posicao(tup_unidades[i]))>obter_pos_x(obter_posicao(tup_unidades[i+1])): #ver se a abcissa da posicao duma unidade for maior a da unidade seguinte 
                    tup_unidades=tup_unidades[:i]+(tup_unidades[i+1],)+(tup_unidades[i],)+tup_unidades[i+2:] #se for, troca-las de ordem
        cont=cont+1 #atualizacao do contador, para ver a proxima unidade
    return(tup_unidades)

#-----------------------------------------TAD mapa----------------------------------

def cria_mapa(d,w,e1,e2):
    #cria_mapa: tuplo x tuplo x tuplo x tuplo ---> mapa
    '''Construtor que recebe um tuplo com dois valores inteiros, correspondentes
    as dimensoes do labirinto, um tuplo de 0 ou mais posicoes correspondentes
    as paredes que nao sao os limites exteriores do labirinto, um tuplo de 
    uma ou mais unidades do mesmo exercito e um tuplo com uma ou mais
    unidades de um outro exercito, e devolve o mapa que representa internamente
    o labirinto e as unidades presentes'''
    if type(d) is tuple and type(w) is tuple and type(e1) is tuple and type(e2) is tuple and len(d)==2 and d[0]>=3 and d[1]>=3 and type(d[0]) is int and type(d[1]) is int and len(e1)>=1 and len(e2)>=1: #verificar que todos os argumentos sao tuplos, que a dimensao e valida e que os tuplos de unidades nao sao vazios
        if len(w)!=0: #ver se o tuplo de paredes e vazio ou nao
            for pos in w: #se nao for, ver se cada elemento do tuplo e uma posicao, e que esta esta contida dentro do labirinto, nao correspondendo as paredes exteriores
                if not eh_posicao(pos) or obter_pos_x(pos)==0 or obter_pos_y(pos)==0 or obter_pos_x(pos)>=d[0]-1 or obter_pos_y(pos)>=d[1]-1:
                    raise ValueError('cria_mapa: argumentos invalidos')
        for uni_1 in e1: 
            if not eh_unidade(uni_1): #ver se todos os elementos do primeiro tuplo de unidades sao unidades validas
                raise ValueError('cria_mapa: argumentos invalidos')
        for uni_2 in e2:
            if not eh_unidade(uni_2): #ver se todos os elementos do segundo tuplo de unidades sao unidades validas
                raise ValueError('cria_mapa: argumentos invalidos')
            mapa={'dim':d, 'paredes':w, 'exercito_1':e1, 'exercito_2':e2} 
            return mapa
    raise ValueError('cria_mapa: argumentos invalidos')

def cria_copia_mapa(mapa):
    #cria_copia_mapa: mapa ---> mapa
    '''Construtor que recebe um mapa como argumento e devolve uma copia desse
    mapa'''
    e1=()
    for uni in mapa['exercito_1']:
        e1=e1+(cria_copia_unidade(uni),) #criar copias de cada unidade do primeiro exercito
    e2=()
    for uni in mapa['exercito_2']:
        e2=e2+(cria_copia_unidade(uni),) #criar copias de cada unidade do segundo exercito   
    return cria_mapa(mapa['dim'],mapa['paredes'],e1,e2)

def obter_tamanho(mapa):
    #obter_tamanho: mapa ---> tuplo
    '''Seletor que devolve um tuplo correspondente a dimensao do mapa'''
    return mapa['dim']

def obter_nome_exercitos(mapa):
    #obter_nome_exercitos: mapa ---> tuplo
    '''Seletor que devolve um tuplo ordenado com duas cadeias de caracteres
    correspondentes aos nomes dos exercitos do mapa'''
    nomes=()
    if len(mapa['exercito_1'])!=0: #verificar que ha unidades do primeiro exercito
        nomes=nomes+(obter_exercito(mapa['exercito_1'][0]),) 
    if len(mapa['exercito_2'])!=0: #verificar que ha unidades do segundo exercito
        nomes=nomes+(obter_exercito(mapa['exercito_2'][0]),)
    nomes_ordenados=tuple(sorted(nomes)) #ordenar os nomes dos exercitos
    return nomes_ordenados

def obter_unidades_exercito(mapa,exercito):
    #obter_unidades_exercito: mapa x str -----> tuplo de unidades
    '''Seletor que devolve um tuplo contendo todas as unidades do mapa
    pertencentes ao exercito dado como argumento'''
    tup_unidades=()
    if len(mapa['exercito_1'])!=0 and obter_exercito(mapa['exercito_1'][0])==exercito: #ver se o nome do exercito das unidades do primeiro exercito e igual ao nome dado como argumento
        for uni in mapa['exercito_1']: #se for, colocar todas as unidades desse exercito num tuplo
            tup_unidades=tup_unidades+(uni,) 
    elif len(mapa['exercito_2'])!=0 and mapa['exercito_2'][0]['exercito']==exercito: #se o nome nao for igual ao das unidades do primeiro exercito, ver se e igual as do segundo
        for uni in mapa['exercito_2']:
            tup_unidades=tup_unidades+(uni,) #se for, colocar todas as unidades desse exercito num tuplo
    return ordenar_unidades(tup_unidades) #devolver com essas unidades ordenadas pela ordem de leitura do labirinto
    
def obter_todas_unidades(mapa):
    #obter_todas_unidades: mapa ----> tuplo
    '''Seletor que devolve um tuplo contendo todas as unidades do mapa,
    ordenadas pela ordem de leitura do labirinto'''
    tup_unidades=() 
    for uni in mapa['exercito_1']:
        tup_unidades=tup_unidades+(uni,) #adicionar as unidades do primeiro exercito 
    for uni in mapa['exercito_2']:
        tup_unidades=tup_unidades+(uni,) #adicionar as unidades do segundo exercito
    return ordenar_unidades(tup_unidades) #devolver o tuplo ordenado de todas as unidades

def obter_unidade(mapa,pos):
    #obter_unidade: mapa x posicao ---> unidade
    '''Seletor que devolve a unidade do mapa que se encontra na posicao dada
    como argumento'''
    for uni in mapa['exercito_1']:
        if obter_posicao(uni)==pos: #verificar se alguma unidade do primeiro exercito esta na posicao dada como argumento
            return uni
    for uni in mapa['exercito_2']:
        if obter_posicao(uni)==pos: #verificar se alguma unidade do segundo exercito esta na posicao dada como argumento
            return uni

def eliminar_unidade(mapa,unidade):
    #eliminar_unidade: mapa x unidade ---> mapa
    '''Modificador que modifica destrutivamente o mapa e a unidade dados como 
    argumentos, eliminando a unidade e deixando livre a posicao onde esta se
    encontrava'''
    for index in range(len(mapa['exercito_1'])):
        if mapa['exercito_1'][index]==unidade: #verificar se a unidade dada como argumento se encontra no primeiro exercito
            mapa['exercito_1']=mapa['exercito_1'][:index]+mapa['exercito_1'][index+1:] #se sim, devolver o mapa dado como argumento sem essa unidade
            return mapa
    for index in range(len(mapa['exercito_2'])):
        if mapa['exercito_2'][index]==unidade: #verificar se a unidade dada como argumento se encontra no segundo exercito
            mapa['exercito_2']=mapa['exercito_2'][:index]+mapa['exercito_2'][index+1:] #se sim, devolver o mapa dado como argumento sem essa unidade
            return mapa  

def mover_unidade(mapa,unidade,pos):
    #mover_unidade: mapa x unidade x posicao ---> mapa
    '''Modificador que modifica destrutivamente o mapa e a unidade dados 
    como argumentos, alterando a posicao da unidade no mapa para a nova
    posicao dada como argumento, deixando livre a posicao onde se encontrava'''
    for uni in mapa['exercito_1']:
        if uni==unidade: #verificar se a unidade dada como argumento se encontra no primeiro exercito
            muda_posicao(uni,pos) #altera a posicao da unidade para a dada como argumento
            return mapa
    for uni in mapa['exercito_2']: 
        if uni==unidade: #verificar se a unidade dada como argumento se encontra no segundo exercito
            muda_posicao(uni,pos) #altera a posicao da unidade para a dada como argumento
            return mapa
        
def eh_posicao_unidade(mapa,pos):
    #eh_posicao_unidade: mapa x posicao ---> booleano
    '''Reconhecedor que devolve True apenas no caso da posicao dada como 
    argumento estar ocupada por uma unidade'''    
    if eh_posicao(pos): #verificar se a posicao dada como argumentos e valida
        if obter_unidade(mapa,pos) in mapa['exercito_1'] or obter_unidade(mapa,pos) in mapa['exercito_2']: #verificar se ha alguma unidade nessa posicao em cada um dos exercitos
            return True
        return False
    return False
        
def eh_posicao_corredor(mapa,pos):
    #eh_posicao_corredor: mapa x posicao ---> booleano
    '''Reconhecedor que devolve True apenas no caso da posicao dada como 
    argumento corresponder a um corredor do labirinto'''
    if eh_posicao(pos):
        if 0<obter_pos_x(pos)<mapa['dim'][0]-1 and 0<obter_pos_y(pos)<mapa['dim'][1]-1 and pos not in mapa['paredes']:
            return True #verificar se a posicao dada esta dentro das dimensoes do labirinto e verificar que nao e nenhuma parede interior
        return False
    return False

def eh_posicao_parede(mapa,pos):
    #eh_posicao_parede: mapa x posicao ----> booleano
    '''Reconhecedor que devolve True apenas no caso da posicao dada como
    argumento corresponder a uma parede do labirinto'''
    if eh_posicao(pos):
        if pos not in mapa['paredes']: #verificar se a posicao dada e ou nao uma parede interior
            if ((obter_pos_x(pos)==0 or obter_pos_x(pos)==mapa['dim'][0]-1) and obter_pos_y(pos)<=mapa['dim'][1]-1) or ((obter_pos_y(pos)==0 or obter_pos_y(pos)==mapa['dim'][1]-1) and obter_pos_x(pos)<=mapa['dim'][0]-1): #verificar se a posicao dada e uma parede exterior
                return True 
            return False
        return True #se a posicao dada for uma parede interior, entao devolver True
    return False

def mapas_iguais(m1,m2):
    #mapas_iguais: mapa x mapa ----> booleano
    '''Teste que devolve True apenas se os mapas dados como argumentos forem
    iguais'''
    return m1==m2

def mapa_para_str(mapa):
    #mapa_para_str: mapa ---> str
    '''Transformador que devolve a representacao externa do mapa'''    
    res=''
    dim=obter_tamanho(mapa) #obter dimensao do mapa
    for fila in range(dim[1]): #percorrer as filas do mapa
        for coluna in range(dim[0]): #percorrer as colunas do mapa
            if eh_posicao_parede(mapa,cria_posicao(coluna,fila)): #verificar se e parede
                res=res+'#'
            elif eh_posicao_unidade(mapa,cria_posicao(coluna,fila)): #verificar se e posicao
                res=res+unidade_para_char(obter_unidade(mapa,cria_posicao(coluna,fila)))
            else: #se nao for uma nem outra, e porque e corredor
                res=res+'.'
        res=res+'\n' 
    res=res[:-1] #retirar o ultimo '\n' do labirinto
    return res

def obter_inimigos_adjacentes(mapa,uni):
    #obter_inimigos_adjacentes: mapa x unidade ----> tuplo de unidades
    '''Funcao de alto nivel que devolve um tuplo contendo as unidades inimigas
    adjacentes a unidade dada como argumento, de acordo com a ordem de leitura
    do labirinto'''
    pos_adjs=obter_posicoes_adjacentes(obter_posicao(uni)) #obter as posicoes adjacentes da unidade dada comoa argumento
    uni_adjs=() 
    for pos in pos_adjs:
        if eh_unidade(obter_unidade(mapa,pos)): #verificar se ha unidades nessas posicoes
            uni_adjs=uni_adjs+(obter_unidade(mapa,pos),) #se sim, adiciona-las a um tuplo que vai conter as unidades adjacentes a dada como argumento
    inim_adjs=()
    for uni_adj in uni_adjs:
        if obter_exercito(uni)!=obter_exercito(uni_adj): #verificar se as unidades adjacentes sao ou nao do mesmo exercito da unidade dada como argumento
            inim_adjs=inim_adjs+(uni_adj,) #se nao forem, e porque sao inimigas, e portanto sao adicionadas a um tuplo que vai conter as unidades inimigas adjacentes
    return inim_adjs

def obter_movimento(mapa, unit):
    #obter_movimento: mapa x unidade ----> posicao
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

#------------------------Funcoes adicionais-----------------------------------

def calcula_pontos(mapa,exercito):
    #calcula_pontos: mapa x str ---> inteiro
    '''Funcao que recebe um mapa e uma cadeia de caracteres correspondente ao
    nome de um dos exercitos do mapa e devolve o total dos pontos de vida de 
    todas as unidades desse exercito'''
    vida_total=0
    unidades=obter_unidades_exercito(mapa,exercito) #obter todas as unidades do exercito dado como argumento
    for uni in unidades:
        vida_total=vida_total+obter_vida(uni) #obter a vida de cada uma delas e somar tudo
    return vida_total

def simula_turno(mapa):
    #simula_turno: mapa ---> mapa
    '''Funcao que modifica o mapa fornecido como argumento de acordo com a 
    simulacao de um turno de batalha completo, e devolve o proprio mapa.
    Seguindo a ordem de leitura do labirinto, cada unidade viva vai-se mover
    uma vez e atacar um inimigo se possivel'''
    nome_e1=obter_nome_exercitos(mapa)[0] 
    nome_e2=obter_nome_exercitos(mapa)[1] #obtencao do nome dos dois exercitos
    cemiterio=() #criacao de um tuplo vazio onde vao ser colocadas as unidades que ja morreram
    unidades_ordenadas=obter_todas_unidades(mapa) #obtencao de todas as unidades do mapa, que vao estar ordenadas pela ordem de leitura do labirinto
    for uni in unidades_ordenadas:  
        if uni not in cemiterio and len(obter_unidades_exercito(mapa,nome_e1))!=0 and len(obter_unidades_exercito(mapa,nome_e2))!=0: 
            #por cada unidade do mapa, se ela nao estiver ja morta e se ainda restarem unidades de ambos os exercitos:
            pos=obter_movimento(mapa,uni) #obter a posicao para onde a unidade se ira mover
            mover_unidade(mapa,uni,pos) #mover a unidade para essa posicao
            inim_adj=obter_inimigos_adjacentes(mapa,uni) #obter um tuplo com todos os inimigos adjacentes a essa unidade, ordenados pela ordem de leitura do labirinto
            if len(inim_adj)!=0: #se esse tuplo nao for vazio
                if unidade_ataca(uni,inim_adj[0]): #vai ser atacada a primeira unidade inimiga e verificar-se se essa unidade morreu
                    eliminar_unidade(mapa,inim_adj[0]) #se morreu, remove-la do mapa
                    cemiterio=cemiterio+(inim_adj[0],) #e adiciona-la ao cemiterio, de modo a esta nao atacar nesse mesmo turno em que morre
    return mapa    

def pontuacao_str(mapa,nome_1,nome_2,rip):
    #pontuacao_str: mapa x str x str x booleano ----> str
    '''Funcao auxiliar que recebe como argumento um mapa, um nome para cada
    exercito, e a flag 'rip' que e 'True' se todas as unidades de algum 
    exercito ja morreram e e 'False' se ainda houveram unidades vivas de ambos
    os exercitos. Esta funcao devolve uma string com a pontuacao de cada um
    dos dois exercitos'''
    if rip: #verificar se algum dos exercitos ja morreu
        if obter_nome_exercitos(mapa)[0]==nome_1: #verificar se o primeiro exercito e o exercito que ainda esta vivo
            pontos_1=calcula_pontos(mapa,nome_1) #se for, calcular os seus pontos
            pontos_2=0 #e colocar os pontos do outro exercito a 0
        else: #se o primeiro exercito nao for o exercito que ainda esta vivo, e porque ja morreu, e o segundo e o que ainda nao morreu
            pontos_1=0 #colocar os pontos do primeiro exercito a 0
            pontos_2=calcula_pontos(mapa,nome_2) #calcular os pontos do segundo exercito, que ainda esta vivo
    else: #se nenhum dos exercitos tiver morrido ainda, calcular os pontos de cada um como usual
        pontos_1=calcula_pontos(mapa,nome_1) 
        pontos_2=calcula_pontos(mapa,nome_2)
    res= '[ '+str(nome_1)+':'+str(pontos_1)+' '+str(nome_2)+':'+str(pontos_2)+' ]'
    return res #devolver a string que contem o nome de cada exercito e os pontos de cada um a frente do nome
 
def simula_batalha(nome,modo):
    #simula_batalha: str x booleano ----> str
    '''Funcao que simula uma batalha completa. A batalha termina quando um dos
    exercitos vence ou, se apos completar um turno de batalha, nao ocorreu 
    nenhuma alteracao ao mapa e as unidades. Esta funcao recebe uma cadeia de 
    caracteres e um valor booleano e devolve o nome do exercito vencedor
    O argumento booleano ativa o modo 'verboso' (True) ou o modo 'quiet'
    (False). No modo 'quiet' e devolvido o primeiro e o ultimo turno da batalha
    e no modo 'verboso' e mostrado cada turno da batalha'''
    f=open(nome,'r')
    dim=eval(f.readline()) #leitura da dimensao do labirinto
    nome_vida_forca_1=eval(f.readline()) #leitura do nome do primeiro exercito, da vida e forca das suas unidades
    nome_vida_forca_2=eval(f.readline()) #leitura do nome do segundo exercito, da vida e forca das suas unidades
    paredes=eval(f.readline()) #leitura das paredes
    posicoes_1=eval(f.readline()) #leitura das posicoes das unidades do primeiro exercito
    posicoes_2=eval(f.readline()) #leitura das posicoes das undiades do segundo exercito
    e1=()
    for pos in posicoes_1:
        e1=e1+(cria_unidade(pos,nome_vida_forca_1[1],nome_vida_forca_1[2],nome_vida_forca_1[0]),) #criacao do primeiro exercito
    e2=()
    for pos in posicoes_2:
        e2=e2+(cria_unidade(pos,nome_vida_forca_2[1],nome_vida_forca_2[2],nome_vida_forca_2[0]),) #criacao do segundo exercito
    mapa=cria_mapa(dim,paredes,e1,e2) #criacao do mapa
    f.close()
    copia=()
    nome_1=obter_nome_exercitos(mapa)[0] 
    nome_2=obter_nome_exercitos(mapa)[1]
    rip=False #inicializacao da flag 'rip' que indica se todas as unidades de algum exercito ja morreram (True); se ainda estiverem vivas unidades de ambos os exercitos fica em 'False'
    print(mapa_para_str(mapa)) #print do mapa inicial
    print(pontuacao_str(mapa,nome_1,nome_2,rip)) #print da pontuacao inicial
    while copia!=mapa: #verificar que houve alteracoes no mapa de um turno para o outro; se nao houver e porque nao ha mais movimentos possiveis e por isso ha empate
        if len(obter_nome_exercitos(mapa))==2: #verificar que ainda ha unidades de ambos os exercitos
            copia=cria_copia_mapa(mapa)
        else:
            rip=True #se nao houver e porque um dos exercitos ja morreu, e a batalha acabou
            break #sair do ciclo nesse caso
        mapa=simula_turno(mapa) #fazer o proximo turno
        if modo and len(obter_nome_exercitos(mapa))==2: #se estiver em modo verboso e ainda houver unidades de ambos os exercitos:
            print(mapa_para_str(mapa)) #imprimir o mapa
            print(pontuacao_str(mapa,nome_1,nome_2,rip)) #e a pontuacao
    print(mapa_para_str(mapa)) #print do ultimo turno
    print(pontuacao_str(mapa,nome_1,nome_2,rip)) # print da pontuacao do ultimo turno
    if len(obter_nome_exercitos(mapa))==2: #verificar se ainda ha unidades vivas de ambos os exercitos
        return('EMPATE') #se houver e porque ha empate
    return str(obter_nome_exercitos(mapa)[0]) #caso contrario, dar print do nome do exercito vencedor, o unico que ainda esta vivo