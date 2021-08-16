import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error

@st.cache()
def prediction(car_data, car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick):
    X = car_data.iloc[:, :-1] 
    y = car_data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 

    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    score = lin_reg.score(X_train, y_train)

    price = lin_reg.predict([[car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick]])
    price = price[0]

    y_test_pred = lin_reg.predict(X_test)
    test_r2_score = r2_score(y_test, y_test_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)
    test_msle = mean_squared_log_error(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

    return price, score, test_r2_score, test_mae, test_msle, test_rmse

def app(car_data):
    st.markdown("<p style='color:red;font-size:20px'> Linear Regression for Car Price Prediction </p>",unsafe_allow_html = True)

    feat_list2 = ['car_width', 'engine_size', 'horse_power', 'drive_wheel_fwd', 'car_comp_buick']

    car_width = st.sidebar.slider(feat_list2[0],float(car_data['carwidth'].min()),float(car_data['carwidth'].max()))

    engine_size = st.sidebar.slider(feat_list2[1],float(car_data['enginesize'].min()),float(car_data['enginesize'].max()))

    horse_power = st.sidebar.slider(feat_list2[2],float(car_data['horsepower'].min()),float(car_data['horsepower'].max()))

    # S2.2: Define the 'app()' function as directed above.
    drw_fwd = st.radio("Is it a forward drive wheel car?", ('Yes','No'))
    if drw_fwd == 'No':
        drw_fwd = 0
    else:
        drw_fwd = 1
    
    com_bui = st.radio("Is the car manufactured by Buick?", ("Yes", "No"))
    
    if com_bui == 'No':
        com_bui = 0
    else:
        com_bui = 1
    
    # When 'Predict' button is clicked, the 'prediction()' function must be called 
    # and the value returned by it must be stored in a variable, say 'price'. 
    # Print the value of 'price' and 'score' variable using the 'st.success()' and 'st.info()' functions respectively.
    if st.button("Predict"):
        st.subheader("Prediction results:")
        price, score, car_r2, car_mae, car_msle, car_rmse = prediction(car_data, car_width, engine_size, horse_power, drw_fwd, com_bui)
        st.success("The predicted price of the car: ${:,}".format(int(price)))
        st.info("Accuracy score of this model is: {:2.2%}".format(score))
        st.info(f"R-squared score of this model is: **{car_r2:.3f}**")  
        st.info(f"Mean absolute error of this model is: **{car_mae:.3f}**")  
        st.info(f"Mean squared log error of this model is: **{car_msle:.3f}**")  
        st.info(f"Root mean squared error of this model is: **{car_rmse:.3f}**")