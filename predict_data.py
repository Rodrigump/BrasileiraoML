import pandas as pd
from sklearn.linear_model import LinearRegression

from get_data import *
from prepare_data import *

if __name__ == '__main__':

    #Download da base histórica

    start = 1995

    end = 2024

    #treino

    #years = [download_data_from_source(year, 'train') for year in range(start, end)]

    #teste

    download_data_from_source(end, 'test')

    #Tratamento dos dados e geração dos datasets

    train = set_train_dataset()

    test = set_test_dataset()

    #Modelo preditivo

    labels = ['Posicao', 'Pts', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG'] #Variáveis utilizadas

    X = train[labels]

    y = train['Pts_Final']

    lr = LinearRegression()
    
    lr.fit(X, y)

    print('Variáveis\t', labels)

    coef = lr.coef_

    print('Coeficientes\t', coef)

    score = lr.score(X, y)

    print('Score\t', score)

    pred = lr.predict(test[labels])

    #DataFrame com a predição

    clube = test['Clube'].tolist()

    pts = [int(i) for i in pred.tolist()]

    df = pd.DataFrame({'Clube': clube, 'Pts': pts}).sort_values(by="Pts", ascending=False)

    df.index = range(1,21)

    print(df)
