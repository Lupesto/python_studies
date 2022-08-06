modelo = 'G3'
componente_procurado = 'Carcaça'

lista = ['Carcaça Chassis Moto G3 Xt 1556+tampa Traseira 100%original não liga', ' Chassis Moto G 3 Xt1556', 'Câmera Frontal Moto G3 Original Retirado',
         'Câmera Frontal Motorola Moto G3 Xt1543 Xt1544 Retirada', 'Flex Do Encaixe Do Display Motorola Moto G5 Original',
         'Alto Falante Auricular Auto Moto G3 Xt1543 Xt1544 Original', 'Alto Falante Auricular Auto Moto G3 Xt1543 Xt1544 Original',
         'Câmera Frontal  Moto G3 Xt1543 Xt1544 Retirada', 'Borracha Proteção Entrada P2 Fone Moto G3 Original ',
         'Tampa Traseira Original Moto G3 - Xt 1543 Original - Usada ', 'Alto Falante Campainha Moto E E1 G1 G3 Xt1021 Xt1022 Xt1025',
         'Conector De Fone - Moto G3 Xt1544 - 100% Original - Retirada', 'Placa Do Flash Luz Traseira Motorola Moto G3 Original',
         'Entrada P2 Conector Do Fone Motorola Moto G3 Original', 'Par De Contato Conector Do Auto Falante Moto G3 Original ',
         'Alto-falante Campainha Motorola Moto G3 Original', 'Alto Falante Auricular Motorola Moto G3 Original',
         'Tampa Do Conector De Carga Motorola Moto G3 Original', 'Kit Borrachas Dos Botões Power E Volumes Moto G3 Original',
         'Camera Self Frontal Motorola Moto G3 Xt1543 Xt1544 Original', 'Placa Mãe Moto G3 Para Retirada De Componentes',
         'Auto Falante Moto C Plus G2 G3 G4 G4 Play G4 Plus G5 G5 Plus', 'Cabo Flex Display Motorola Moto G3 Dual Xt1543 100% Original',
         'Slot Sim Card Chip Motorola Moto G3 Xt1543 Xt1544 Xt1550', 'Carcaça Aro Chassi Motorola Moto G6 Play Xt1922 Com Flex',
         'Botão Power Interno Moto G3 Xt1543', 'Botão Volume Moto G3 Xt1543', 'Botão Power Interno Moto G3 Xt1543', 'Dock Conector De Carga Moto G3 Xt1543',
         'Dock Conector De Carga Moto G3 Xt1543', 'Botão Power Moto G3 Xt1543', 'Botões Externo Do Aro Lateral Motorola Moto G3 Original',
         'Campainha Alto Falante Viva Voz Moto G1 G3 E2 Original', 'Cabo Flex Display Motorola Moto G3 Dual Xt1543 100% Original sem sinal', 'Aro Chassi Moto G5 Plus Xt1683',
         'Dock Conector De Carga Moto G3 Xt1543', 'Dock Conector De Carga Moto G3 Xt1543', 'Chassi Frontal Moto G5s Xt1802 Plus Original De Fabrica',
         'Aro Chassi Moto G5s  Original Retirado', 'Chassi Branco Moto X Force Xt1580 100% Original', 'Auricular Alto Falante Speaker Moto G3 100% Original',
         'Aro Frontal Lateral Com Chassi Motorola Moto G5 Xt1672', 'Carcaça Berço Moto G3 ', 'Gabinete Chassi LG G3 D850 D855 Frame Carenagem',
         'Gabinete Chassi LG G3 D850 D855 Frame Carenagem', 'Aro Chassi Carcaça Moto G5 Usado Xt1672 Xt1671 Preto',
         'Gabinete Aro Chassi Motorola Moto G6 Plus Xt1926 Original', 'Gabinete Aro Chassi Motorola Moto G6 Plus Xt1926 Original sem sinal',
         'Gabinete Aro Chassi Motorola Moto G6 Plus Xt1926 Original', 'Gabinete Aro Chassi Motorola Moto G6 Plus Xt1926 Original']

precos = ['R$69,99', 'R$25', 'R$8,99', 'R$9', 'R$9,90', 'R$9,90', 'R$9,99', 'R$9,99', 'R$10', 'R$10', 'R$10,99', 'R$12,80', 'R$13,89',
          'R$13,89', 'R$13,89', 'R$13,89', 'R$13,89', 'R$13,89', 'R$13,89', 'R$14,77', 'R$18', 'R$19,99', 'R$19,99', 'R$19,99', 'R$20',
          'R$20,90', 'R$20,90', 'R$20,90', 'R$20,90', 'R$20,90', 'R$20,90', 'R$21,90', 'R$22,90', 'R$22,99', 'R$24', 'R$24,90', 'R$24,90',
          'R$25', 'R$25,99', 'R$29', 'R$29,90', 'R$29,90', 'R$30', 'R$33', 'R$34,69', 'R$34,90', 'R$35,90', 'R$35,90', 'R$35,90', 'R$35,90']


palavrasMust = [componente_procurado]

palavrasEvitar = ['retirada de componentes', 'componentes', 'sucata',
                  'defeito', 'mas', 'descrição', 'não funciona', 'não liga',
                  'peças', 'sem sinal']

"""LIDAR CoM MAISCULAS E MINUSCULAS. <- terei que aprender regex?

Deve ser referente ao modelo Procurado.
Jogar os condizentes em uma lista | Ou | Pegar a posição na lista
com posição na lista pegar o preço referente.


"""

condizentes = []
for i in lista:
    if modelo in i and componente_procurado in i:
        condizentes.append(i)

for i in palavrasEvitar:
    for a in condizentes:
        if i in a:
            del(condizentes[condizentes.index(a)])

print(condizentes)
