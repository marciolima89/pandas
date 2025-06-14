# Bibliotecas necessárias
import pandas as pd


# funcao
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores[['score', 'rank']]
    return scores


# dados para inserir
dados_scores = [
    [1, 3.50],
    [2, 3.65],
    [3, 4],
    [4, 3.85],
    [5, 4],
    [6, 3.65]
]

colunas_score = ['id', 'score']

scores = pd.DataFrame(dados_scores, columns=colunas_score).astype(
    {'id': int, 'score': float})
scores['rank'] = scores['score'].rank(
    method='dense', ascending=False).astype(int)
scores = scores.sort_values(by='rank', ascending=True)

df = order_scores(scores)
print(df)
