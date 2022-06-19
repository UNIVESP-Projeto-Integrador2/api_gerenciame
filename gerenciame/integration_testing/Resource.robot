*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variable ***
${URL_API}         http://api.gerenciame.com/v1
#{TOKEN} 
#${APP_KEY}      njMf2EiyQ17g6C3vLUxk1yEsWTforVqf
#${APP_SECRET}   EgpTuUcM93IqHY8icgR3cK6Cn4bOlkQwSlfLd6ryMjrhhwMW

*** Keywords ***
#Conectar a API
    #Create Session    gerenciame    ${URL_API}

# Ações 
#### DADO
que estamos realizando uma request para o endpoint tarefas-get
    Create Session    gerenciame    ${URL_API}

#### QUANDO
preenchermos o queryParam ""
    #TO-DO
realizarmos a chamada    
${RESPOSTA}    Get Request    gerenciame    /tarefas
    Log            ${RESPOSTA.text}

#### ENTÃO
o status da chamada sera "200"
    [Arguments]    ${STATUS_CODE_ESPERADO}
    Should Be Equal As Strings    ${RESPOSTA.status_code}    ${STATUS_CODE_ESPERADO}

o retorno sera de sucesso    



##Cenário 02 Depreciado em 12/04/2019 devido atualização na API
# Nenhum dado deve ser mostrado para o CEP "${CEP}"
#     Confere o status code       200
#     Confere endereço do CEP     ${EMPTY}
#     Confere bairro do CEP       ${EMPTY}
#     Confere cidade do CEP       ${EMPTY}
#     Confere UF do CEP           ${EMPTY}
#     Confere CEP                 ${CEP}

A mensagem de erro "${MSG_ERRO}" deve ser retornada
    Confere o status code       200
    Confere mensagem de erro    ${MSG_ERRO}

#### PASSOS
Conecta ao WebService
    Create Session      consultaCEP     ${HOST}

Realiza requisição do CEP
    [Arguments]         ${CEP_DESEJADO}
    ${RESPOSTA}=        Get Request  consultaCEP  /${CEP_DESEJADO}/?app_key=${APP_KEY}&app_secret=${APP_SECRET}
    Log                 Resposta: ${RESPOSTA.text}
    Set Test Variable   ${RESPOSTA}

Confere o status code
    [Arguments]     ${STATUS_ESPERADO}
    Should Be Equal As Strings   ${RESPOSTA.status_code}  ${STATUS_ESPERADO}
    Log             Status Code Retornado: ${RESPOSTA.status_code} -- Status Code Esperado: ${STATUS_ESPERADO}

Confere endereço do CEP
    [Arguments]         ${ENDERECO}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  endereco   ${ENDERECO}

Confere bairro do CEP
    [Arguments]         ${BAIRRO}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  bairro   ${BAIRRO}

Confere cidade do CEP
    [Arguments]         ${CIDADE}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  cidade   ${CIDADE}

Confere UF do CEP
    [Arguments]         ${UF}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  uf   ${UF}

Confere CEP
    [Arguments]         ${CEP}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  cep   ${CEP}

Confere mensagem de erro
    [Arguments]         ${MSG_ERRO}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  error   ${MSG_ERRO}
