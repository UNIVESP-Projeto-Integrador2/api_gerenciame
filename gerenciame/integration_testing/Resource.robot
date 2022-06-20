*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variable ***
${URL_API}         http://api.gerenciame.com/v1
#{TOKEN} 
#${APP_KEY}      njMf2EiyQ17g6C3vLUxk1yEsWTforVqf
#${APP_SECRET}   EgpTuUcM93IqHY8icgR3cK6Cn4bOlkQwSlfLd6ryMjrhhwMW
${RESPONSE_BODY}    

*** Keywords ***
#Conectar a API
    #Create Session    gerenciame    ${URL_API}

# Ações 
#### DADO
que estamos realizando uma request para o endpoint tarefas-get
    Create Session    gerenciame    ${URL_API}

#### QUANDO
preenchermos os queryParams "${DATA_INICIAL}" e "${DATA_FINAL}"
    #TO-DO
realizarmos a chamada    
${RESPOSTA}    Get Request    gerenciame    /tarefas
    Log            ${RESPOSTA.text}
    Set Test Variable    ${RESPOSTA} 

#### ENTÃO
o status da chamada sera "200"
    [Arguments]    ${STATUS_CODE_ESPERADO}
    Should Be Equal As Strings    ${RESPOSTA.status_code}    ${STATUS_CODE_ESPERADO}

o retorno sera de sucesso    


Confere UF do CEP
    [Arguments]         ${UF}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  uf   ${UF}

Confere CEP
    [Arguments]         ${CEP}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  cep   ${CEP}

Confere mensagem de erro
    [Arguments]         ${MSG_ERRO}
    Dictionary Should Contain Item  ${RESPOSTA.json()}  error   ${MSG_ERRO}
