import requests
import json

response = requests.get("http://api.gerenciame.com/v1/tarefas",
                        params={'data_inicio': '2022-06-19', 'data_final': '2022-06-19'})
print(response.text)
print(type(response.text))

# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]['id_tarefa'])

json_response = response.json()
print(type(json_response))
print(json_response['tarefas'][0]['id_tarefa'])
assert response.status_code == 200
response.headers


{
    "tarefas": [
        {
            "id_tarefa": 2147483647,
            "nome_tarefa": "string",
            "data_inicial": "7976-05-23",
            "data_limite": "4071-12-30",
            "hora": "11:49",
            "descricao": "string",
            "status": 100,
            "subtarefas": [
                {
                    "id_subtarefa": 2147483647,
                    "nome_subtarefa": "string",
                    "anexo_subtarefa": "string",
                    "status_subtarefa": "a fazer"
                }
            ]
        }
    ]
}
