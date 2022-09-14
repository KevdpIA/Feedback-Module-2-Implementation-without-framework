# Feedback Module 2: Implementation of ML without framework
# Kevin Joan Delgado Pérez A01706328
# 26/08/22

Implementation of a Machine Learning technique without frameworks, this is a part from an activity with feedback.

The study case consists in the management of a dataset with the information of the demand of bikes in Seoul, South Korea. Each column have different characteristics and the used in this activity:
  
 *  Dependent variable:
 
  - Rented Bike count : Count of bikes rented at each hour
  
 *  Independent variable:
 
  - Hour : Hour of he day
  - Temperature : Temperature in Celsius
  - Windspeed : m/s

In this code, are an implementation of a linear regression WIHTOUT FRAMEWORK to obtain the coefficents of the independent variables to model an equation for predict the count of bikes rented at each hour.

The objetive from use this method with the dataset of rented bikes in Seoul is learn the process of the Machine Learning to predict values with an optimization model(gradient descent), normalization method(min and max method) and a graphic that prints the mean of the error acumulations.

Finally, the print shows how the model learn and reduce the errors with each epoch of the path. The final values indicate the behavior of each one if you predict any value of the output, in this case, the count of rented bikes.

# Notes:


  ## If you want to run the code, install the dependencies with:
  
  
     pip install ./requirements.txt
  
  
  ## I ONLY use the framework sklearn to make the split data for the test of the model.
  
  
