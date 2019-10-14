from sklearn import tree
import pyttsx3


en = pyttsx3.init()

def falar(texto_falado):
    en.say(texto_falado)
    en.setProperty('voice','pt-br')
    en.setProperty('rate',145)
    en.setProperty('volume',1)
    en.runAndWait()

#Febre
febre_alta = 0
febre_baixa = 0
# ------------------
falar('Olá, Seja Bem Vindo ao Smart Doctor\n '
      'Primeiramente queremos saber a sua temperatura do corpo para vermos se você apresenta febre. '
      'Vamos começar ?')
falar('Quantos graus deu o termômetro no seu corpo ?')
temperatura = int(input(''))
if temperatura >= 38:
    falar(f'Você está com febre alta, está com {temperatura} º Celsius')
    febre_alta = temperatura
elif temperatura < 38:
    falar(f'Você não está com febre alta, está com {temperatura} º Celsius')
    febre_baixa = temperatura

# olhos vermelhos
sim = 1
nao = 0
# ---------------

# graus
leve = 1
moderada = 2
intensa = 3
#----------------

# Definição das doenças por inteiros
nenhuma = 0
dengue = 1
zika = 2
chikungunya = 3
#-----------------------------------

sintomas = [[intensa, moderada, leve, intensa, intensa, nao, leve, febre_alta, leve],
            [moderada, leve, moderada, leve, leve, sim, intensa, febre_baixa, moderada],
            [moderada, intensa, intensa, leve, moderada, sim, leve, febre_alta, leve],
            [nenhuma,nenhuma,nenhuma,nenhuma,nenhuma,nao,nenhuma,febre_baixa,nenhuma]]

doenca = [dengue, zika, chikungunya, nenhuma]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(sintomas, doenca)

print('A seguir responda apenas com "Leve","Moderada" ou "Intensa" os respectivos sintomas abaixo:')
print()

falar('Está sentido dores de cabeça ?')
dor_cabeca = input('')
if dor_cabeca.lower() == 'leve':
    dor_cabeca_e = 1
elif dor_cabeca.lower() == 'moderada':
    dor_cabeca_e = 2
elif dor_cabeca.lower() == 'intensa':
    dor_cabeca_e = 3
elif dor_cabeca.lower() == 'não' or 'nao':
    dor_cabeca_e = 0


falar('Está sentido dores na articulação ?')
dor_articulacao = input('')
if dor_articulacao.lower() == 'leve':
    dor_articulacao_e = 1
elif dor_articulacao.lower() == 'moderada':
    dor_articulacao_e = 2
elif dor_articulacao.lower() == 'intensa':
    dor_articulacao_e = 3
elif dor_articulacao.lower() == 'não' or 'nao':
    dor_articulacao_e = 0


falar('Está sentido dores musculares ?')
dor_muscular = input('')
if dor_muscular.lower() == 'leve':
    dor_muscular_e = 1
elif dor_muscular.lower() == 'moderada':
    dor_muscular_e = 2
elif dor_muscular.lower() == 'intensa':
    dor_muscular_e = 3
elif dor_muscular.lower() == 'não' or 'nao':
    dor_muscular_e = 0


falar('Está sentido fadiga (cansaço) ?')
fadiga = input('')
if fadiga.lower() == 'leve':
    fadiga_e = 1
elif fadiga.lower() == 'moderada':
    fadiga_e = 2
elif fadiga.lower() == 'intensa':
    fadiga_e = 3
elif fadiga.lower() == 'não' or 'nao':
    fadiga_e = 0


falar('Está tendo vômitos ?')
vomitos = input('')
if vomitos.lower() == 'leve':
    vomitos_e = 1
elif vomitos.lower() == 'moderada':
    vomitos_e = 2
elif vomitos.lower() == 'intensa':
    vomitos_e = 3
elif vomitos.lower() == 'não' or 'nao':
    vomitos_e = 0

falar('Está com olhos bem vermelhos ?')
falar('Responda apenas com "sim" ou "não"')
olhos_red = input('')
if olhos_red.lower() == 'sim':
    olhos_red = sim
elif olhos_red.lower() == 'não' or 'nao':
    olhos_red = nao

falar('Está com manchas no corpo ?')
manchas = input('')
if manchas.lower() == 'leve':
    manchas_e = 1
elif manchas.lower() == 'moderada':
    manchas_e = 2
elif manchas.lower() == 'intensa':
    manchas_e = 3
elif manchas.lower() == 'não' or 'nao':
    manchas_e = 0

falar('Está sentido coceiras no corpo ?')
coceiras  = input('')
if coceiras.lower() == 'leve':
    coceiras_e = 1
elif coceiras.lower() == 'moderada':
    coceiras_e = 2
elif coceiras.lower() == 'intensa':
    coceiras_e = 3
elif coceiras.lower() == 'não' or 'nao':
    coceiras_e = 0

resultado = clf.predict([[dor_cabeca_e, dor_articulacao_e, dor_muscular_e,
                          fadiga_e, vomitos_e, olhos_red, manchas_e, temperatura, coceiras_e]])

print()
print()

if resultado == 1:
    falar('Está com dengue')
elif resultado == 2:
    falar('Está com zika')
elif resultado == 3:
    falar('Está com chikungunya')
elif resultado == 0:
    falar('Está com nenhuma doença')