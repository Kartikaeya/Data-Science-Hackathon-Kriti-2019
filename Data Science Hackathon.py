

# # importing important packages




import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# # Loading Data



dataset = pd.read_csv('training_data.csv')
#print(dataset)
X = dataset.drop(columns = ['Salary'],axis =1)
#y = dataset.iloc[:,2]
test = pd.read_csv('testing_data.csv')
#print(X)
print(test)





X.info()


# # Feature Engineering




y = dataset.iloc[:,2]
#print(y)





for col in ['Gender','10board','12graduation','12board', 'CollegeID', 'CollegeTier']:
    X[col]=X[col].astype('category')
    
for col in ['Degree', 'Specialization','CollegeCityID','CollegeCityTier', 'CollegeState', 'GraduationYear', 'English',
       'Logical', 'Quant', 'Domain']:
    X[col]=X[col].astype('category')
    
for col in ['Gender','10board','12graduation','12board', 'CollegeID', 'CollegeTier','Degree', 'Specialization','CollegeCityID','CollegeCityTier', 'CollegeState', 'GraduationYear', 'English',
       'Logical', 'Quant', 'Domain']:
    X[col]=X[col].cat.codes
    
X['JobCity']=X['JobCity'].astype('category')
X['JobCity']=X['JobCity'].cat.codes





for col in ['JobCity','Gender','10board','12graduation','12board', 'CollegeID', 'CollegeTier','Degree', 'Specialization','CollegeCityID','CollegeCityTier', 'CollegeState', 'GraduationYear', 'English',
       'Logical', 'Quant', 'Domain']:
    X[col]=X[col].astype('category')
    X[col]=X[col].cat.codes
print(X)    





for col in ['JobCity','Gender','10board','12graduation','12board', 'CollegeID', 'CollegeTier','Degree', 'Specialization','CollegeCityID','CollegeCityTier', 'CollegeState', 'GraduationYear', 'English',
       'Logical', 'Quant', 'Domain']:
    test[col]=test[col].astype('category')
    test[col]=test[col].cat.codes
print(test)    




X = X.drop([ 'Unnamed: 0' , 'ID' ,'DOB'],axis = 1)
print(X)





test = test.drop([ 'Unnamed: 0' , 'ID' ,'DOB'],axis = 1)
print(test)





test.info()





print(X)


# # Model fitting and Data Splitting




from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)





print(x_train)
print(y_train)
print(x_test)
print(y_test)


# # Evaluating Metrics








params = {}
params['learning_rate'] = 0.029
#params['boosting_type'] = 'gbdt'
params['objective'] = 'gamma'
params['metric'] = 'l2'
params['sub_feature'] = 0.55
params['num_leaves'] = 40
params['min_data'] = 50
#params['max_depth'] = 30
print(params)
import lightgbm as lgb
d_train = lgb.Dataset(X, label = y)
clf = lgb.train( params,d_train, 100)
#Prediction
y_pred=clf.predict(test)

y_pred =1.1* y_pred

print(y_pred)





print(pd.DataFrame(y_pred ))

