# Previsor de Média Móvel
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/getrolucas/moving-average-forecast/blob/master/LICENSE) 

-----

Previsor de Média Móvel é um projeto cujo objetivo é produzir previsões simplificadas de séries temporais usando a técnica de médias móveis.

-----

## Exemplo de uso simples:
```bash
from moving_average_forecaster import moving_average

# Crie o objeto m
m = moving_average(df, freq='M', periods=6)

# Crie um DataFrame com as datas futuras
future_df = m.make_future_dataframe()

# Gere as previsões
predictions = m.predict(
    future=future_df, 
    response_col='y', 
    window=3
)
```

## Exemplo de uso em escala:
```bash
from moving_average_forecaster import moving_average

# Crie um dataframe vazio para armezenar os resultados
df_final = pd.DataFrame()

# Loop para todas as categorias
for categoria in df.Categorias.unique():
    df_base = df[df['Categoria'] == categoria].reset_index(drop=True)
    
    # Modelo
    m = moving_average(df=df_base, periods=12)

    future = m.make_future_dataframe()
    
    df_predict = m.predict(
        future=future, 
        response_col='y', 
        window=3,
        dimension_col=True, 
        dimension_col_name='Categorias'
    )
    
    df_final = pd.concat((df_final, df_predict), ignore_index=True)
```
## Resultado:
```bash
# Plotando dados históricos e previsão
df_final[df_final['Categorias'] == df.Categorias.unique()[0]].plot(x='ds')

```
![output](https://github.com/getrolucas/moving-average-forecast/blob/master/moving-forecast-example.png)
