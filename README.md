# Projeto-Integrador-grupo34
Projeto Integrador TADS - ETL e análise de dados do agronegócio Brasileiro com dashboard em Streamlit. 
# Projeto Integrador Grupo 34

## Objetivo da Análise
Explorar dados do agronegócio brasileiro, realizando um processo de ETL (Extract, Transform, Load) e construindo um dashboard interativo em Streamlit para análise e visualização dos resultados.

## Integrantes
- ICARO JULIANO DE DEUS – Organização inicial
- WILLIAM GONCALVES PESSOA– Coleta de dados
- ABNER LUAN CARVALHO BONFIM – Tratamento dos dados
- LUIZ HENRIQUE PAOLUCCI MOURA GRIEBLER DOS SANTOS – Dashboard interativo

## Planejamento das tarefas e cronograma 

- **Tarefa 1 – Organização inicial**  
  Responsável: Integrante Ícaro Juliano de Deus 
  Descrição: Criar o repositório no GitHub, configurar a estrutura de pastas (`data`, `src`, `app`), adicionar o `README.md` inicial e incluir os colaboradores do grupo, prazo de entrega 17/03/2026.

- **Tarefa 2 – Coleta de dados (ETL – Extract)**  
  Responsável: Integrante William Pessoa 
  Descrição: Pesquisar e baixar datasets relevantes sobre o agronegócio brasileiro, organizar os arquivos brutos na pasta `data/` e documentar a origem dos dados no README, prazo de entrega 20/03/2026 .

- **Tarefa 3 – Tratamento dos dados (ETL – Transform)**  
  Responsável: Integrante Abner Luan  
  Descrição: Criar scripts Python em `src/etl.py` para limpeza, normalização e transformação dos dados, salvando os resultados tratados em `data/processed/`, prazo de entrega 21/03/2026.

- **Tarefa 4 – Dashboard interativo (Load + Visualização)**  
  Responsável: Integrante Luiz Griebler  
  Descrição: Desenvolver o aplicativo Streamlit em `app/dashboard.py`, conectar aos dados tratados e implementar gráficos e tabelas interativas para análise, prazo de entrega 22/03/2026.

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
## Tema do projeto
Analise da produção agricola no Brasil 
## Base de dados 
Dataset obtido no kaggle( adicionar possiveis links para estudo e destacar o link que sera usado no projeto)
Contem informações por estado.
## Objetivo 
Mostrar a produção agricola por estado, permitindo comparações regionais e evolução ao longo dos anos
## planejamento 
-ETL: limpeza e padronização do dados 
-Análise: estatistica e graficos por estado
-Dashboard: visualização interativa em Streamlit
Fluxo resumido:  
`
Kaggle → Extração → Limpeza/Transformação → Dados tratados → Dashboard Streamlit
## Ideia inicial do Dashboard
O Dashboard será desenvolvido em Streamlit e apresentará:
- Grafico de barras mostrando a produção agrícola por estado.
- Linha do tempo com a evolução da produção ao longo dos anos.
- filtros interativos para selecionar estados e culturas por específicas.
- Indicadores numéricos (KPIs) com totais e médias de produção.
