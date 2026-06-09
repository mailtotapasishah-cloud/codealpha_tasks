import numpy as np

class Sort:
    def __init__(self):
        self.count = 0

    def update(self, detections):
        tracked = []
        for det in detections:
            x1,y1,x2,y2,conf = det
            self.count += 1
            tracked.append([x1,y1,x2,y2,self.count])
        return np.array(tracked)
