import datetime
import os

x = datetime.datetime.now()
titulo = x.strftime("%d%b%Y") #+ x.strftime("%b")
print(titulo)


nomeCompleto = os.path.join('dados', 'dadosLimpos'+titulo)
arquivo = open(nomeCompleto, 'a')
dados = {'xxxxxamera frontal': {'camera frontal j5 metal usada': 20.0, 'camera frontal j5 metal j510mn 100% original retirado': 25.0, 'camera frontal samsung j5 metal (usado)': 25.0, 'camera frontal j5 metal j510mn 100% original retirado ': 27.99, 'camera frontal samsung j5 metal, j510,original usada': 45.9}, 'camera traseira': {'camera traseira samsung j5 metal, j510, original usada': 35.9, 'camera traseira samsung j5 metal sm-j510 retirado 100% origi': 39.99, 'camera traseira j5 metal original': 55.0}, 'placa': {'placa base samsung  j510 j5 metal ': 199.0, 'j5 metal placa mae usada': 200.0, 'placa mãe samsung j5 metal j 510 m/ da original ': 230.0, 'placa mãe lógica samsung j5 metal sm-j510 100% original': 239.9, 'placa mãe original samsung j 5 metal j510': 240.0, 'placa samsung j5 metal sm-j510 (100% funcionando)': 248.99, 'placa principal samsung j5 metal, j510': 249.9, 'placa mãe j5 metal sm-j510mn/ds': 250.0, 'placa mãe lógica samsung j5 metal sm-j510 original': 250.0, 'placa j5 metal': 250.0, 'placa samsung j5 metal': 280.0, 'placa logica principal samsung j5 metal sm-j510mn/ds': 380.0, 'placa mãe samsung j510 j5 metal original': 250.0, 'placa mãe samsung j5 metal j510mn funcionando perfeitamente!': 250.0, 'placa mãe lógica principal j5 metal - sm j510 mn/ds ': 250.0, 'placa  samsung j5 metal sm-j510mn/ds 16gb original retirada': 270.0, 'placa j5 metal j-510': 260.0, 'placa mãe lógica principal j5 j510 metal - 100% testado': 330.0, 'placa mãe samsung galaxy j5 metal j510 + câmeras ': 280.0}, 'tampa': {'tampa traseira branca  j5 metal j510 100% original retirada ': 22.99, 'tampa traseira samsung galaxy j5 j500m/ds original preta': 30.0, 'tampa traseira galaxy j5 metal 2016 j510m original': 33.0, 'tampa traseira parte da placa mãe j510mn/ds j5 metal': 38.0, 'carcaça traseira+tampa j510/j5metal retirada de ap. 100% org': 48.9, 'tampa traseira samsung galaxy j5 metal j510 2016 original ': 29.9, 'tampa traseira original galaxy j5 sm-j510 metal 2016 dourada': 40.0}, 'bateria': {'bateria original usado samsung j5 metal j510': 36.9, 'bateria j5 metal': 45.0, 'bateria j5 metal modelo j510 100%. boa e original retirada !': 90.0, 'bateria j5 metal j510 orig': 88.0}, 'display': {'display touch samsung j510 galaxy j5 metal original novo': 200.0, 'tela frontal touch display j5 2016 j510 - 100% testada': 275.0}, 'carcaça': {'carcaça berço j5 metal': 29.9, 'carcaça traseira samsung j510 j5 2016 original retirado': 30.0, 'carcaça j5 metal': 35.0, 'carcaça traseira+tampa j510/j5metal retirada de ap. 100% org': 48.9, 'carcaça samsung j5 metal': 100.0}}

#print(str(dados))
for i in dados:
    arquivo.write(i)
    arquivo.write("\n")
    for a in dados[i]:
        arquivo.write(a)
        arquivo.write('  ----> R$:')
        arquivo.write(str(dados[i][a]))
        
        arquivo.write("\n")
    arquivo.write("\n")
    
 
arquivo.close()
