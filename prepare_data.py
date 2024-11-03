import os
import pandas as pd

#Prepara o DataFrame do conjunto de treino
def set_train_dataset(folder='./train/'):

    train_dfs = []

    for file in os.listdir(folder):
        df = pd.read_csv(folder+file)
        train_dfs.append(df)

    train_df = pd.concat(train_dfs)

    #Dados até a 37ª rodada de cada edição

    train_df1 = train_df.loc[train_df['Rodada'] < 38]

    #Dados da última rodada de cada edição

    train_df2 = train_df.loc[train_df['Rodada'] == 38, ['Clube', 'Ano', 'Posicao', 'Pts']]

    #Join dos dois dataframes

    train_curated_df = pd.merge(train_df1, train_df2, on=['Clube', 'Ano'])

    train_curated_df['GP'] = train_curated_df['Gols'].str.split(':').str[0]

    train_curated_df['GC'] = train_curated_df['Gols'].str.split(':').str[1]

    train_dataset = train_curated_df.rename(columns={'Posicao_x': 'Posicao', 'Pts_x': 'Pts', 'Posicao_y': 'Posicao_Final', 'Pts_y': 'Pts_Final'})

    return train_dataset

#Prepara o DataFrame do conjunto de teste
def set_test_dataset(folder='./test/'):

    test_dfs = []

    for file in os.listdir(folder):
        df = pd.read_csv(folder+file)
        test_dfs.append(df)

    test_df = pd.concat(test_dfs)

    test_labels = ['Clube', 'Rodada', 'Posicao', 'Pts', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG']

    test_df['GP'] = test_df['Gols'].str.split(':').str[0]

    test_df['GC'] = test_df['Gols'].str.split(':').str[1]

    test_dataset = test_df.loc[test_df['Rodada'] == 38, test_labels]

    return test_dataset
