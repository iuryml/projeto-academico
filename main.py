from sklearn import tree

class Decisao:


    #olhos vermelhos e febre acima de 38ºC
    sim = 1
    nao = 0
    #---------------


    leve = 1
    moderada = 2
    intensa = 3

    dengue = 1
    zika = 2
    chikungunya = 3

    sintomas = [[intensa, moderada, leve, intensa, intensa, nao, leve, sim, leve],
                [moderada, leve, moderada, leve, leve, sim, intensa, nao, moderada],
                [moderada, intensa, intensa, leve, moderada, sim, leve, sim, leve]]

    doenca = [dengue, zika, chikungunya]

    contD = 0
    contZ = 0
    contC = 0

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(sintomas, doenca)

    print('A seguir responda apenas com "leve","moderada" ou "intensa" os respectivos sintomas abaixo:')
    print('LEVE - Sintomas quase não sentidos ou de vez quando durante o dia')
    print('MODERADA - Sintomas que aparecem com frequência duranto o dia')
    print('INTESA - Sintomas que aparecem com muita frequência e de grande volume durante o dia')
    print('--'*40)

    dor_cabeca = input('Está sentido dores de cabeça ?\n')
    if dor_cabeca.lower() == 'leve':
        dor_cabeca_e = 1
    elif dor_cabeca.lower() == 'moderada':
        dor_cabeca_e = 2
        contZ += 1
        contC += 1
    elif dor_cabeca.lower() == 'intensa':
        dor_cabeca_e = 3
        contD += 1


    dor_articulacao = input('Está sentido dores na articulação ?\n')
    if dor_articulacao.lower() == 'leve':
        dor_articulacao_e = 1
        contZ += 1
    elif dor_articulacao.lower() == 'moderada':
        dor_articulacao_e = 2
        contD +=1
    elif dor_articulacao.lower() == 'intensa':
        dor_articulacao_e = 3
        contC += 1


    dor_muscular = input('Está sentido dores musculares ?\n')
    if dor_muscular.lower() == 'leve':
        dor_muscular_e = 1
    elif dor_muscular.lower() == 'moderada':
        dor_muscular_e = 2
        contZ += 1
    elif dor_muscular.lower() == 'intensa':
        dor_muscular_e = 3
        contD += 1
        contC += 1


    fadiga = input('Está sentido fadiga (cansaço) ?\n')
    if fadiga.lower() == 'leve':
        fadiga_e = 1
        contZ += 1
        contC += 1
    elif fadiga.lower() == 'moderada':
        fadiga_e = 2
    elif fadiga.lower() == 'intensa':
        fadiga_e = 3
        contD += 1


    vomitos = input('Está tendo vômitos ?\n')
    if vomitos.lower() == 'leve':
        vomitos_e = 1
        contZ += 1
    elif vomitos.lower() == 'moderada':
        vomitos_e = 2
        contC += 1
    elif vomitos.lower() == 'intensa':
        contD += 1
        vomitos_e = 3


    olhos_red = input('Está com olhos bem vermelhos ? Responda apenas "sim ou não" \n')
    if olhos_red.lower() == 'sim':
        olhos_red = sim
        contZ += 1
        contC += 1
    elif olhos_red.lower() == 'não' or 'nao' or '':
        olhos_red = nao
        contD += 1

    manchas = input('Está com manchas no corpo ?\n')
    if manchas.lower() == 'leve':
        manchas_e = 1
        contD += 1
        contC += 1
    elif manchas.lower() == 'moderada':
        manchas_e = 2
    elif manchas.lower() == 'intensa':
        manchas_e = 3
        contZ += 1

    febre = input('Seu termômetro apresentou valor igual ou acima de 38,0º C ?\n')
    if febre.lower() == 'sim':
        temp = sim
        contD += 1
        contC += 1
    elif febre.lower() == 'não' or 'nao' or '':
        temp = nao
        contZ += 1

    coceiras  = input('Está sentido coceiras no corpo ?\n')
    if coceiras.lower() == 'leve':
        coceiras_e = 1
        contD += 1
        contC += 1
    elif coceiras.lower() == 'moderada':
        coceiras_e = 2
        contZ += 1
    elif coceiras.lower() == 'intensa':
        coceiras_e = 3

    r = [dor_cabeca_e, dor_articulacao_e, dor_muscular_e,fadiga_e, vomitos_e, olhos_red, manchas_e, temp, coceiras_e]
    resultado = clf.predict([r])

    print()
    print()

    if resultado == 1:
        print('É possível de você estar com dengue')

    elif resultado == 2:
        print('É possível de você estar com zika')

    elif resultado == 3:
        print('É possível de você estar com chikungunya')


    d = (contD / 9) * 100
    print('Você apresenta {:.2f}% '.format(d))
    z = (contZ / 9) * 100
    print('Você apresenta {:.2f}% '.format(z))
    c = (contC / 9) * 100
    print('Você apresenta {:.2f}% '.format(c))
