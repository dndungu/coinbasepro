from datetime import datetime
import numpy as np

class ohlcv:
    def __init__(self, x):
        self.n = len(x)
        self.at = np.array([datetime.fromtimestamp(v[0]) for v in x])
        self.open = np.array([v[3] for v in x])
        self.high = np.array([v[2] for v in x])
        self.low = np.array([v[1] for v in x])
        self.close = np.array([v[4] for v in x])
        self.price = np.array([0.5 * (v[3] + v[4]) for v in x])
        self.volume = np.array([v[5] for v in x])
