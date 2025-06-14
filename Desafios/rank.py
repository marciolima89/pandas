# Bibliotecas necessárias
import pandas as pd

# Dados para input
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |

# informar a quantidade de registros que serao inseridos
n = int(input('Quantos registros serão inseridos? '))
print(n)

# preencher listas
id_list = []
score_list = []

# popular os dados na lista
for i in range(n):
    # garantir que o ID será único
    while True:
        add_id = int(input('Informe ID do usuário: '))
        if add_id in id_list:
            print(
                f"O id '{add_id}' inserido já foi cadastrado, favor adicionar um novo")
        else:
            break
    # orientar para inserção do tipo float
    while True:
        try:
            add_score = float(input('Informe pontuação do usuário: '))
            break
        except ValueError:
            print("O valor inserido não é do tipo float. Substitua vírgula por ponto")

    id_list.append(add_id)
    score_list.append(add_score)

dados = {"id": id_list, "score": score_list}
df = pd.DataFrame(dados)
df = df.set_index('id')

# criar coluna de rank
df['rank'] = df['score'].rank(method='dense', ascending=False).astype(int)
df = df.sort_values(by='score', ascending=False)

print(df[['score', 'rank']])
