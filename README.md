# Projeto-Integrador-grupo34
Projeto Integrador TADS - ETL e análise de dados do agronegócio Brasileiro com dashboard em Streamlit. 
# Projeto Integrador Grupo 34

## Objetivo da Análise
Explorar dados do agronegócio brasileiro, realizando um processo de ETL (Extract, Transform, Load) e construindo um dashboard interativo em Streamlit para análise e visualização dos resultados.

## Integrantes
- Integrante A – Organização inicial
- Integrante B – Coleta de dados
- Integrante C – Tratamento dos dados
- Integrante D – Dashboard interativo

## Planejamento das Tarefas

- **Tarefa 1 – Organização inicial**  
  Responsável: Integrante Ícaro Juliano de Deus 
  Descrição: Criar o repositório no GitHub, configurar a estrutura de pastas (`data`, `src`, `app`), adicionar o `README.md` inicial e incluir os colaboradores do grupo.

- **Tarefa 2 – Coleta de dados (ETL – Extract)**  
  Responsável: Integrante William Pessoa 
  Descrição: Pesquisar e baixar datasets relevantes sobre o agronegócio brasileiro, organizar os arquivos brutos na pasta `data/` e documentar a origem dos dados no README.

- **Tarefa 3 – Tratamento dos dados (ETL – Transform)**  
  Responsável: Integrante Abner Luan  
  Descrição: Criar scripts Python em `src/etl.py` para limpeza, normalização e transformação dos dados, salvando os resultados tratados em `data/processed/`.

- **Tarefa 4 – Dashboard interativo (Load + Visualização)**  
  Responsável: Integrante Luiz Griebler  
  Descrição: Desenvolver o aplicativo Streamlit em `app/dashboard.py`, conectar aos dados tratados e implementar gráficos e tabelas interativas para análise.

## Estrutura de Pastas

- Projeto-Integrador-grupo34/
  - data/ → dados brutos e processados
    - raw/ → dados originais
    - processed/ → dados tratados
  - src/ → scripts Python para ETL
    - etl.py
  - app/ → dashboard em Streamlit
    - dashboard.py
  - .gitignore → arquivos/pastas ignorados pelo Git
  - README.md → documentação do projeto
