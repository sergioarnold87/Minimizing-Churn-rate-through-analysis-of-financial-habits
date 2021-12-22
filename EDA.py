#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:15:45 2021

@author: sergio
"""

# Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

dataset = pd.read_csv('churn_data.csv')

# Analisis Exploratorio de los datos

dataset.head(5)
dataset.columns
dataset.describe()

# Limpiar los datos
dataset[dataset.credit_score < 300]
dataset = dataset[dataset.credit_score >=300]

# Eliminar los NaN
dataset.isna().any()
dataset.isna().sum()
dataset = dataset.drop(columns = ['credit_score', 'rewards_earned'])

## Histogramas

dataset2 = dataset.drop(columns = ['user', 'churn'])
fig = plt.figure(figsize=(15,12))
plt.suptitle('Histograma de las columnas numéricas', fontsize = 20)
for i in range(1, dataset2.shape[1] + 1):
    plt.subplot(6,5,i)
    f = plt.gca()
    f.axes.get_yaxis().set_visible(False)
    f.set_title(dataset2.columns.values[i-1])
    
    vals = np.size(dataset2.iloc[:, i-1].unique())
    
    plt.hist(dataset2.iloc[:, i-1], bins = vals, color ='#3F5D7D')
plt.tight_layout(rect = [0, 0.03, 1, 0.95])


    

