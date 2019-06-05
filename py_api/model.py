import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df_ = df[include]


categories = []
for col, col_type in df_.dtypes.iteritems():
	if col_type != 'O':
		df_[col].fillna(0, inplace=True)
	else:
		categories.append(col)

df_ohe = pd.get_dummies(df_, columns = categories, dummy_na=True)

dependent_var = 'Survived'
x = df_ohe[df_ohe.columns.difference([dependent_var])]
y = df_ohe[dependent_var]
lr = LogisticRegression()
lr.fit(x,y)

joblib.dump(lr, 'model.pkl')
print("dumped model")

lr = joblib.load('model.pkl')
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("dumped columns")