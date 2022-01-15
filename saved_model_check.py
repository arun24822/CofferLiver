import joblib
m_jlib = joblib.load('saved_model')
print(m_jlib.predict(([[32,1,38.5,52.5,7.7,22.1,7.5,6.93,3.23,106,12.1,69]])))
print(m_jlib.predict_proba(([[32,1,38.5,52.5,7.7,22.1,7.5,6.93,3.23,106,12.1,69]])))