# Feedback Module 2: Implementation of ML without framework
- Kevin Joan Delgado Pérez A01706328
- 26/08/22

Implementation of a Machine Learning technique without frameworks, this is a part from an activity with feedback.

The study case consists in the management of a dataset with the information of different wines, each column have different characteristics, for example:
  
  - Alcohol
  - Malic acid
  - Ash
  - Alcalinity of ash
  - Magnesium
  - Total phenols
  - Flavonoids
  - Nonflavanoid phenols
  - Proanthocyanins
  - Color intensity
  - Hue
  - OD280/OD315 of diluted wines
  - Prolines

In this code, is developed a linear regression to predict with an hypothesis, an output variable affected by four input variables.

The objetive to use this method with the dataset of wine is predict the Alcohol levels in wine according to the behaviors of Malic acid, Flavonoids, Proanthocyanins and Color intensity.

In the code, there is an optimization model(gradient descent), normalization method(min and max method) and a graphic that prints the mean of the error acumulations.

Finally, the print shows how the model learn and reduce the errors with each epoch of the path. The final values indicate the behavior of each one if you predict any value of the output, in this case, of the alcohol.
