# Facebook NLP translator 

## Introduction

At the point in life of writing this, I had 2 objectives :
- I wanted to both learn Portuguese (albeit Brazilian Portuguese)
- I wanted to do a natural language processing project.


Problem with learning a language is about _being efficient._
There's no point to learn a bunch of information I won't use.
Why not use all the things I will actually use? Well to do that I need to know the words I use most.


### What this project is
A project made to identify the following :
    - Most common words.
    - Most common verbs.
    - Word commonality to most popular words (according to wikipedia).

### What this project _isnt_

It's not a magical catch all that will tell you everything.
It's not a perfect project intended for anything serious.
It's not a project for all platforms of messeages.


## Installation and Prep

- (Optional Create a virtual environment)
- `pip install -r requirements.txt`
- `pip install spacy-transformers -f https://download.pytorch.org/whl/torch_stable.html` easiest way to install spacy.
- Download a copy of your facebook messenger data. Unzip it, put the `messages` folder into this projects folder.

## Running

`python main.py`

## Tested against
- Python 3.8

## Example output

```
(venv) ➜  nlu git:(master) ✗ python main.py                  
--MOST COMMON Words and translations--
1: EN i  frequency : 59340
2: EN to  frequency : 37347
3: EN you  frequency : 35365
4: EN the  frequency : 35240
5: EN it  frequency : 26866
6: EN a  frequency : 26404
7: EN   frequency : 20138
8: EN in  frequency : 15739
9: EN that  frequency : 15273
10: EN of  frequency : 13287
11: EN is  frequency : 13065
12: EN and  frequency : 12652
13: EN was  frequency : 11390
14: EN for  frequency : 11231
15: EN be  frequency : 10928
16: EN like  frequency : 10647
17: EN so  frequency : 10499
18: EN its  frequency : 10273
19: EN but  frequency : 10126
20: EN my  frequency : 10001
21: EN have  frequency : 9433
22: EN on  frequency : 9142
23: EN me  frequency : 8959
24: EN not  frequency : 8364
25: EN do  frequency : 8274
26: EN just  frequency : 7914
27: EN what  frequency : 7563
28: EN get  frequency : 7149
29: EN dont  frequency : 6823
30: EN with  frequency : 6822
31: EN if  frequency : 6546
32: EN at  frequency : 6246
33: EN will  frequency : 5972
34: EN are  frequency : 5763
35: EN no  frequency : 5612
36: EN im  frequency : 5424
37: EN how  frequency : 5408
38: EN as  frequency : 5321
39: EN they  frequency : 5267
40: EN go  frequency : 5140
41: EN want  frequency : 5032
42: EN thats  frequency : 4994
43: EN then  frequency : 4879
44: EN good  frequency : 4866
45: EN she  frequency : 4724
46: EN about  frequency : 4699
47: EN he  frequency : 4573
48: EN all  frequency : 4555
49: EN can  frequency : 4503
50: EN we  frequency : 4372
51: EN up  frequency : 4338
52: EN yeah  frequency : 4271
53: EN your  frequency : 4258
54: EN really  frequency : 4225
55: EN did  frequency : 4214
56: EN think  frequency : 4188
57: EN am  frequency : 4130
58: EN know  frequency : 4095
59: EN there  frequency : 4036
60: EN this  frequency : 4029
61: EN id  frequency : 3992
62: EN or  frequency : 3972
63: EN one  frequency : 3928
64: EN out  frequency : 3888
65: EN too  frequency : 3716
66: EN going  frequency : 3662
67: EN time  frequency : 3539
68: EN now  frequency : 3526
69: EN though  frequency : 3388
70: EN would  frequency : 3334
71: EN her  frequency : 3329
72: EN youre  frequency : 3282
73: EN when  frequency : 3256
74: EN an  frequency : 3228
75: EN lol  frequency : 3118
76: EN why  frequency : 3023
77: EN more  frequency : 3000
78: EN didnt  frequency : 2936
79: EN from  frequency : 2900
80: EN need  frequency : 2873
81: EN them  frequency : 2824
82: EN see  frequency : 2709
83: EN got  frequency : 2624
84: EN say  frequency : 2600
85: EN sent  frequency : 2593
86: EN shit  frequency : 2579
87: EN work  frequency : 2530
88: EN could  frequency : 2489
89: EN were  frequency : 2467
90: EN had  frequency : 2430
91: EN way  frequency : 2407
92: EN much  frequency : 2403
93: EN people  frequency : 2317
94: EN xd  frequency : 2307
95: EN right  frequency : 2297
96: EN well  frequency : 2246
97: EN sure  frequency : 2186
98: EN fuck  frequency : 2138
99: EN said  frequency : 2025
100: EN him  frequency : 2014
Your word commonality to the world is 52%
--VERBS--
EN have PT : ['ter ', 'ela tem dois irmãos ', 'ter para fazer '] frequency : 9433
EN want PT : ['querer ', 'querer que alguém faça ', 'querer fazer '] frequency : 5032
EN think PT : ['acreditar ', 'achar ', 'acho que sim '] frequency : 4188
EN know PT : ['saber ', 'você sabia ', 'saber fazer '] frequency : 4095
EN need PT : ['necessidade ', 'necessidades básicas ', 'se for necessário '] frequency : 2873
EN work PT : ['trabalho ', 'bom trabalho ', 'começar trabalhar em '] frequency : 2530
EN fuck PT: No Translation Found! frequency : 2138
EN make PT : ['fazer ', 'produzir ', 'deduzir de '] frequency : 1916
EN link PT : ['elo ', 'conexão ', 'conexão ferroviária '] frequency : 1632
EN feel PT : ['sentir-se ', 'sentir-se bem ', 'sentir calor frio '] frequency : 1395
EN look PT : ['olhar ', 'olhar ', 'cara '] frequency : 1323
EN tell PT : ['dizer ', 'contar alguém sobre alguém ', 'dizer alguém '] frequency : 1292
EN take PT : ['tomada ', 'ter uma ideia sobre alguém ', 'seguir '] frequency : 1282
EN find PT : ['encontrar ', 'localizar ', 'declarar alguém culpado inocente '] frequency : 1230
EN call PT : ['ligação ', 'telefonar para alguém ', 'estar de plantão '] frequency : 945
EN suppose PT : ['supor ', 'supor que ', 'ter obrigação de fazer '] frequency : 936
EN give PT : ['dar ', 'dar ', 'dar alguém '] frequency : 889
EN enjoy PT : ['gostar ', 'desfrutar ', 'gostar de fazer '] frequency : 862
EN mean PT : ['mau ', 'ser mau com alguém ', 'pão-duro '] frequency : 841
EN watch PT : ['vigilância ', 'estar espreita de ', 'estar de guarda '] frequency : 758
EN come PT : ['vir ', 'vir em direção alguém ', 'ir '] frequency : 731
EN code PT : ['código ', 'código ', 'codinome '] frequency : 720
EN send PT : ['enviar ', 'mandar ', 'mande lembranças minhas ela '] frequency : 681
EN wait PT : ['esperar ', 'esperar por alguém ', 'deixar alguém esperando '] frequency : 658
EN mind PT : ['mente ', 'cabeça ', 'estar fora de si '] frequency : 637
EN help PT : ['ajudar ', 'facilitar ', 'melhorar '] frequency : 616
EN guess PT : ['palpite ', 'um palpite sobre ', 'um palpite feliz '] frequency : 571
EN wrong PT : ['errado ', 'incorreto ', 'estar errado sobre alguém '] frequency : 554
EN read PT : ['ler ', 'vê se me entende não ', 'ler para alguém '] frequency : 550
EN worry PT : ['preocupação ', 'aborrecimento ', 'problemas financeiros '] frequency : 537
EN remember PT : ['lembrar ', 'não consigo lembrar nome dele ', 'homenagear '] frequency : 533
EN meet PT : ['encontrar ', 'ir buscar ', 'combinar de ir buscar alguém '] frequency : 516
EN town PT : ['cidade ', 'município ', 'vilarejo '] frequency : 503
EN question PT : ['pergunta ', 'uma pergunta sobre ', 'sem contestar '] frequency : 503
EN able PT : ['capaz ', 'ser capaz de fazer ', 'fisicamente apto '] frequency : 502
EN leave PT : ['despedida ', 'despedir-se de alguém ', 'licença '] frequency : 496
EN plan PT : ['plano ', 'projeto ', 'plano de poupança '] frequency : 484
EN start PT : ['começar ', 'começar fazer ', 'começar por '] frequency : 475
EN bring PT : ['trazer ', 'introduzir ', 'trazer novidades '] frequency : 473
EN live PT : ['vivo ', 'ao vivo ', 'com corrente '] frequency : 472
EN change PT : ['mudança ', 'para variar ', 'seria bom para variar '] frequency : 457
EN hope PT : ['esperança ', 'esperança de ', 'perder esperança '] frequency : 449
EN walk PT : ['caminhada ', 'são cinco minutos pé ', 'ir caminhar '] frequency : 440
EN keep PT : ['sustento ', 'torre de castelo ', 'para valer '] frequency : 432
EN stop PT : ['parada ', 'pôr fim ', 'parada '] frequency : 386
EN believe PT : ['acreditar em ', 'ela não conseguia acreditar no que via ', 'não consigo acreditar que '] frequency : 370
EN imagine PT : ['imaginar ', 'supor ', 'acredito que '] frequency : 368
EN answer PT : ['resposta ', 'em resposta ', 'dar uma resposta alguém '] frequency : 366
EN move PT : ['movimento ', 'apressar-se ', 'mudança '] frequency : 357
EN stay PT : ['estada ', 'permanecer ', 'hospedar-se '] frequency : 352
EN forgot PT : ['esquecer ', 'esquecer de fazer ', 'esquecer que '] frequency : 352
EN thank PT : ['agradecer ', 'agradecer alguém por ', 'obrigado '] frequency : 341
EN email PT : ['e-mail ', 'correio eletrônico ', 'mandar um e-mail para alguém '] frequency : 336
EN break PT : ['rachadura ', 'intervalo ', 'pausa '] frequency : 333
EN chill PT : ['friagem ', 'frio ', 'resfriar-se '] frequency : 328
EN write PT : ['escrever ', 'escrever para alguém ', 'passar um cheque alguém '] frequency : 321
EN drink PT : ['bebida ', 'bebida alcoólica ', 'drinque '] frequency : 311
EN expect PT : ['esperar ', 'supor ', 'esperar que alguém faça '] frequency : 307
EN sound PT : ['sadio ', 'sólido ', 'bom '] frequency : 301
EN happen PT : ['acontecer ', 'que quer que aconteça ', 'por acaso '] frequency : 300
EN rest PT : ['colocar ', 'apoiar ', 'apoiar em '] frequency : 297
EN assume PT : ['pressupor ', 'assumir '] frequency : 294
EN study PT : ['estudar ', 'examinar ', 'estudar '] frequency : 292
EN agree PT : ['concordar ', 'concordar com ', 'concordar em fazer '] frequency : 289
EN book PT : ['livro ', 'álbum ', 'talão '] frequency : 281
EN hear PT : ['ouvir ', 'ficar sabendo ', 'ficar sabendo que '] frequency : 278
EN laugh PT : ['risada ', 'fazer para se divertir ', 'rir '] frequency : 276
EN understand PT : ['entender ', 'compreender ', 'no meu entendimento '] frequency : 272
EN learn PT : ['aprender ', 'saber distinguir certo do errado ', 'decorar '] frequency : 255
EN seem PT : ['parecer ', 'parecer que ', 'parecer feliz aborrecido '] frequency : 247
EN appreciate PT : ['dar valor ', 'apreciar ', 'compreender '] frequency : 241
EN bother PT : ['problema ', 'chateação ', 'não custa nada '] frequency : 231
EN listen PT : ['escutar ', 'escutar alguém ', 'estar atento para ouvir '] frequency : 231
EN kill PT : ['matança ', 'matar ', 'destruir '] frequency : 219
EN notice PT : ['notar ', 'notar que ', 'perceber '] frequency : 217
EN fall PT : ['cair ', 'não ter graça ', 'falhar '] frequency : 216
EN report PT : ['relatório ', 'apresentar um relatório de ', 'reportagem '] frequency : 203
EN upset PT : ['virar ', 'atrapalhar ', 'perturbar '] frequency : 196
EN warm PT : ['morno ', 'quente ', 'para agasalhar '] frequency : 193
EN travel PT : ['viajar ', 'viajar de avião carro ', 'viajar com pouca bagagem '] frequency : 189
EN respond PT : ['responder ', 'responder alguém ', 'reagir '] frequency : 187
EN miss PT : ['senhorita ', 'Miss Brasil ', 'engano '] frequency : 184
EN pass PT : ['desfiladeiro ', 'passe ', 'dar uma cantada em alguém '] frequency : 181
EN turn PT : ['girar ', 'dar voltas ', 'dar voltas em '] frequency : 175
EN spend PT : ['gastar ', 'passar ', 'passar tempo fazendo '] frequency : 172
EN finish PT : ['fim ', 'chegada ', 'acabamento '] frequency : 172
EN explain PT : ['explicar ', 'explicar alguém ', 'explicar como que '] frequency : 162
EN mention PT : ['menção ', 'referência ', 'fazer referência '] frequency : 154
EN stress PT : ['stress ', 'ênfase ', 'acento '] frequency : 151
EN near PT : ['perto ', 'próximo ', 'num futuro próximo '] frequency : 148
EN continue PT : ['continuar ', 'ele prosseguiu dizendo que ', 'continuar com '] frequency : 140
EN pick PT : ['escolha ', 'escolher vontade ', 'melhor do grupo '] frequency : 139
EN become PT : ['tornar-se ', 'ficar ', 'tornar-se advogado professor '] frequency : 137
EN speak PT : ['falar ', 'fale mais alto ', 'por assim dizer '] frequency : 136
EN hold PT : ['preensão ', 'arranjar ', 'compreender '] frequency : 134
EN forward PT : ['para frente ', 'inclinar-se para frente ', 'daquele dia em diante '] frequency : 133
EN offer PT : ['oferecer ', 'oferecer-se para ocupar um cargo ', 'aceita um drinque '] frequency : 131
EN join PT : ['unir ', 'ligar ', 'apertar as mãos '] frequency : 128
EN save PT : ['salvar ', 'salvar as aparências ', 'salvar alguém de alguém '] frequency : 125
EN relax PT : ['relaxar ', 'relaxe ', 'relaxe '] frequency : 123
EN forget PT : ['esquecer ', 'esquecer de fazer ', 'esquecer que '] frequency : 120
EN decide PT : ['decidir ', 'decidir contra fazer ', 'decidir não fazer '] frequency : 119
EN react PT : ['reagir ', 'reagir alguém ', 'reagir alguém '] frequency : 117
EN accept PT : ['aceitar ', 'este cartão de crédito aceito na França não mesmo '] frequency : 112
EN piss PT : ['fazer xixi ', 'gozar alguém ', 'mijar '] frequency : 111
EN fail PT : ['fracassar ', 'fracassar em ', 'falhar '] frequency : 111
EN visit PT : ['visita ', 'fazer uma visita alguém ', 'visitar '] frequency : 110
EN enter PT : ['entrar ', 'penetrar ', 'introduzir '] frequency : 109
EN beat PT : ['batimento ', 'pulsação ', 'batida '] frequency : 108
EN suck PT : ['sugar ', 'aspirar ', 'mamar '] frequency : 108
EN intend PT : ['pretender ', 'pretender fazer ', 'ser destinado '] frequency : 106
EN catch PT : ['apanhar ', 'pegar ', 'capturar '] frequency : 105
EN considering PT : ['apesar de ', 'tendo em vista ', 'apesar do tempo '] frequency : 105
EN avoid PT : ['evitar ', 'evitar fazer ', 'evitar fazer '] frequency : 105
EN lose PT : ['perder ', 'perder cabeça ', 'perder '] frequency : 102
EN light PT : ['luz ', 'luz do dia ', 'luz '] frequency : 99
EN click PT : ['fazer clique ', 'estalar ', 'clicar '] frequency : 99
EN lack PT : ['falta ', 'por falta de ', 'carecer de '] frequency : 99
EN apply PT : ['solicitar ', 'recorrer alguém ', 'candidatar-se um emprego '] frequency : 98
EN build PT : ['construir ', 'fabricar ', 'criar '] frequency : 97
EN suggest PT : ['sugerir ', 'propor ', 'propor alguém que '] frequency : 96
EN drop PT : ['gota ', 'gota gota ', 'uma gota de água no oceano '] frequency : 96
EN wake PT : ['esteira ', 'na esteira de ', 'velório '] frequency : 95
EN follow PT : ['seguir ', 'entender ', 'seguir '] frequency : 90
EN realize PT : ['dar-se conta de ', 'perceber ', 'realizar '] frequency : 89
EN contact PT : ['contato ', 'fazer contato com alguém ', 'relação '] frequency : 88
EN install PT : ['instalar '] frequency : 86
EN pull PT : ['puxar ', 'disparar ', 'extrair '] frequency : 85
EN download PT : ['baixar '] frequency : 85
EN push PT : ['apertar ', 'empurrar ', 'abrir porta empurrando '] frequency : 81
EN cause PT : ['causa ', 'motivo ', 'isto não motivo para '] frequency : 81
EN rock PT : ['rocha ', 'estar em apuros ', 'uísque com gelo '] frequency : 80
EN repeat PT : ['repetir ', 'repetição ', 'reprise '] frequency : 78
EN draw PT : ['atração ', 'empate ', 'sorteio '] frequency : 76
EN adore PT : ['adorar '] frequency : 76
EN dress PT : ['vestido ', 'vestir-se ', 'vestir-se de azul '] frequency : 75
EN blame PT : ['culpar ', 'culpar alguém por ', 'pôr culpa de em alguém '] frequency : 75

```
