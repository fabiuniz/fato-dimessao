<!-- 
  Tags: DadosIA
  Label: 🧱 Fato Dimenssão - Análise de Despesas Pessoais com Python
  Description:🌍 Analise de Dados - Fato Dimensão
  technical_requirement: Python, pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels, Git
  path_hook: hookfigma.hook1
-->

# 📊 Análise de Despesas Pessoais com Python

Um sistema completo de análise de dados financeiros pessoais que transforma dados brutos de transações em insights acionáveis para gestão inteligente do orçamento familiar.

<p align="center">
  <img src="/images/screenshot.png" alt="imagem do Projeto">
</p>

## 🎯 Objetivos do Projeto

Este projeto demonstra como aplicar técnicas avançadas de análise de dados para:
- **Compreender** padrões de gastos pessoais
- **Identificar** oportunidades de economia
- **Prever** despesas futuras
- **Otimizar** o orçamento familiar
- **Detectar** anomalias e gastos atípicos

## 🛠️ Tecnologias Utilizadas

```python
# Bibliotecas principais
pandas          # Manipulação e análise de dados
numpy           # Computação numérica
matplotlib      # Visualização de dados
seaborn         # Visualizações estatísticas avançadas
scikit-learn    # Machine learning (regressão linear)
statsmodels     # Análise estatística e decomposição temporal
```

## 📋 Estrutura da Análise

### 1. 🧹 Preparação e Limpeza dos Dados
- Conversão de formatos (datas, valores monetários)
- Tratamento de dados inconsistentes
- Padronização de categorias de despesas
- Criação de variáveis temporais (ano, mês, dia da semana)

### 2. 🏗️ Modelagem Dimensional (Fato x Dimensão)
- **Tabela Fato**: `fato_despesas` - armazena transações com dimensões temporais
- **Tabela Dimensão**: `dim_categoria` - metadados das categorias de despesa
- Estrutura otimizada para análises multidimensionais

### 3. 📈 Cinco Pilares da Análise de Dados

#### 🔍 **Análise Descritiva** - "O que aconteceu?"
- Despesa total do período
- Médias por categoria e período
- Distribuição de gastos
- Rankings de categorias mais custosas

#### 🔬 **Análise Diagnóstica** - "Por que aconteceu?"
- Identificação de picos de despesas
- Detecção de outliers usando IQR
- Análise de proporções mensais
- Investigação de transações atípicas

#### 🔮 **Análise Preditiva** - "O que pode acontecer?"
- Regressão linear para previsão de gastos futuros
- Modelos específicos por categoria
- Projeções baseadas em tendências históricas
- Validação cruzada dos modelos

#### 💡 **Análise Prescritiva** - "O que deve ser feito?"
- Recomendações personalizadas de economia
- Estabelecimento de orçamentos inteligentes
- Alertas para gastos excessivos
- Estratégias específicas por categoria

#### 📅 **Análise Sazonal** - "Existem padrões temporais?"
- Decomposição de séries temporais
- Padrões mensais e semanais
- Identificação de sazonalidades
- Tendências de longo prazo

## 📊 Dashboard Interativo

O projeto gera automaticamente um dashboard com quatro visualizações principais:

1. **Despesas Mensais** - Evolução temporal dos gastos
2. **Ranking por Categoria** - Identificação dos maiores custos
3. **Tendência Temporal** - Linha de evolução dos gastos
4. **Distribuição por Categoria** - Boxplots para análise de dispersão

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

### Execução
```python
# O código já inclui dados simulados para demonstração
python fato_dimensao.py
```

### Personalizando com Seus Dados
Para usar seus próprios dados, substitua a variável `dados_string` pelo formato:
```
Data;Categoria;Valor
01/07/2024;MERCADO;-150,50
02/07/2024;GASOLINA;-80,00
```

## 📈 Principais Insights Gerados

### 🎯 Análise Automática
- **Top 5 categorias** com maiores despesas
- **Mês de maior gasto** e suas causas
- **Previsões** para o próximo mês (geral e por categoria)
- **Recomendações específicas** baseadas nos padrões identificados

### 📊 Visualizações Geradas
- Gráficos de evolução temporal
- Comparativos por categoria
- Análise de sazonalidade
- Detecção visual de outliers

## 🔧 Funcionalidades Avançadas

### 🤖 Machine Learning Integrado
- Regressão linear para previsões
- Detecção automática de outliers
- Análise de tendências

### 📅 Análise Temporal Sofisticada
- Decomposição sazonal quando há dados suficientes
- Análise por dia da semana
- Padrões mensais recorrentes

### 💰 Gestão Inteligente
- Cálculo automático de orçamentos sugeridos
- Alertas para gastos atípicos
- Recomendações personalizadas

## 📋 Exemplo de Saída

```
--- Análise Descritiva ---
Despesa total no período: R$ 15,234.56
Média de despesas por transação: R$ 87.43

Top 5 Categorias com maiores despesas:
MERCADO        4,567.89
TELEFONE       2,134.56
GASOLINA       1,876.54
RESTAURANTE    1,456.78
CONDOMINIO     1,234.56

--- Análise Preditiva ---
Previsão de despesa total para Julho/2025: R$ 1,456.78
Previsão para categoria 'MERCADO' em Julho/2025: R$ 456.78

--- Análise Prescritiva ---
Recomendações para redução de despesas:
- A categoria 'MERCADO' é a de maior despesa...
```

## 🎓 Aplicações Educacionais

Este projeto serve como um **caso de estudo completo** para:
- Estudantes de Data Science
- Profissionais de análise financeira
- Desenvolvedores Python interessados em análise de dados
- Qualquer pessoa interessada em gestão financeira pessoal

## 🔄 Extensões Possíveis

- Integração com APIs bancárias
- Interface web com Streamlit ou Dash
- Alertas automáticos por email/SMS
- Análise comparativa com benchmarks
- Categorização automática usando NLP
- Previsões com modelos mais sofisticados (ARIMA, Prophet)

## 📚 Metodologia Científica

O projeto segue as melhores práticas de análise de dados:
- **Reprodutibilidade**: Seed fixado para resultados consistentes
- **Validação**: Separação treino/teste nos modelos preditivos
- **Visualização**: Gráficos informativos e profissionais
- **Documentação**: Código amplamente comentado
- **Modularidade**: Estrutura organizada e reutilizável

---

## 👨‍💻 Autor

[Fabiano Rocha/Fabiuniz](https://github.com/SeuUsuarioGitHub)

## 📄 Licença

Este projeto é disponibilizado sob licença MIT. Sinta-se livre para usar, modificar e distribuir.
