# Desafio - Melhorando o sistema bancário do projeto anterior

## Objetivos
 Melhorar o sistema bancario anterio adicionando um menu para cadastrar usuário e outro para criar conta referente a esse usuário. Também trabalhar com os as passagens de parametros do tipo posicional e por keypair.

## Premissas
 1. Cliente pode ter um unico cadastro, porém varias contas associadas a ele
 2. Cada conta funciona de forma independente
 3. Na função de saque, os parametros devem ser passados somente por keypair
 4. Na função de deposito, os parametros devem ser passados somente usando posição
 5. Saques tem limites de máximo de R$ 500.00, só podem ser realizado 3 vezes ao dia (não há necessidade de controle do dia) e é necessário ter dinheiro em conta para permitir a operação
 6. A operação de Extrato precisa apresentar todas as operações realizadas pelo usuário, incluindo os resultados. Se nenhuma operação foi executada, ainda uma mensagem dizendo que nenhuma operação foi executada deve ser apresentada. 


 