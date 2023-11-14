# Documento de Visão

____

# Calculadora de Combustível

## 1. Introdução

### 1.1. Resumo

### 1.2. Escopo

Principais responsabilidades e não responsabilidades do sistema.

#### Responsabilidades

- Estimar a quantidade de combustível que será necessário para um percurso;
- Estimar a distãncia a ser percorrida entre dois pontos;
- Indicar as principais vias de uma boa rota para transitar entre dois pontos.

#### Não-responsabilidades

- Garantir acesso total no caso de perda de conexão com a internet.
- Permitir que os usuários conversem entre si.
- Garantir a melhor rota.

## 2. Requisitos

### 2.1. Requisitos Funcionais

| ckeck | Cod | Nome                                            | Descrição                                                                                       |
|-------|-----|-------------------------------------------------|-------------------------------------------------------------------------------------------------|
| ✅     | F01 | Entrada das Coordenadas                         | O sistema deve permitir que os usuários informem as coordenadas de dois pontos para o sistema.  |
| ✅     | F02 | Entrada da Média de Consumo                     | O sistema deve permitir que os usuários informem a Média de Consumo do Veículo                  |
| ✅     | F02 | Seleção de inclusão da viagem de volta          | O sistema deve permitir que os usuários informem se desejam incluir a viagem de volta           |
| ✅     | F03 | Validação de dados no Frontend                  | O Frontend deve validar os dados digitados e reportar erro                                      |
| ✅     | F03 | Validação de dados no Backend                   | O Backend deve validar os dados recebidos na requisição e reportar erro                         |
| ✅     | F04 | Comunicação com API do Mapbox                   | O Backend consome a API do Mapbox para consultas                                                |
| ✅     | F05 | Tratamento de exceções                          | O Backend trata vários tipos de exceções previsíveis e notifica o usuário                       |
| ✅     | F06 | Apresentação de Relatório da Viagem             | O usuário recebe o Relatório da viagem entre os pontos                                          |
| ✅     | F07 | Relatório da Viagem tem a distância             | O Relatório da viagem inclui a distância estimada da rota                                       |
| ✅     | F08 | Relatório da Viagem tem a quant. de combustível | O Relatório da viagem inclui a quantidade estimada de combustível para a viagem                 |
| ✅     | F09 | Link para o Repositório                         | O usuário tem acesso ao link do repositório dos arquivos do projeto                             |
| ✅     | F10 | Repositório versionado                          | Os arquivos do projeto são versionados com Git                                                  |
| ✅     | F11 | As regras de negócio são testadas no Backend    | O sistema possui uma boa cobertura de testes automatizados para as regras de negócio do Backend |
| ✅     | F12 | As regras de negócio são testadas no Frontend   | O sistema possui testes automatizados para as regras de negócio no frontend                     |

### 2.2. Requisitos Não-funcionais

| check | Cod  | Nome                                        | Descrição                                                                                                |
|-------|------|---------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ✅     | NF01 | Reports de erro sem recarregar a página     | Os erros encontrados, na validação dos dados informados, são notificados sem recarregar a página inteira |
| ✅     | NF02 | Status das operações são notificados        | Cada operação realizada pelo sistema dispara um aviso na interface do usuário                            |
| ✅     | NF03 | Impedimento de envio de formulário inválido | O formulário permite o envio apenas após ter seos campos validados                                       |
| ✅     | NF04 | Programação Orientada a Objetos             | As informações são mapeadas para instãncias de objetos                                                   |
| ✅     | NF05 | Disponibilização de App                     | Configuração de PWA                                                                                      |
| ✅     | NF06 | Uma Paleta de Cores                         | A interface possui uma paleta de cores bem definida                                                      |
| ✅     | NF07 | Uma logo                                    | A interface possui uma logomarca definida                                                                |
| ✅     | NF08 | Layout responsivo                           | a interface possui um layout responsivo bem desenhado                                                    |
| ✅     | NF09 | apresentação da imagem do percurso          | O Percurso é representado por uma imagem no mapa embutido na interface do usuário                        |

