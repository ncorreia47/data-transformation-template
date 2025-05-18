# Strategy Method para transformação de dados

O objetivo desse código foi ilustrar a importância de design patterns no desenvolvimento de Pipelines de Dados.
O código refatorado era utilizado na etapa de ELT em ambiente de produção, através do serviço de Cloud Functions dentro do ambiente Google Cloud.
A ideia da refatoração para adotar o Strategy Method foi uma alternativa para alguns dos problemas encontrados na versão antiga do código, que utilizava método de implementação
de Template Method.

## Escopo:
Para abstrair toda a lógica de negócio do código em produção, foi desenvolvido um código para receber dados de um dataframe e convertê-lo para um arquivo json.
Por isso, os seguintes passos foram definidos para construir esse processo:
- Criar o template method para simular a versão original do código
- Desenvolver as estratégias de refatoração para adequar-se ao Strategy Method
- Implementar métodos para não violação dos principios SOLID, pois Template method:
  - OCP (Open/Closed Principle): exige herança para extensão, e não composição.
  - LSP (Liskov Substitution Principle): suas subclasses devem manter o comportamento esperado da classe base, o que pode ser violado se métodos abstratos forem implementados de forma muito diferente.
  - SRP (Single Responsibility Principle): sua classe base pode acabar assumindo responsabilidades demais (validação, caminho, exportação).

## Desenvolvimento da refatoração

### Lógica aplicada
Para realizar a refatoração do código em Template Method para Strategy Method, foi necessário:
 - Definir as strategies do código, pois as interfaces construídas precisam incluir os métodos através de composição e não herança
 - Separar as responsabilidades das classes principais
 - Desenvolver templates para abstrair as complexidades inerentes aos tipos de arquivos utilizados. Nesse exemplo, foi desenvolvido o template **dataframe_to_json**

### Estrutura do projeto
O projeto está organizado da seguinte maneira:
```bash
src/
└── core        # define a classe de exportar dataframes
├── interface   # implementa as estratégias definidas
├── templates   # abstrai a complexidade dos tratamentos de arquivos (como no caso, json-like)
└── utils       # arquivos de utilidades

```
  
