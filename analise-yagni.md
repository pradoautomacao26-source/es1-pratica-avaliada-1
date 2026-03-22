# Análise do princípio YAGNI

## O que é YAGNI

YAGNI significa "You Aren't Gonna Need It", ou seja, você não deve implementar funcionalidades que não são necessárias no momento.

## Atributos desnecessários

A classe Usuario possui atributos que não são necessários para os requisitos atuais, como:
- telefone
- endereço
- foto de perfil
- data de nascimento
- preferências

Esses atributos violam YAGNI porque não são usados nas funcionalidades exigidas.

## Métodos desnecessários

Também existem métodos que não são necessários:
- editar perfil
- adicionar amigos
- remover amigos
- gerar relatórios
- integração com redes sociais

Esses métodos aumentam a complexidade sem necessidade.

## Por que isso é um problema

Adicionar funcionalidades desnecessárias:
- aumenta a complexidade
- dificulta manutenção
- gera mais chances de erro
- atrasa o desenvolvimento

## Conclusão

O ideal é manter apenas o necessário: cadastro, login e listagem de usuários, garantindo um sistema simples e eficiente.
