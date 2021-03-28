# [ 65 720 469 503] << lef[ 65 720 469 503]t|| right>> [860 720 631 503]

import numpy as np
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
left = np.array([ 65, 720, 469, 503]).reshape(-1,1)
right = np.array([860, 720, 631, 503]).reshape(-1,1)
lm.fit(left, right)
# LinearRegression.fit(left, right)
i = np.array([600]).reshape(-1,1)
pred = lm.predict(i)
print(pred.reshape(1))