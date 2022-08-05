import numpy as np
import streamlit as st
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn import metrics


def app(df):
    # prepare the data for the model
    # select the only NOX as target variabel
    nox_df = df.copy()
    nox_df = nox_df.drop("CO", axis=1)  # drop the target variable CO

    # split the data for training and test using sklearn train_test_split function
    # split the data
    X = nox_df.iloc[:, 0:-1]
    y = nox_df["NOX"]

    # normalize the X and y.
    X = nox_df = Normalizer().fit_transform(X)
    # normalize the data

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, shuffle=True)

    #Linear regreesion
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    from sklearn.metrics import mean_absolute_error
    y_pred = linear_model.predict(X_test)
    mae_linear = mean_absolute_error(y_test, y_pred)

    #Random Forest Regressor
    model = RandomForestRegressor()
    # evaluate the model
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    n_scores = cross_val_score(model, X_train, y_train, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1,
                               error_score='raise')

    model = RandomForestRegressor(random_state=0)
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    with st.expander('View about Linear Regreesor'):
        st.markdown("""<p style='color:yellow'>
        Linear regression is one of the easiest and most popular Machine Learning algorithms. It is a statistical method that is used for predictive analysis. Linear regression makes predictions for continuous/real or numeric variables such as sales, salary, age, product price, etc.
        """, unsafe_allow_html=True)

        st.markdown("""<p style='color:yellow'>
        Linear regression algorithm shows a linear relationship between a dependent (y) and one or more independent (y) variables, hence called as linear regression. Since linear regression shows the linear relationship, which means it finds how the value of the dependent variable is changing according to the value of the independent variable. \
        """, unsafe_allow_html=True)
        st.markdown("""<p style='color:yellow'>
        The linear regression model provides a sloped straight line representing the relationship between the variables
        . Consider the below image:
        
        """, unsafe_allow_html=True)
        lin = Image.open("linear.png")
        st.image(lin, caption="Graph of a linear regression model")

        st.success(f"MAE Sore of our model is {mae_linear}")

    with st.expander("View about Random Forest Regressor"):
        rfr1 = Image.open('rfr1.png')
        st.image(rfr1)

        st.markdown("""<p style = 'color:pink'>
        Random Forest Regression is a supervised learning algorithm that uses ensemble learning method for regression. Ensemble learning method is a technique that combines predictions from multiple machine learning algorithms to make a more accurate prediction than a single model.
        """, unsafe_allow_html=True)

        rfr2  = Image.open('rfr2.png')
        st.image(rfr2)

        st.markdown("""<p style = 'color:pink'>
        The diagram above shows the structure of a Random Forest. You can notice that the trees run in parallel with no interaction amongst them. A Random Forest operates by constructing several decision trees during training time and outputting the mean of the classes as the prediction of all the trees
        """, unsafe_allow_html=True)
        st.success(f"MAE Score of our model is{mae}")
    with st.expander("Conclusion"):
        st.markdown("""<p style = 'color:red'>
        Looks like the Random forest works well on this dataset and is also better than the simple linear regression model. I just applied the random forest model with default parameters, and I'm amazed that a simple random forest model can fit the data so well
        
        """, unsafe_allow_html=True)
