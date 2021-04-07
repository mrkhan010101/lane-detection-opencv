import numpy as np
import pandas as pd
import time
def combo(lane_image, lines):
    # print(lane_image)
    # print(lines)
    x1= []
    x2= []
    y1= []
    y2= []
    for line in lines:
        a1, b1, a2, b2 = line.reshape(4)
        if(b1 - b2 >= 50):
            continue
        else:
            x1.append(a1)
            y1.append(b1)
            x2.append(a2)
            y2.append(b2)
            para = np.polyfit((a1,a2), (b1,b2), 1)
            slope = para[0]
            # print(slope)
    # df = pd.DataFrame({
    #     "X1": x1,
    #     "Y1": y1,
    #     "X2": x2,
    #     "Y2": y2,
    # })
    i = time.time()
    filename = "image %.2f" % i
    print(filename)
    # df.to_csv('%s.csv' %filename)