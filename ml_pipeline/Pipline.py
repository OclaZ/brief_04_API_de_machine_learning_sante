import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def load_data():   
    path = "data.csv"
    df = pd.read_csv(path)
    return df

df = load_data()

target_column = "status"
x=df.drop(columns=[target_column])
y=df[target_column]
cat_columns = x.select_dtypes(exclude=['int64', 'float64']).columns
num_columns = x.select_dtypes(include=['int64', 'float64']).columns


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_columns),
        ('cat',  LabelEncoder(), cat_columns)
    ])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model',  SVC())
])

SVC_param_grid = [
    {
        'model__C': [0.1, 1, 10],
        'model__kernel': ['linear', 'rbf'],
        'model__gamma': ['scale', 'auto']
    }
]
svc_grid = GridSearchCV(pipeline,SVC_param_grid,cv=5, n_jobs=-1, scoring ='accuracy')

svc_grid.fit(x_train, y_train)
machy_best_model = svc_grid.best_estimator_
test_accuracy = machy_best_model.score(x_test, y_test)
# print(f"Test Accuracy: {test_accuracy}")


## random forest regressor

if y.dtype == 'object':
    label = LabelEncoder()
    y = label.fit_transform(y)

preprocessor1 = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_columns),
        ('cat',  OneHotEncoder(handle_unknown='ignore'), cat_columns)
    ])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor1),
    ('model',  RandomForestClassifier())
])

RF_param_grid = [
    {
        'model__n_estimators': [100, 200],
        'model__max_depth': [None, 10, 20],
        'model__min_samples_split': [2, 5]
    }
]
rf_grid = GridSearchCV(pipeline,RF_param_grid,cv=5, n_jobs=-1, scoring ='accuracy')  
rf_grid.fit(x_train, y_train)
best_model = rf_grid.best_estimator_
test_accuracy2 = best_model.score(x_test, y_test)
print(f"Test random foresst regression classifier: {test_accuracy2}")


## Save the best model
joblib.dump(best_model, 'model_lhcen.pkl')
joblib.load('model_lhcen.pkl')
loaded_model = joblib.load('model_lhcen.pkl')
result = loaded_model.score(x_test, y_test)
print(f"Loaded model test accuracy: {result}")