import datetime

x = datetime.datetime.now()
titulo = x.strftime("%d%B%Y")



nomeArquivo = 'x'
arquivo = open(titulo+".txt", 'a')

arquivo.write('Teste\n')

arquivo.write('sahushauhsuahs')
arquivo.close
