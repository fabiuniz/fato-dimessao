#pip install pandas numpy matplotlib seaborn scikit-learn statsmodels

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import date, timedelta
import warnings

warnings.filterwarnings('ignore') # Ignorar warnings para melhor visualização

# =============================================================================
# 1. LIMPEZA / TRATAMENTO DOS DADOS
# =============================================================================

def simulardados():
	# Defina a semente para reprodutibilidade
	np.random.seed(42)
	# Defina as categorias e o intervalo de datas
	categorias = [
	    'GASOLINA', 'MERCADO', 'RESTAURANTE', 'REMEDIOS', 'BANCO', 'IMPRESSORA', 
	    'CONDOMINIO', 'PAPELARIA', 'PIZZARIA', 'MECANICO', 'TELEFONE', 'FEIRA', 
	    'INTERNET'
	]
	data_inicio = date(2024, 7, 1)
	data_fim = date(2025, 6, 30)
	# Crie uma lista de datas entre o intervalo definido
	datas = [data_inicio + timedelta(days=x) for x in range((data_fim - data_inicio).days + 1)]
	# Crie os dados simulados
	n_transacoes = 200 # Aumente o número de transações para uma simulação mais robusta
	dados_simulados = {
	    'Data': np.random.choice([d.strftime('%d/%m/%Y') for d in datas], n_transacoes),
	    'Categoria': np.random.choice(categorias, n_transacoes),
	    'Valor': np.round(np.random.uniform(-500, -10, n_transacoes), 2)
	}
	# Crie o DataFrame
	df_simulado = pd.DataFrame(dados_simulados)
	# Converta o DataFrame para uma string no formato desejado
	dados_string_simulados = df_simulado.to_csv(sep=';', index=False, header=True, float_format='%.2f')
	return dados_string_simulados

dados_string = """Data;Categoria;Valor
01/07/2024;GASOLINA;-39,77
01/07/2024;MERCADO;-209,21
01/07/2024;RESTAURANTE;-67,8
01/08/2024;MERCADO;-35,51
01/08/2024;REMEDIOS;-48,96
01/11/2024;REMEDIOS;-39,12
02/04/2025;BANCO;-7,76
02/04/2025;BANCO;-79
02/05/2025;BANCO;-7,76
02/07/2024;BANCO;-7,76
02/07/2024;BANCO;-79
02/08/2024;BANCO;-7,76
02/08/2024;BANCO;-79
02/08/2024;GASOLINA;-148,31
02/09/2024;BANCO;-7,76
02/09/2024;GASOLINA;-100
02/10/2024;BANCO;-7,76
02/10/2024;BANCO;-79
02/12/2024;BANCO;-7,76
03/01/2025;BANCO;-79
03/02/2025;BANCO;-7,76
03/09/2024;BANCO;-79
03/09/2024;MERCADO;-73,25
03/10/2024;IMPRESSORA;-20
03/10/2024;IMPRESSORA;-230
03/12/2024;BANCO;-79
04/02/2025;BANCO;-79
04/07/2024;MERCADO;-115,33
04/10/2024;MERCADO;-62,16
04/11/2024;BANCO;-7,76
04/11/2024;BANCO;-79
04/11/2024;MERCADO;-113,44
04/11/2024;REMEDIOS;-71,23
04/11/2024;RESTAURANTE;-46,9
05/03/2025;BANCO;-7,76
05/05/2025;BANCO;-79
05/05/2025;PIZZARIA;-46
05/05/2025;RESTAURANTE;-70
05/08/2024;PAPELARIA;-37,28
06/03/2025;BANCO;-79
06/05/2025;MERCADO;-43,52
06/08/2024;GASOLINA;-106,67
07/04/2025;CONDOMINIO;-529,76
07/04/2025;RESTAURANTE;-71
07/08/2024;RESTAURANTE;-31
07/10/2024;PAPELARIA;-12,1
07/11/2024;REMEDIOS;-15,9
08/05/2025;CONDOMINIO;-529,76
08/07/2024;MECANICO;-80
08/07/2024;MERCADO;-36,75
08/11/2024;MERCADO;-27,08
09/04/2025;MERCADO;-21,9
09/09/2024;GASOLINA;-100
09/09/2024;MERCADO;-729,94
09/09/2024;RESTAURANTE;-12
09/09/2024;RESTAURANTE;-58
09/09/2024;RESTAURANTE;-73,9
09/12/2024;PIZZARIA;-103
10/02/2025;PIZZARIA;-114
10/07/2024;PIZZARIA;-36
10/10/2024;MERCADO;-736,55
11/07/2024;MERCADO;-175,99
12/03/2025;MERCADO;-19,99
12/05/2025;MERCADO;-47,54
12/05/2025;RESTAURANTE;-56
12/08/2024;GASOLINA;-67,49
12/08/2024;PIZZARIA;-28
13/11/2024;MERCADO;-33,34
13/11/2024;MERCADO;-53,45
14/01/2025;MERCADO;-42,48
14/01/2025;REMEDIOS;-12,7
14/04/2025;MERCADO;-42,26
14/04/2025;RESTAURANTE;-79,9
14/05/2025;MERCADO;-16,99
14/08/2024;MERCADO;-78,53
14/10/2024;MERCADO;-47,33
14/10/2024;TELEFONE;-129
14/10/2024;TELEFONE;-1449,00
15/01/2025;MERCADO;-51,96
16/04/2025;MERCADO;-61,75
16/09/2024;GASOLINA;-100
16/09/2024;PAPELARIA;-30,7
16/10/2024;REMEDIOS;-16,28
16/10/2024;REMEDIOS;-208,66
16/10/2024;REMEDIOS;-90,99
17/02/2025;MERCADO;-238,25
17/02/2025;MERCADO;-47,05
17/02/2025;PIZZARIA;-87
17/02/2025;RESTAURANTE;-47,9
17/03/2025;MECANICO;-300
17/03/2025;MERCADO;-61,37
17/03/2025;REMEDIOS;-57,22
17/07/2024;MERCADO;-63,4
18/07/2024;RESTAURANTE;-22
18/10/2024;MERCADO;-16,07
18/11/2024;PIZZARIA;-80
19/02/2025;MERCADO;-49,03
19/03/2025;MERCADO;-13,76
19/03/2025;MERCADO;-24,48
19/05/2025;FEIRA;-35,98
19/05/2025;MERCADO;-53,01
19/05/2025;PIZZARIA;-52
19/08/2024;GASOLINA;-188,71
19/08/2024;MECANICO;-200
19/08/2024;PIZZARIA;-73
19/11/2024;MERCADO;-58,91
19/12/2024;MERCADO;-19,86
20/01/2025;MERCADO;-26,17
20/01/2025;PIZZARIA;-42
20/01/2025;PIZZARIA;-99
20/08/2024;MERCADO;-73,1
20/12/2024;MERCADO;-515,44
21/10/2024;REMEDIOS;-47,67
21/11/2024;MERCADO;-48,77
22/01/2025;MERCADO;-33,11
22/04/2025;MERCADO;-44,03
22/04/2025;MERCADO;-98,98
22/04/2025;PAPELARIA;-35,1
22/07/2024;MERCADO;-124,57
22/11/2024;MERCADO;-41,68
23/01/2025;MERCADO;-40,71
23/01/2025;REMEDIOS;-25,18
23/04/2025;MERCADO;-16,99
23/05/2025;MERCADO;-51,65
23/09/2024;REMEDIOS;-104,99
23/09/2024;REMEDIOS;-200
23/10/2024;MERCADO;-39,69
23/10/2024;REMEDIOS;-71,6
23/10/2024;TELEFONE;-128
23/10/2024;TELEFONE;-58,83
23/10/2024;TELEFONE;-58,83
24/02/2025;MERCADO;-38,52
24/09/2024;MERCADO;-12,88
25/04/2025;MERCADO;-816,05
25/07/2024;TELEFONE;-128
25/07/2024;TELEFONE;-63
25/07/2024;TELEFONE;-63
25/09/2024;MERCADO;-28,71
25/09/2024;TELEFONE;-128
25/09/2024;TELEFONE;-70
25/09/2024;TELEFONE;-70
25/11/2024;PIZZARIA;-42
26/03/2025;INTERNET;-130,59
26/03/2025;TELEFONE;-51,01
26/03/2025;TELEFONE;-51,01
26/05/2025;INTERNET;-158,71
26/05/2025;RESTAURANTE;-67
26/05/2025;TELEFONE;-135
26/05/2025;TELEFONE;-54
26/05/2025;TELEFONE;-54
26/08/2024;GASOLINA;-219,25
26/08/2024;PIZZARIA;-98
26/08/2024;RESTAURANTE;-78
26/08/2024;TELEFONE;-128
26/08/2024;TELEFONE;-70
26/08/2024;TELEFONE;-70
27/01/2025;MERCADO;-10,98
27/01/2025;PAPELARIA;-570,9
27/05/2025;MERCADO;-28,75
27/09/2024;MERCADO;-17,79
28/04/2025;INTERNET;-135
28/04/2025;TELEFONE;-54
28/04/2025;TELEFONE;-54
28/10/2024;PIZZARIA;-99
28/10/2024;REMEDIOS;-29,99
28/10/2024;REMEDIOS;-41,88
28/10/2024;REMEDIOS;-89,36
28/11/2024;MERCADO;-26,02
29/04/2025;MERCADO;-47,82
29/05/2025;MERCADO;-11,28
29/05/2025;MERCADO;-29,73
29/07/2024;GASOLINA;-116,95
29/07/2024;MERCADO;-106,49
29/07/2024;MERCADO;-61,11
29/07/2024;PIZZARIA;-93
30/04/2025;MERCADO;-19,97
30/09/2024;MERCADO;-17,56
30/09/2024;PIZZARIA;-65
30/09/2024;REMEDIOS;-34,8
30/09/2024;REMEDIOS;-532,18
31/03/2025;MERCADO;-54,98
31/03/2025;PAPELARIA;-48,3
31/03/2025;PIZZARIA;-51
31/03/2025;RESTAURANTE;-83,5
"""

#dados_string = simulardados()

# =============================================================================
# 1. IDENTIFICAÇÃO FATOS x DIMENSÕES
# =============================================================================

# Carregar os dados
from io import StringIO
df = pd.read_csv(StringIO(dados_string), sep=';')

# Converter a coluna 'Data' para datetime
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Converter a coluna 'Valor' para numérico, substituindo ',' por '.'
df['Valor'] = df['Valor'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# Remover o sinal negativo do valor para análise de despesas
df['Valor'] = df['Valor'].abs()

# Exibir as primeiras linhas e tipos de dados
print("Primeiras linhas do DataFrame:")
print(df.head())
print("\nTipos de dados:")
print(df.info())

# Tabela Fato: Despesas
# Adicionar colunas de tempo para análise sazonal e agregação
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month
df['Dia'] = df['Data'].dt.day
df['Dia_da_Semana'] = df['Data'].dt.day_name()

fato_despesas = df[['Data', 'Ano', 'Mes', 'Dia', 'Dia_da_Semana', 'Categoria', 'Valor']].copy()

# Tabela Dimensão: Categorias
# Podemos adicionar atributos às categorias se tivéssemos mais informações (ex: tipo de categoria, subcategoria)
dim_categoria = df[['Categoria']].drop_duplicates().reset_index(drop=True)
dim_categoria['ID_Categoria'] = dim_categoria.index

# =============================================================================
# 2. CLASSIFICADOR DE TIPOS DE ANÁLISE
# =============================================================================

# A. Análise Descritiva: O que aconteceu?
# B. Análise Diagnóstica: Por que aconteceu?
# C. Análise Preditiva: O que pode acontecer?
# D. Análise Prescritiva: O que deve ser feito?
# E. Análise Sazonal: Existem padrões ao longo do tempo?

# =============================================================================
# 3. EXPLORADOR FATOS x DIMENSÕES
# =============================================================================

# Juntar a dimensão à fato para ter o ID da categoria (exemplo de como faríamos em um DW)
# Para este exercício, a própria string da categoria já serve como identificador
fato_despesas = pd.merge(fato_despesas, dim_categoria, on='Categoria', how='left')

print("\nTabela Fato - Despesas (com novas colunas de tempo e ID_Categoria):")
print(fato_despesas.head())
print("\nTabela Dimensão - Categorias:")
print(dim_categoria.head())

# =============================================================================
# 4. FERRAMENTAS DE VISUALIZAÇÃO
# =============================================================================

# Gráfico de Barras
# Gráfico de Linhas
# Boxplot
# (Essas visualizações são geradas e agrupadas no dashboard abaixo)

# =============================================================================
# 5. DASHBOARD PRINCIPAL
# =============================================================================

# Criação do dashboard com múltiplas visualizações
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Despesas por Mês (Barras)
despesas_mensais_serie_plot = fato_despesas.groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum()
despesas_mensais_serie_plot.index = despesas_mensais_serie_plot.index.strftime('%b %Y')
sns.barplot(x=despesas_mensais_serie_plot.index, y=despesas_mensais_serie_plot.values, ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Despesas por Mês')
axes[0, 0].set_xlabel('Mês')
axes[0, 0].set_ylabel('Valor Total (R$)')
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Despesas por Categoria (Barras horizontais)
despesas_por_categoria_plot = fato_despesas.groupby('Categoria')['Valor'].sum().sort_values()
sns.barplot(x=despesas_por_categoria_plot.values, y=despesas_por_categoria_plot.index, ax=axes[0, 1], palette='plasma')
axes[0, 1].set_title('Despesas por Categoria')
axes[0, 1].set_xlabel('Valor Total (R$)')
axes[0, 1].set_ylabel('Categoria')

# 3. Evolução temporal (Linha)
sns.lineplot(x=despesas_mensais_serie_plot.index, y=despesas_mensais_serie_plot.values, ax=axes[1, 0], marker='o', color='darkorange')
axes[1, 0].set_title('Evolução Temporal das Despesas')
axes[1, 0].set_xlabel('Mês')
axes[1, 0].set_ylabel('Valor Total (R$)')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Distribuição Quantidade (Boxplot)
sns.boxplot(x='Categoria', y='Valor', data=fato_despesas, ax=axes[1, 1], palette='tab10')
axes[1, 1].set_title('Distribuição de Valores por Categoria (Boxplot)')
axes[1, 1].set_xlabel('Categoria')
axes[1, 1].set_ylabel('Valor (R$)')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()


# =============================================================================
# ANÁLISE COMPLETA
# =============================================================================

print("\n--- Análise Descritiva ---")

# Despesas totais
total_despesas = fato_despesas['Valor'].sum()
print(f"Despesa total no período: R$ {total_despesas:,.2f}")

# Média de despesas por transação
media_por_transacao = fato_despesas['Valor'].mean()
print(f"Média de despesas por transação: R$ {media_por_transacao:,.2f}")

# Top 5 Categorias com maiores despesas
print("\nTop 5 Categorias com maiores despesas:")
despesas_por_categoria = fato_despesas.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
print(despesas_por_categoria.head())

# Despesas mensais
despesas_mensais = fato_despesas.groupby(['Ano', 'Mes'])['Valor'].sum().unstack(fill_value=0)
print("\nDespesas mensais:")
print(despesas_mensais)

# Visualização: Despesas por Categoria
plt.figure(figsize=(12, 6))
sns.barplot(x=despesas_por_categoria.index, y=despesas_por_categoria.values, palette='viridis')
plt.title('Despesas Totais por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Visualização: Tendência Mensal de Despesas
despesas_mensais_serie = fato_despesas.groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum()
plt.figure(figsize=(12, 6))
despesas_mensais_serie.plot(kind='line', marker='o')
plt.title('Tendência Mensal de Despesas')
plt.xlabel('Data')
plt.ylabel('Valor Total (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()


print("\n--- Análise Diagnóstica ---")

# Vamos investigar o pico de despesas em 'MERCADO'
# Identificar o mês com a maior despesa em MERCADO
mercado_pico_mes = fato_despesas[fato_despesas['Categoria'] == 'MERCADO'].groupby(['Ano', 'Mes'])['Valor'].sum().idxmax()
print(f"\nMês com a maior despesa em MERCADO: {mercado_pico_mes}")

# Detalhar as transações de MERCADO no mês de pico (ex: 2024, 10)
# Ajuste o ano e mês conforme o resultado de mercado_pico_mes
ano_pico, mes_pico = mercado_pico_mes
transacoes_pico_mercado = fato_despesas[
(fato_despesas['Categoria'] == 'MERCADO') &
(fato_despesas['Ano'] == ano_pico) &
(fato_despesas['Mes'] == mes_pico)
].sort_values(by='Valor', ascending=False)
print(f"\nDetalhes das transações de MERCADO em {mes_pico}/{ano_pico}:")
print(transacoes_pico_mercado)

# Se houver valores muito discrepantes, podemos identificá-los como outliers
# Usando o IQR para identificar outliers em 'MERCADO'
q1 = fato_despesas[fato_despesas['Categoria'] == 'MERCADO']['Valor'].quantile(0.25)
q3 = fato_despesas[fato_despesas['Categoria'] == 'MERCADO']['Valor'].quantile(0.75)
iqr = q3 - q1
outlier_upper_bound = q3 + 1.5 * iqr
outlier_mercado = fato_despesas[
(fato_despesas['Categoria'] == 'MERCADO') &
(fato_despesas['Valor'] > outlier_upper_bound)
]
print(f"\nTransações de MERCADO consideradas outliers (acima de R$ {outlier_upper_bound:,.2f}):")
print(outlier_mercado)

# Análise de proporção de despesas
total_mensal = fato_despesas.groupby(['Ano', 'Mes'])['Valor'].sum()
proporcao_categoria_mensal = fato_despesas.groupby(['Ano', 'Mes', 'Categoria'])['Valor'].sum().unstack(fill_value=0)
proporcao_categoria_mensal = proporcao_categoria_mensal.div(total_mensal, axis=0) * 100

print("\nProporção das despesas por categoria em cada mês (top 3 categorias com maior valor em cada mês):")
for idx, row in proporcao_categoria_mensal.iterrows():
	top_3 = row.nlargest(3)
	if not top_3.empty:
		print(f"\n{idx[1]}/{idx[0]}:")
		print(top_3.apply(lambda x: f"{x:.2f}%"))


		print("\n--- Análise Preditiva ---")

# Previsão de despesas totais futuras
# Agrupar por mês e somar os valores
despesas_por_mes = fato_despesas.groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum().reset_index()
despesas_por_mes['Mes_Num'] = (despesas_por_mes['Data'].dt.year - despesas_por_mes['Data'].dt.year.min()) * 12 + despesas_por_mes['Data'].dt.month

X = despesas_por_mes[['Mes_Num']]
y = despesas_por_mes['Valor']

# Dividir os dados em treino e teste (opcional para conjuntos de dados pequenos)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Prever o próximo mês (o último mês em Mes_Num + 1)
proximo_mes_num = despesas_por_mes['Mes_Num'].max() + 1
previsao_proximo_mes = model.predict([[proximo_mes_num]])

# Calcular a data do próximo mês para exibição
ultima_data = fato_despesas['Data'].max()
proxima_data_previsao = ultima_data + pd.DateOffset(months=1)

print(f"\nPrevisão de despesa total para {proxima_data_previsao.strftime('%B/%Y')}: R$ {previsao_proximo_mes[0]:,.2f}")

# PREVISÃO DE DESPESAS PARA UMA CATEGORIA ESPECÍFICA (EX: MERCADO)
despesas_mercado_por_mes = fato_despesas[fato_despesas['Categoria'] == 'MERCADO'].groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum().reset_index()

if not despesas_mercado_por_mes.empty:
    despesas_mercado_por_mes['Mes_Num'] = (despesas_mercado_por_mes['Data'].dt.year - despesas_mercado_por_mes['Data'].dt.year.min()) * 12 + despesas_mercado_por_mes['Data'].dt.month

    X_mercado = despesas_mercado_por_mes[['Mes_Num']]
    y_mercado = despesas_mercado_por_mes['Valor']

    # Treinar um novo modelo para a categoria MERCADO
    model_mercado = LinearRegression()
    model_mercado.fit(X_mercado, y_mercado)

    # Prever o próximo mês para MERCADO
    proximo_mes_num_mercado = despesas_mercado_por_mes['Mes_Num'].max() + 1
    previsao_mercado_proximo_mes = model_mercado.predict([[proximo_mes_num_mercado]])

    print(f"Previsão de despesa para a categoria 'MERCADO' em {proxima_data_previsao.strftime('%B/%Y')}: R$ {previsao_mercado_proximo_mes[0]:,.2f}")
else:
    print("Não há dados suficientes para prever despesas para a categoria 'MERCADO'.")

# Visualização da previsão
plt.figure(figsize=(12, 6))
plt.scatter(X, y, label='Despesas Reais')
plt.plot(X, model.predict(X), color='red', label='Linha de Regressão')
plt.scatter(proximo_mes_num, previsao_proximo_mes, color='green', s=100, label=f'Previsão para {proxima_data_previsao.strftime("%m/%Y")}')
plt.title('Previsão de Despesas Totais Mensais')
plt.xlabel('Número do Mês (a partir do início dos dados)')
plt.ylabel('Valor Total (R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()        


print("\n--- Análise Prescritiva ---")

# Cenário 1: Redução de gastos em categorias de alto impacto
print("\nRecomendações para redução de despesas:")
top_categoria = despesas_por_categoria.index[0]
top_valor = despesas_por_categoria.values[0]

print(f"- A categoria '{top_categoria}' é a de maior despesa (R$ {top_valor:,.2f}). Considere estratégias para reduzir gastos nesta área, como: ")
if top_categoria == 'MERCADO':
	print("  - Elaborar lista de compras e segui-la rigorosamente.")
	print("  - Comparar preços em diferentes estabelecimentos.")
	print("  - Evitar compras por impulso.")
elif top_categoria == 'TELEFONE':
	print("  - Avaliar planos de celular mais econômicos.")
	print("  - Utilizar Wi-Fi sempre que possível para chamadas e dados.")
	print("  - Controlar o uso de aplicativos que consomem muitos dados.")
elif top_categoria == 'RESTAURANTE' or top_categoria == 'PIZZARIA':
	print("  - Cozinhar mais em casa e levar marmita para o trabalho/escola.")
	print("  - Limitar a frequência de saídas para comer fora.")
else:
	print(f"  - Analisar as despesas específicas dentro de '{top_categoria}' para identificar oportunidades de economia.")

# Cenário 2: Estabelecimento de um orçamento
print("\nRecomendação: Estabelecer um orçamento mensal baseado na média histórica e previsão.")
media_mensal_historica = despesas_mensais_serie.mean()
print(f"- A média de despesas mensais históricas é de R$ {media_mensal_historica:,.2f}.")
print(f"- Com base na previsão, sugere-se um orçamento para o próximo mês de aproximadamente R$ {previsao_proximo_mes[0]:,.2f}.")
print("- Monitore as despesas regularmente para garantir que o orçamento está sendo seguido.")

# Cenário 3: Alerta para outliers
if not outlier_mercado.empty:
	print("\nAlerta: Foram identificadas transações de MERCADO significativamente altas (outliers).")
	print("  - Revise estas transações para entender o motivo (ex: compra grande, erro de registro).")
	print("  - Se forem gastos recorrentes e altos, reavalie a necessidade e busque alternativas.")



	print("\n--- Análise Sazonal ---")

# Agrupar despesas por mês do ano (ignorando o ano específico para encontrar padrões sazonais)
despesas_por_mes_do_ano = fato_despesas.groupby('Mes')['Valor'].sum()

print("\nDespesas totais por mês do ano:")
print(despesas_por_mes_do_ano.sort_index())

# Visualização: Despesas por Mês do Ano
plt.figure(figsize=(10, 5))
sns.barplot(x=despesas_por_mes_do_ano.index, y=despesas_por_mes_do_ano.values, palette='plasma')
plt.title('Padrão Sazonal de Despesas por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor Total (R$)')
plt.xticks(ticks=np.arange(12), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.tight_layout()
plt.show()

# Análise de decomposição de série temporal (requer mais dados para ser muito eficaz)
# Vamos tentar, mas com dados limitados o resultado pode não ser ideal
# Reindexar a série para garantir que não há lacunas e preencher com 0
serie_sazonal = fato_despesas.set_index('Data').resample('M')['Valor'].sum().fillna(0)

if len(serie_sazonal) > 2 * 12: # Mínimo de 2 anos para decomposição mensal
    decomposition = seasonal_decompose(serie_sazonal, model='additive', period=12) # Assumindo sazonalidade anual

    fig = decomposition.plot()
    fig.set_size_inches(12, 8)
    plt.suptitle('Decomposição Sazonal das Despesas', y=1.02)
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.show()

    # Identificar meses comumente mais caros
    print("\nMeses com maior tendência de despesas (baseado na média mensal histórica):")
    media_despesas_por_mes_calendario = fato_despesas.groupby(fato_despesas['Data'].dt.month)['Valor'].mean()
    print(media_despesas_por_mes_calendario.sort_values(ascending=False).head())
else:
	print("\nDados insuficientes para uma decomposição sazonal robusta (mínimo de 2 anos de dados recomendado).")
	print("Para essa amostra, a visualização 'Padrão Sazonal de Despesas por Mês' já fornece insights sazonais.")

# Análise de despesas por dia da semana
despesas_por_dia_semana = fato_despesas.groupby('Dia_da_Semana')['Valor'].sum()
# Reordenar para uma visualização mais lógica da semana
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
despesas_por_dia_semana = despesas_por_dia_semana.reindex(ordem_dias)

print("\nDespesas totais por dia da semana:")
print(despesas_por_dia_semana)

plt.figure(figsize=(10, 5))
sns.barplot(x=despesas_por_dia_semana.index, y=despesas_por_dia_semana.values, palette='coolwarm')
plt.title('Despesas Totais por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()    