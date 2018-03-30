# Using linear regression
# Accepts: Matrix of values retrieved from top-k values of Q2
# Result: array of w's
# w_0 + w_1 x_0 + w_2 x _1 ... + w_n w_n-1 = Target

from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split as tts
from sklearn import metrics
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta as rdel
from NarrowData import getID, getGranularityType
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def percentError(y_pred, y_test):
    y_pred, y_test = np.array(y_pred), np.array(y_test)
    return np.mean(np.abs((y_test - y_pred) / y_test)) * 100

def percentDif(y_pred, y_test):
    y_pred, y_test = np.array(y_pred), np.array(y_test)
    return np.mean(np.abs((y_test - y_pred) / (y_test/2))) * 100

def calculateTarget(corrMatrix, yValues, xValues, xTitle, yTitle, granu):
    fig1 = plt.figure()
    # ----- Plot the initial line graph -----
    target = corrMatrix[0]
    fig1 = plt.plot(xValues, yValues, label=yTitle)

    fig1 = plt.xlabel(xTitle)
    fig1 = plt.ylabel(yTitle)

    titleString = "Prediction of " + yTitle + " in the Next Timestamp"
    fig1 = plt.title(titleString)

    # ----- Prepare Data to use in Linear Regression -----
    # X = Attribute = [top-1, top-2, top-3, ... top-n][0]
    # y = Label = Target

    y = yValues
    X = corrMatrix

    #attribute = pd.DataFrame(corrMatrix)

    # Attribute - Independent (Timestamp)
    # Labels - Dependent (Value)

# ----- Train Data -----
    # 80% of data to training set, while 20% of it is to test set
    X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=0)

    # 90% of data to training set, 10% of it is to test set
    #X_train, X_test, y_train, y_test = tts(X, y, test_size=0.1, random_state=0)

    # 100% of data to training set, none to test set
    #X_train, X_test, y_train, y_test = tts(X, y, test_size=1, random_state=0)
    '''
    print('length of xValues: ', len(xValues))
    print('length of yValues: ', len(yValues))
    print('')
    print('Length of X_train: ', len(X_train))
    print('Length of X_test: ', len(X_test))
    print('Length of y_train: ', len(y_train))
    print('Length of y_test: ', len(y_test))
    '''
    reg = lr()
    reg.fit(X_train, y_train)

# ----- Test Data -----
    # ----- See if Linear Regression is accurate -----
    y_pred = reg.predict(X_test)

    #'''
    # ----- Display Actual data vs Predicted data -----
    print('')
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df)
    #'''

    # ----- Display Analysis section -----
    print()
    print('Analysis: ')
    print('R^2 prediction: ', reg.score(X_test, y_test))
    print('---')
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    perErr = percentError(y_pred, y_test)
    print('Percent Error:', perErr)
    perDif = percentDif(y_pred, y_test)
    print('Percent Difference:', perDif)
    print('---')

    # ----- Display Coefficients (weights) -----
    print('')
    coeff_df = pd.DataFrame(reg.coef_, X.columns, columns=['Coefficient'])
    print(coeff_df)
    print('')

    # ----- Quick Calculations -----
    target = y_pred[len(y_pred) - 1]      # predict in the next timestamp
    stamp = xValues[len(xValues) - 1]
    print('Last timestamp on graph: ', stamp)
    lab = yValues[len(yValues) - 1]
    print('Last value on graph: ', lab)

    predStamp = ''
    print(granu)

    '''if (granu == 'Daily'):
        predStamp = stamp + timedelta(days=1)
    elif(granu == 'Monthly'):
        predStamp = stamp + timedelta(months=1)
    elif(granu == 'Yearly'):
        predStamp = stamp + timedelta(years=1)
    '''
    if (granu == 'Daily'):
        predStamp = stamp + timedelta(days=1)
    elif (granu == 'Monthly'):
        predStamp = stamp + rdel(months=1)
    elif (granu == 'Yearly'):
        predStamp = stamp + rdel(years=1)

    print('Prediction timestamp: ', predStamp)

    # ----- Retrieve the values gotten from the correlation to calculate Target -----
    temp = []
    matrixLast = corrMatrix.tail(1).values.tolist()
    for item in matrixLast[0]:
        temp.append(item)
    corr = coeff_df['Coefficient'].values.tolist()
    '''
    print('')
    print(corrMatrix.tail(1))
    print('')

    print(temp)
    print(corr)
    '''
    # w_0 + w_1*x_0 + w_2*x_1 ... + w_n w_n-1 = Target
    prediction = reg.intercept_
    ctr = 0
    while (ctr < len(temp)):
        prediction = prediction + (temp[ctr] * corr[ctr])
        ctr = ctr + 1

    # End Results:
    fig1 = plt.plot(predStamp, prediction, 'or', c='k', label='Prediction in the Next Timestamp')
    legend = plt.legend()
    print('')
    print("X-Value: ", predStamp)
    print("Y-Value: ", prediction)


    frame = legend.get_frame()

    '''
    fig2 = plt.figure()
    fig2 = plt.plot(X_test, y_test, label='Linear Regression')
    fig2 = plt.plot(X_test, y_pred, c='g', label="Prediction")
    fig2 = plt.plot(predStamp, prediction, 'or', c='k', label="Prediction in the Next Timestamp")
    legent = plt.legend()
    frame = legend.get_frame()
    # Error: Ordinal must be >= 1
    '''

    plt.show()
    return
