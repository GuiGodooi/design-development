import pandas as pd

carros = {
    'Marca' : ['Opel', 'Mini', 'Ferrari'],
    'Modelo' : ['Astra', 'Cooper', 'F40'],
    'Ano' : ['22', '24', '98'],
}

df_carros = pd.DataFrame(carros)
df_carros.to_excel('carros.xlsx')