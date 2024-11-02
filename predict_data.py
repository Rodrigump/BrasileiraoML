import pandas as pd
from sklearn.linear_model import LinearRegression

from prepare_data import *

if __name__ == '__main__':

    #Tratamento dos dados e geração dos datasets

    train = set_train_dataset()

    test = set_test_dataset()

    #Modelo preditivo

    labels = ['Rodada', 'Posicao', 'Pts', 'V', 'E', 'D', 'GP', 'GC'] #Variáveis utilizadas

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
