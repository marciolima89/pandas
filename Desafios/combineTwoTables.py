# Importar bibliotecas necessarias
import pandas as pd


# Criar funcao
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on='personId', how='left')
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result


# Criando df de pessoas
dados_psa = [
    [1, 'Wang', 'Allen'],
    [2, 'Alice', 'Bob']
]
col_psa = ['personId', 'lastName', 'firstName']
person = pd.DataFrame(dados_psa, columns=col_psa).astype(
    {'personId': 'int64', 'lastName': 'string', 'firstName': 'string'})

# Criando df de endereços
dados_ads = [
    [1, 2, 'New York City', 'New York'],
    [2, 3, 'Leetcode', 'New York']
]
col_ads = ['addressId', 'personId', 'city', 'state']
address = pd.DataFrame(dados_ads, columns=col_ads).astype(
    {'addressId': 'int64', 'personId': 'int64', 'city': 'string', 'state': 'string'})

# Resultado
# print('Dataframe de pessoas: \n', person, '\n')
# print('Dataframe de enderecos: \n', address)
df = combine_two_tables(person, address)
df = df.fillna('NULL')
print(df)
