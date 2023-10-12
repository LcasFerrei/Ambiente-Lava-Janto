import time
p,inp = print,input
c1=0
while True:
  tarefas = inp('insira quais serão as atividades: ').split()
  while True:
    p(tarefas)
    while True:
      ListaDeCarro=[]
      marca = inp('qual a marca do veiculo: ')
      placa = int(inp('qual a placa do veiculo: '))
      for i in range(len(tarefas)):
        ListaDeCarro.append({'marca' : marca,'placa':placa,'status':tarefas[i]})
        p(ListaDeCarro[i])
        time.sleep(3)
      if tarefas[-1] == tarefas[len(tarefas)-1]:
        break
    c1+=1
    p('numero de veiculos prontos: ', c1)
    p('1 : para continuar ')
    p('2 : para redefnir processo de lavagem')
    p('3 : para encerrar tarefas')
    resposta = inp()
    if resposta =='2':
      p('--redefnir processo de lavagem--'.center(15))
      p('')
      break
    elif resposta == '3':
      break
  if resposta=='3':
    p('--aitivades encerradas--'.center(15))
    break
