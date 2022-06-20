*** Settings ***
Documentation       http://api.gerenciame.com/v1/tarefas
Library             RequestsLibrary
Library             Collections
# Suite Setup         Conectar a API
Resource            BDDpt-br.robot
Resource            Resource.robot

*** Variables ***
${URL_API}        http://api.gerenciame.com/v1

*** Test Case ***
Cenário 01: Consulta de tarefas
    Dado que estamos realizando uma request para o endpoint tarefas-get
#    Quando passarmos um token "<token>"
#    E preenchermos o header
    Quando preenchermos os queryParams "2022-06-19" e "2022-06-20"
    E realizarmos a chamada
    Entao o status da chamada sera "200" 
    E o retorno sera de sucesso

 Cenário 02: Consulta de endereço inexistente
     Dado que esteja conectado no webservice de consultas de CEP
     Quando o usuário consultar o CEP "99999-999"
     Então nenhum dado deve ser mostrado para o CEP "99999999"

Cenário 03: Consulta de endereço inexistente
    Dado que esteja conectado no webservice de consultas de CEP
    Quando o usuário consultar o CEP "99999-999"
    Então a mensagem de erro "CEP INVÁLIDO" deve ser retornada
