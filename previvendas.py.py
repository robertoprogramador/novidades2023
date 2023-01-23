#!/usr/bin/env python
# coding: utf-8

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# 
# - Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

# ### Passo a Passo de um Projeto de Ciência de Dados
# 
# - Passo 1: Entendimento do Desafio
# - Passo 2: Entendimento da Área/Empresa
# - Passo 3: Extração/Obtenção de Dados
# - Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# - Passo 5: Análise Exploratória
# - Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
# - Passo 7: Interpretação de Resultados

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# - TV, Jornal e Rádio estão em milhares de reais
# - Vendas estão em milhões

# #### Importar a Base de dados

# In[ ]:


#*importar a base de dados para o python
#*visualizar a base de dados e fazer os ajustes nela
#*análise exploratória;entender como a base de dados está se comportando
#*criar a inteligencia artificial e fazer as previsões


# In[3]:


#*importar a base de dados para o python
import pandas as pd

tabela = pd.read_csv("advertising.csv")
display(tabela)


# #### Análise Exploratória
# - Vamos tentar visualizar como as informações de cada item estão distribuídas
# - Vamos ver a correlação entre cada um dos itens

# In[4]:


get_ipython().system('pip install scikit-learn')


# In[5]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')


# In[7]:


#plotli, matplotli e seaborn
tabela.corr()


# In[8]:


#tabela em forma de gráfico
import seaborn as sns
import matplotlib.pyplot as plt
#criar o grafico
sns.heatmap(tabela.corr(),annot=True, cmap="Wistia")


# #### Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# 
# - Separando em dados de treino e dados de teste

# In[9]:


#y-> quem voce quer prever->vendas
#x -> o resto dos dados
y = tabela[["Vendas"]]
x = tabela[["TV","Radio","Jornal"]]

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)


# In[10]:


y


# In[11]:


x


# #### Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# 
# - Regressão Linear
# - RandomForest (Árvore de Decisão)

# In[12]:


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


# In[13]:


#criar a inteligencia artificial e fazer as previsões
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


# In[14]:


modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


# #### Teste da AI e Avaliação do Melhor Modelo
# 
# - Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece

# In[15]:


#testar pra ver qual inteligencia artificial é melhor
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))


# #### Visualização Gráfica das Previsões

# In[16]:


previsao_arvoredecisao


# In[17]:


tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['previsoes Arvore de Decisao'] = previsao_arvoredecisao
tabela_auxiliar['Previsoes Regressao Linear'] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)


# #### Como fazer uma nova previsão?

# In[18]:


novos=pd.read_csv("novos.csv")
display(novos)


# In[19]:


#modelo vencedor foi a Arvore de decisão
previsao=modelo_arvoredecisao.predict(novos)
print(previsao)


# In[ ]:





# In[ ]:




