import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler, RobustScaler


def ohe_col(df: pd.DataFrame, col_name) -> pd.DataFrame:
    """
    범주형 텍스트 데이터를 숫자로 변환

    변환된 데이터list를 기존 DataFrame에 concat하는 함수

    Parameters
    ----------
    df
        범주형데이터가 속한 DataFrame

    col_name
        범주형데이터의 column 이름

    return
    ------
    pd.DataFrame
        인코딩한 범주형 데이터를 기존 DataFrame에 병합하여 return
    """
    ohe = OneHotEncoder()
    ohe_arr = np.array(df[col_name])
    ohe_arr = np.reshape(ohe_arr, (-1, 1))

    ohe_name = ohe.fit_transform(ohe_arr)
    ohe_df = pd.DataFrame(ohe_name.toarray(), columns=ohe.get_feature_names_out())
    df.drop(col_name, axis=1, inplace=True)
    df = pd.concat([df, ohe_df], axis=1)

    return df


def dataset_split(df: pd.DataFrame, label):
    """
    독립변수와 종속변수 분리

    Parameters
    ----------
    df
        분리하고자 하는 DataFrame
    label
        종속변수 지정

    Return
    ------
    (x, y)
        x
            독립변수들

        y
            종속변수
    """
    x = df.drop(label, axis=1)
    y = df[label]

    return (x, y)


class scaling:

    def __init__(self, train, test):

        ss = StandardScaler()
        norm = Normalizer()
        ms = MinMaxScaler()
        rs = RobustScaler()

        self.ss_train = ss.fit_transform(train)
        self.ss_test = ss.transform(test)

        self.norm_train = norm.fit_transform(train)
        self.norm_test = norm.transform(test)

        self.ms_train = ms.fit_transform(train)
        self.ms_test = ms.transform(test)

        self.rs_train = rs.fit_transform(train)
        self.rs_test = rs.transform(test)
