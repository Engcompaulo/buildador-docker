#!/usr/bin/env python3.10
#Python 3.10
import sys
import json
import yaml

parameters = sys.argv[:]
envs = json.loads(parameters[1])

print(envs)
saida = json.dumps(envs, indent=4)
print(saida)

with open('projetos.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service['projetos'][1])


#################### Exemplo to use in Terminal  ################
''' 
python3.10 buildador.py '{"name": "prod 1"}'
python3.10 buildador.py '{"name": "home-nodered"}'

'''