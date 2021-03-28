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

# [ 67 720 459 503] << left|| right>> [850 720 631 503]
# [ 74 720 461 503] << left|| right>> [841 720 630 503]
# [ 74 720 460 503] << left|| right>> [854 720 637 503]
# [ 71 720 456 503] << left|| right>> [849 720 637 503]
# [ 72 720 450 503] << left|| right>> [855 720 634 503]
# [ 66 720 456 503] << left|| right>> [839 720 633 503]
# [ 73 720 459 503] << left|| right>> [857 720 635 503]
# [ 64 720 448 503] << left|| right>> [853 720 639 503]
# [ 67 720 453 503] << left|| right>> [848 720 635 503]
# [ 72 720 459 503] << left|| right>> [855 720 636 503]