# Xperf

O Xperf é um projeto de aplicação que permite a coleta e análise eficiente de informações de desempenho de redes. Ele foi desenvolvido para realizar testes de ping e testes de velocidade de internet, armazenar os resultados em um banco de dados MySQL e fornecer insights valiosos sobre a qualidade da conexão. Com essa ferramenta, é possível monitorar e avaliar a estabilidade e a velocidade da rede de forma centralizada.

## Principais Recursos

- Coleta detalhada de informações sobre equipamentos, incluindo marca, modelo e endereço MAC.
- Realização automatizada de testes de ping para destinos específicos.
- Execução periódica de testes de velocidade de internet (download/upload).
- Armazenamento seguro e organizado dos resultados em um banco de dados MySQL.
- Análise e visualização intuitiva dos dados coletados para tomadas de decisões informadas.

## Motivação

O projeto Xperf surgiu da necessidade de simplificar e agilizar a avaliação de desempenho de redes, permitindo a identificação de possíveis gargalos e problemas de conectividade. Com uma estrutura flexível e adaptável, o Xperf se torna uma ferramenta versátil para profissionais de TI, administradores de rede e entusiastas que desejam otimizar a experiência online.

## Instalação e Uso

### Pré-requisitos

- Python 3.x
- Bibliotecas Python: ping3, speedtest-cli, tqdm, mysql-connector-python

### Instalação

1. Clone este repositório para a sua máquina local:

git clone https://github.com/SEU_USUARIO/Xperf.git


2. Instale as dependências do projeto:


### Configuração

1. Crie um banco de dados MySQL e defina suas credenciais no arquivo `main.py` e `database_functions.py`.
2. Use o script no repositorio para criar as tabelas necessárias no banco de dados:
3. Execute o arquivo `main.py` para coletar e armazenar os dados.

## Uso

1. Execute o arquivo `main.py` para iniciar a coleta de dados.
2. Acompanhe o progresso dos testes exibidos no terminal.
3. Os resultados serão armazenados no banco de dados e estarão disponíveis para análise posterior.

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicia a coleta de dados.
- `ping_functions.py`: Funções relacionadas à realização de testes de ping.
- `speed_test_functions.py`: Funções relacionadas à realização de testes de velocidade.
- `database_functions.py`: Funções relacionadas à interação com o banco de dados.
- `README.md`: Este arquivo de documentação.

## Contribuição

Contribuições são bem-vindas! Se você deseja adicionar recursos, corrigir problemas ou melhorar a documentação, fique à vontade para fazer um fork deste repositório, implementar suas melhorias e enviar um pull request. Juntos, podemos aprimorar o Xperf e torná-lo ainda mais poderoso.

## Licença

Este projeto é licenciado sob a Licença MIT.

---

Criado por Thiago Alves da Silva Filho - thiagof2755@gmail.com
