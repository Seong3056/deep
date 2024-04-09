# 제시된 여행 보험 예측 데이터에서 TravelInsurance(여행보험 패키지를 구매 했는지 여부) 를 예측하는 모델을 개발하고
# 모델 개발 과정과 테스트 데이터셋에 대한 auc 를 답안으로 작성하시오


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    ExtraTreesClassifier,
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("./data/travel_insurance_prediction.csv")


df.head()


df.info()
# 결측값은 없음
# 오브젝트는 분석을 통해 인코딩 또는 드랍여부 판단


df.describe()
# 데이터간 크기가 상이하므로 스케일링이 필요


df["Employment Type"].value_counts()


df["GraduateOrNot"].value_counts()


df["FrequentFlyer"].value_counts()


df["EverTravelledAbroad"].value_counts()


df_corr = df.corr(numeric_only=True)
sns.heatmap(
    df_corr,
    cbar=True,
    annot=True,
    square=True,
    fmt=".2f",
    annot_kws={"size": 10},
    yticklabels=df_corr,
    xticklabels=df_corr,
)


# - AnnualIncome 의 영향이 가장 큼


# 인코딩할 컬럼들 이름 가져오기
object_columns = df.select_dtypes(include="object").columns.tolist()


object_columns_reshape = np.reshape(object_columns, (-1, 1))

for column in object_columns_reshape:
    ohe = OneHotEncoder()
    ohe_arr = np.array(df[column])
    ohe_arr = np.reshape(ohe_arr, (-1, 1))

    ohe_name = ohe.fit_transform(ohe_arr)
    ohe_df = pd.DataFrame(
        ohe_name.toarray(), columns=ohe.get_feature_names_out(input_features=column)
    )
    df = pd.concat([df, ohe_df], axis=1)


df.head()


x = df.drop("TravelInsurance", axis=1)
y = df["TravelInsurance"]


x_train, x_test, y_train, y_test = train_test_split(
    x, y, stratify=df[object_columns], random_state=3056
)


x_train.shape, x_test.shape


x_train.drop(object_columns, axis=1, inplace=True)
x_test.drop(object_columns, axis=1, inplace=True)


ss = StandardScaler()
scaled_train = ss.fit_transform(x_train)
scaled_test = ss.transform(x_test)


# # 의사결정나무


dt = DecisionTreeClassifier(random_state=3056)
dt.fit(scaled_train, y_train)
print(dt.score(scaled_train, y_train))
print(dt.score(scaled_test, y_test))


scores = cross_validate(
    dt,
    scaled_train,
    y_train,
    return_train_score=True,
    n_jobs=-1,
    cv=8,
    scoring="roc_auc",
)

print(np.mean(scores["train_score"]))
print(np.mean(scores["test_score"]))


# # 랜덤포레스트


rf = RandomForestClassifier(
    n_estimators=300, oob_score=True, n_jobs=-1, random_state=3056
)


scores = cross_validate(
    rf,
    scaled_train,
    y_train,
    return_train_score=True,
    n_jobs=-1,
    cv=8,
    scoring="roc_auc",
)

print(np.mean(scores["train_score"]))
print(np.mean(scores["test_score"]))


# # 엑스트라 트리


et = ExtraTreesClassifier(n_jobs=-1, random_state=3056)
scores = cross_validate(
    et,
    scaled_train,
    y_train,
    return_train_score=True,
    n_jobs=-1,
    cv=8,
    scoring="roc_auc",
)

print(np.mean(scores["train_score"]))
print(np.mean(scores["test_score"]))


# # 그레디언트 부스팅


gb = GradientBoostingClassifier(random_state=3056, n_estimators=300, learning_rate=0.09)

scores = cross_validate(
    gb,
    scaled_train,
    y_train,
    return_train_score=True,
    n_jobs=-1,
    cv=8,
    scoring="roc_auc",
)

print(np.mean(scores["train_score"]))
print(np.mean(scores["test_score"]))


gb.fit(scaled_train, y_train)


gb.feature_importances_
